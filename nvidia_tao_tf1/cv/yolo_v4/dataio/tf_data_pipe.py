# Copyright (c) 2019-2021, NVIDIA CORPORATION.  All rights reserved.

"""IVA YOLO v4 data loader builder."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import tensorflow as tf

import nvidia_tao_tf1.core as tao_core
from nvidia_tao_tf1.cv.ssd.utils.tensor_utils import get_non_empty_rows_2d_sparse
from nvidia_tao_tf1.cv.yolo_v3.data_loader.augmentation import (
    outer_augmentations
)
from nvidia_tao_tf1.cv.yolo_v3.data_loader.yolo_v3_data_loader import build_dataloader


def unstack_images(images, shapes, bs):
    """unstack images into a list of images."""
    images_list = []
    for b_idx in range(bs):
        image = images[b_idx, ...]
        shape = shapes[b_idx, ...]
        image = image[0:shape[0], 0:shape[1], ...]
        images_list.append(image)
    return images_list


def tf_regular_augmentation(image, label, training, w_tensor, h_tensor, augmentation_config):
    """Function to do non-mosaic augmentation."""

    ratio = tf.cast(w_tensor, tf.float32) / tf.cast(h_tensor, tf.float32)

    if training:
        aug_img, aug_label = outer_augmentations(
            image,
            label[:, 2:6],
            ratio,
            augmentation_config
        )
        aug_img = tf.image.resize_images(aug_img, [h_tensor, w_tensor])
    else:
        aug_img, aug_label = image, label[:, 2:6]

    aug_img.set_shape([None, None, 3])
    aug_img = tf.transpose(aug_img, (2, 0, 1))
    aug_label = tf.concat([label[:, 0:2], aug_label], axis=-1)
    # filter out bad boxes after augmentation
    aug_x1 = aug_label[:, 2]
    aug_x2 = aug_label[:, 4]
    aug_y1 = aug_label[:, 3]
    aug_y2 = aug_label[:, 5]
    # only select valid labels
    select = tf.logical_and(
        aug_x2 - aug_x1 > 1e-3,
        aug_y2 - aug_y1 > 1e-3
    )
    aug_label = tf.boolean_mask(aug_label, select)

    return aug_img, aug_label


def _resize_box(box, t_shift, l_shift, h_ratio, w_ratio):
    """Helper function to resize labels in mosaic."""

    xmin = l_shift + w_ratio * box[:, -4]
    xmax = l_shift + w_ratio * box[:, -2]
    ymin = t_shift + h_ratio * box[:, -3]
    ymax = t_shift + h_ratio * box[:, -1]
    return tf.stack([xmin, ymin, xmax, ymax], axis=-1)


def tf_do_mosaic(images, labels, min_ratio, w_tensor, h_tensor, augmentation_config):
    """Function to do mosaic augmentation."""
    assert 0 < min_ratio < 0.5, "mosaic_min_ratio must in range (0, 0.5)"

    # Step 1. determine border
    thlw_ratio = tf.random.uniform([2], minval=min_ratio, maxval=1.0-min_ratio)
    th = tf.cast(tf.math.round(thlw_ratio[0] * tf.cast(h_tensor, tf.float32)), tf.int32)
    bh = h_tensor - th
    lw = tf.cast(tf.math.round(thlw_ratio[1] * tf.cast(w_tensor, tf.float32)), tf.int32)
    rw = w_tensor - lw

    # Step 2. Generate 4 images with respect shape

    # top-left
    aug_img0, aug_label0 = outer_augmentations(
        images[0],
        labels[0][:, 2:6],
        tf.cast(lw, tf.float32) / tf.cast(th, tf.float32),
        augmentation_config
    )

    # top-right
    aug_img1, aug_label1 = outer_augmentations(
        images[1],
        labels[1][:, 2:6],
        tf.cast(rw, tf.float32) / tf.cast(th, tf.float32),
        augmentation_config
    )

    # bottom-left
    aug_img2, aug_label2 = outer_augmentations(
        images[2],
        labels[2][:, 2:6],
        tf.cast(lw, tf.float32) / tf.cast(bh, tf.float32),
        augmentation_config
    )

    # bottom-right
    aug_img3, aug_label3 = outer_augmentations(
        images[3],
        labels[3][:, 2:6],
        tf.cast(rw, tf.float32) / tf.cast(bh, tf.float32),
        augmentation_config
    )

    # Step 3. make new images
    shape = tf.stack([h_tensor, w_tensor, 3], axis=0)

    # top-left
    h_idx = tf.range(0, th, delta=1)
    w_idx = tf.range(0, lw, delta=1)
    h_idx, w_idx = tf.meshgrid(h_idx, w_idx)
    h_idx = tf.reshape(tf.transpose(h_idx), (-1,))
    w_idx = tf.reshape(tf.transpose(w_idx), (-1,))
    # (k, 2)
    indices = tf.stack([h_idx, w_idx], axis=1)
    aug_img0 = tf.image.resize_images(aug_img0, [th, lw])

    updates = tf.reshape(
        aug_img0,
        (-1, 3)
    )

    aug_img0 = tf.scatter_nd(
        indices,
        updates,
        shape
    )

    # top-right
    h_idx = tf.range(0, th, delta=1)
    w_idx = tf.range(lw, w_tensor, delta=1)
    h_idx, w_idx = tf.meshgrid(h_idx, w_idx)
    h_idx = tf.reshape(tf.transpose(h_idx), (-1,))
    w_idx = tf.reshape(tf.transpose(w_idx), (-1,))
    # (k, 2)
    indices = tf.stack([h_idx, w_idx], axis=1)
    aug_img1 = tf.image.resize_images(aug_img1, [th, rw])

    updates = tf.reshape(
        aug_img1,
        (-1, 3)
    )

    aug_img1 = tf.scatter_nd(
        indices,
        updates,
        shape
    )

    # bottom-left
    h_idx = tf.range(th, h_tensor, delta=1)
    w_idx = tf.range(0, lw, delta=1)
    h_idx, w_idx = tf.meshgrid(h_idx, w_idx)
    h_idx = tf.reshape(tf.transpose(h_idx), (-1,))
    w_idx = tf.reshape(tf.transpose(w_idx), (-1,))
    # (k, 2)
    indices = tf.stack([h_idx, w_idx], axis=1)
    aug_img2 = tf.image.resize_images(aug_img2, [bh, lw])

    updates = tf.reshape(
        aug_img2,
        (-1, 3)
    )

    aug_img2 = tf.scatter_nd(
        indices,
        updates,
        shape
    )

    # bottom-right
    h_idx = tf.range(th, h_tensor, delta=1)
    w_idx = tf.range(lw, w_tensor, delta=1)
    h_idx, w_idx = tf.meshgrid(h_idx, w_idx)
    h_idx = tf.reshape(tf.transpose(h_idx), (-1,))
    w_idx = tf.reshape(tf.transpose(w_idx), (-1,))
    # (k, 2)
    indices = tf.stack([h_idx, w_idx], axis=1)
    aug_img3 = tf.image.resize_images(aug_img3, [bh, rw])

    updates = tf.reshape(
        aug_img3,
        (-1, 3)
    )

    aug_img3 = tf.scatter_nd(
        indices,
        updates,
        shape
    )

    aug_img = aug_img0 + aug_img1 + aug_img2 + aug_img3

    aug_img.set_shape([None, None, 3])

    # Step 4. make new labels

    th_ratio = tf.cast(th, tf.float32) / tf.cast(h_tensor, tf.float32)
    bh_ratio = tf.cast(bh, tf.float32) / tf.cast(h_tensor, tf.float32)
    lw_ratio = tf.cast(lw, tf.float32) / tf.cast(w_tensor, tf.float32)
    rw_ratio = tf.cast(rw, tf.float32) / tf.cast(w_tensor, tf.float32)

    aug_label0 = _resize_box(aug_label0, 0,
                             0,
                             th_ratio,
                             lw_ratio)

    aug_label1 = _resize_box(aug_label1, 0,
                             lw_ratio,
                             th_ratio,
                             rw_ratio)

    aug_label2 = _resize_box(aug_label2, th_ratio,
                             0,
                             bh_ratio,
                             lw_ratio)

    aug_label3 = _resize_box(aug_label3, th_ratio,
                             lw_ratio,
                             bh_ratio,
                             rw_ratio)

    aug_label = tf.concat([aug_label0, aug_label1, aug_label2, aug_label3], axis=0)

    aug_label_first_2dim = tf.concat([x[:, 0:2] for x in labels], axis=0)

    aug_img = tf.transpose(aug_img, (2, 0, 1))
    aug_label = tf.concat([aug_label_first_2dim, aug_label], axis=-1)

    # filter out bad boxes after augmentation
    aug_x1 = aug_label[:, 2]
    aug_x2 = aug_label[:, 4]
    aug_y1 = aug_label[:, 3]
    aug_y2 = aug_label[:, 5]
    # only select valid labels
    select = tf.logical_and(
        aug_x2 - aug_x1 > 1e-3,
        aug_y2 - aug_y1 > 1e-3
    )
    aug_label = tf.boolean_mask(aug_label, select)

    return aug_img, aug_label


class YOLOv4TFDataPipe:
    """
    Data loader class.

    DataLoader can be used in two ways:
    1. build groundtruth image and label TF tensors. Those two tensors can be
        directly used for training.
    2. build a generator that yields image and label numpy arrays. In this case,
        a TF session needs to be passed into the class initializer.
    """

    def __init__(self,
                 experiment_spec,
                 label_encoder=None,
                 training=True,
                 sess=None,
                 h_tensor=None,
                 w_tensor=None,
                 visualizer=None,
                 rank=0):
        """
        Data loader init function.

        Arguments:
            experiment_spec: The loaded config pb2.
            label_encoder (function, optional): If passed in, groundtruth label will be encoded.
            training (bool): Return training set or validation set.
            sess (TF Session): Required if generator() function needs to be called. Otherwise, just
                pass None.
            visualizer(object): The Visualizer object.
            rank(int): Horovod rank.
        """
        dataset_proto = experiment_spec.dataset_config
        self._exclude_difficult = not dataset_proto.include_difficult_in_training
        dataloader = build_dataloader(
            dataset_proto=dataset_proto,
            augmentation_proto=experiment_spec.augmentation_config,
            h_tensor=h_tensor,
            w_tensor=w_tensor,
            training=training
        )
        self.dataloader = dataloader
        if training:
            batch_size = experiment_spec.training_config.batch_size_per_gpu
        else:
            batch_size = experiment_spec.eval_config.batch_size

        mosaic_prob = experiment_spec.augmentation_config.mosaic_prob
        if training and mosaic_prob > 1e-3:
            mosaic_max_bs = int(math.ceil(mosaic_prob * batch_size))
            mosaic_min_bs = int(math.floor(mosaic_prob * batch_size))
        else:
            mosaic_max_bs = 0
            mosaic_min_bs = 0

        raw_bs = batch_size + 3 * mosaic_max_bs

        self.batch_size = batch_size
        self.images, self.ground_truth_labels, self.shapes, self.num_samples = \
            dataloader.get_dataset_tensors(
                raw_bs
            )
        # original images for debugging
        self._images = self.images
        if self.num_samples == 0:
            return
        self.n_batches = (self.num_samples + self.batch_size - 1) // self.batch_size
        cls_mapping_dict = experiment_spec.dataset_config.target_class_mapping
        self.classes = sorted({str(x) for x in cls_mapping_dict.values()})
        cls_map = tao_core.processors.LookupTable(
            keys=self.classes,
            values=list(range(len(self.classes))),
            default_value=-1)
        cls_map.build()
        self.encode_fn = label_encoder

        gt_labels = []
        source_classes = self.ground_truth_labels.object_class
        mapped_classes = tf.SparseTensor(
            values=cls_map(source_classes.values),
            indices=source_classes.indices,
            dense_shape=source_classes.dense_shape
        )
        mapped_labels = self.ground_truth_labels._replace(object_class=mapped_classes)
        valid_indices = tf.not_equal(mapped_classes.values, -1)
        filtered_labels = mapped_labels.filter(valid_indices)
        filtered_obj_ids = tf.sparse.reshape(filtered_labels.object_class,
                                             [raw_bs, -1, 1])
        filtered_coords = tf.sparse.reshape(filtered_labels.vertices.coordinates,
                                            [raw_bs, -1, 4])
        filtered_occlusion = tf.sparse.reshape(
            filtered_labels.occlusion,
            [raw_bs, -1, 1]
        )
        filtered_obj_ids = tf.sparse.SparseTensor(
            values=tf.cast(tf.round(filtered_obj_ids.values), tf.float32),
            indices=filtered_obj_ids.indices,
            dense_shape=filtered_obj_ids.dense_shape
        )
        filtered_coords = tf.sparse.SparseTensor(
            values=tf.cast(filtered_coords.values, tf.float32),
            indices=filtered_coords.indices,
            dense_shape=filtered_coords.dense_shape
        )
        filtered_occlusion = tf.sparse.SparseTensor(
            values=tf.cast(filtered_occlusion.values, tf.float32),
            indices=filtered_occlusion.indices,
            dense_shape=filtered_occlusion.dense_shape,
        )
        labels_all = tf.sparse.concat(
            axis=-1,
            sp_inputs=[filtered_obj_ids, filtered_occlusion, filtered_coords]
        )
        labels_split = tf.sparse.split(sp_input=labels_all, num_split=raw_bs,
                                       axis=0)
        labels_split = [tf.sparse.reshape(x, [-1, 6]) for x in labels_split]
        labels = [tf.sparse.to_dense(get_non_empty_rows_2d_sparse(x)) for x in labels_split]
        print_op = tf.print(
            "Got label marked as difficult(occlusion > 0), "
            "please set occlusion field in KITTI label to 0 "
            "and re-generate TFRecord dataset "
            "or set `dataset_config.include_difficult_in_training` to True "
            "in spec file, if you want to include it in training."
        )

        def _print_fn():
            with tf.control_dependencies([print_op]):
                return tf.constant([])

        def _no_print_fn():
            return tf.constant([])
        for l_idx, l in enumerate(labels):
            obj_id = tf.cast(l[:, 0], tf.float32)
            is_difficult = tf.cast(l[:, 1], tf.float32)
            x1 = l[:, 2] / tf.cast(self.shapes[l_idx, 1], tf.float32)
            x2 = l[:, 4] / tf.cast(self.shapes[l_idx, 1], tf.float32)
            y1 = l[:, 3] / tf.cast(self.shapes[l_idx, 0], tf.float32)
            y2 = l[:, 5] / tf.cast(self.shapes[l_idx, 0], tf.float32)
            # only select valid labels
            select = tf.logical_and(
                tf.not_equal(obj_id, -1),
                tf.logical_and(tf.less(x1, x2), tf.less(y1, y2))
            )
            label = tf.stack([obj_id, is_difficult, x1, y1, x2, y2], axis=1)
            label = tf.boolean_mask(label, select)
            # exclude difficult boxes is forced to do so
            if self._exclude_difficult:
                print_cond = tf.cond(
                    tf.reduce_any(tf.cast(label[:, 1], tf.bool)),
                    true_fn=_print_fn,
                    false_fn=_no_print_fn,
                )
                with tf.control_dependencies([print_cond]):
                    label = tf.boolean_mask(
                        label,
                        tf.math.logical_not(tf.cast(label[:, 1], tf.bool))
                    )
            gt_labels.append(label)
        self.gt_labels = gt_labels
        self.frame_ids = self.ground_truth_labels.frame_id
        # images
        images_list = unstack_images(
            self.images,
            self.shapes,
            raw_bs
        )

        augmented_images = []
        augmented_labels = []

        # @zeyuz: define outside loop to avoid static test failures
        images = []
        labels = []

        # step 1. add mosaic batch
        mosaic_min_ratio = experiment_spec.augmentation_config.mosaic_min_ratio

        for b_idx in range(mosaic_min_bs):
            for i_idx in range(4):
                idx = b_idx * 4 + i_idx
                images.append(images_list[idx])
                labels.append(self.gt_labels[idx])

            aug_img, aug_label = tf_do_mosaic(images, labels, mosaic_min_ratio,
                                              w_tensor, h_tensor,
                                              experiment_spec.augmentation_config)

            # reset imgs, labels
            images = []
            labels = []

            augmented_images.append(aug_img)
            augmented_labels.append(aug_label)

        # step 2. add maybe mosaic image
        if mosaic_max_bs > mosaic_min_bs:
            # equation to satisfy: (mosaic_min_bs + mosaic_img_prob) / bs = mosaic_prob
            mosaic_img_prob = mosaic_prob * batch_size - mosaic_min_bs
            for i_idx in range(4):
                idx = mosaic_min_bs * 4 + i_idx
                images.append(images_list[idx])
                labels.append(self.gt_labels[idx])

            aug_img, aug_label = tf.cond(
                tf.random.uniform([]) < mosaic_img_prob,
                true_fn=lambda: tf_do_mosaic(images, labels, mosaic_min_ratio,
                                             w_tensor, h_tensor,
                                             experiment_spec.augmentation_config),
                false_fn=lambda: tf_regular_augmentation(images[0], labels[0], training,
                                                         w_tensor, h_tensor,
                                                         experiment_spec.augmentation_config)
            )

            augmented_images.append(aug_img)
            augmented_labels.append(aug_label)

        # step 3. add non-mosaic image
        for b_idx in range(batch_size - mosaic_max_bs):
            aug_img, aug_label = tf_regular_augmentation(images_list[mosaic_max_bs * 4 + b_idx],
                                                         self.gt_labels[mosaic_max_bs * 4 + b_idx],
                                                         training,
                                                         w_tensor, h_tensor,
                                                         experiment_spec.augmentation_config)

            augmented_images.append(aug_img)
            augmented_labels.append(aug_label)

        self.images = tf.stack(augmented_images, axis=0)
        num_channels = experiment_spec.augmentation_config.output_channel
        image_depth = int(experiment_spec.augmentation_config.output_depth) or 8
        # See conversion: https://pillow.readthedocs.io/en/3.2.x/reference/Image.html
        bgr_ = tf.reshape(
            tf.constant([0.1140, 0.5870, 0.2990], dtype=tf.float32),
            (1, 3, 1, 1)
        )
        # Vis the augmented images in TensorBoard, only rank 0
        if rank == 0 and visualizer is not None:
            # TensorBoard image summary only supports 8-bit images
            if visualizer.enabled and image_depth == 8:
                if num_channels == 3:
                    aug_images = self.images
                else:
                    # Project RGB to grayscale
                    aug_images = tf.reduce_sum(
                        self.images * bgr_,
                        axis=1,
                        keepdims=True
                    )
                aug_images = tf.transpose(aug_images, (0, 2, 3, 1))
                _max_box_num = tf.shape(augmented_labels[0])[0]
                for _aug_label in augmented_labels[1:]:
                    _max_box_num = tf.reduce_max(
                        tf.stack([_max_box_num, tf.shape(_aug_label)[0]], axis=0)
                    )
                _aug_label_list = []
                for _aug_label in augmented_labels:
                    _num_pad = _max_box_num - tf.shape(_aug_label)[0]
                    _aug_label_list.append(tf.pad(_aug_label, [(0, _num_pad), (0, 0)]))
                _aug_label_concat = tf.stack(_aug_label_list, axis=0)[:, :, 2:]
                # (xmin, ymin, xmax, ymax) to (ymin, xmin, ymax, xmax)
                _aug_label_concat = tf.gather(_aug_label_concat, [1, 0, 3, 2], axis=2)
                aug_images = tf.image.draw_bounding_boxes(
                    aug_images,
                    _aug_label_concat
                )
                aug_images = tf.cast(aug_images, tf.uint8)
                visualizer.image(
                    "augmented_images",
                    aug_images,
                    data_format="channels_last"
                )
        self._images = self.images
        self.gt_labels = augmented_labels
        img_mean = experiment_spec.augmentation_config.image_mean
        if experiment_spec.augmentation_config.output_channel == 3:
            assert image_depth == 8, (
                f"RGB images only support 8-bit depth, got {image_depth}, "
                "please check `augmentation_config.output_depth` in spec file"
            )
            if img_mean:
                bb, gg, rr = img_mean['b'], img_mean['g'], img_mean['r']
            else:
                bb, gg, rr = 103.939, 116.779, 123.68
        else:
            if img_mean:
                bb, gg, rr = img_mean['l'], img_mean['l'], img_mean['l']
            elif image_depth == 8:
                bb, gg, rr = 117.3786, 117.3786, 117.3786
            elif image_depth == 16:
                # 117.3786 * 256
                bb, gg, rr = 30048.9216, 30048.9216, 30048.9216
            else:
                raise ValueError(
                    f"Unsupported image depth: {image_depth}, should be 8 or 16, "
                    "please check `augmentation_config.output_depth` in spec file"
                )
        perm = tf.constant([2, 1, 0])
        self.images = tf.gather(self.images, perm, axis=1)
        self.images -= tf.constant([[[[bb]], [[gg]], [[rr]]]])
        if num_channels == 1:
            self.images = tf.reduce_sum(self.images * bgr_, axis=1, keepdims=True)
        self.encoded_labels = self.gt_labels
        if self.encode_fn is not None:
            self.encoded_labels = self.encode_fn(self.gt_labels)
        self.sess = sess

    def set_encoder(self, label_encoder):
        """Set a new label encoder for output labels."""
        self.encode_fn = label_encoder
        self.encoded_labels = self.encode_fn(self.gt_labels)

    def generator(self):
        """Yields img and label numpy arrays."""

        if self.sess is None:
            raise ValueError('TF session can not be found. Pass a session to the initializer!')
        while True:
            img, enc_label, label = self.sess.run(
                [self.images, self.encoded_labels, self.gt_labels]
            )
            yield img, enc_label, label

    def get_array(self):
        '''get the array for a batch.'''
        return self.sess.run([self.images, self.gt_labels])

    def get_array_and_frame_ids(self):
        '''get the array and frame IDs for a batch.'''
        return self.sess.run([self.frame_ids, self.images, self.gt_labels])
