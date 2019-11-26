from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from autorecsys.pipeline.base import Block


class RatingPredictionOptimizer(Block):
    """
    latent factor optimizer for cateory datas
    """

    def build(self, hp, inputs=None):
        input_node = tf.concat(inputs, axis=1)
        output_node = tf.keras.layers.Dense(1)(input_node)
        output_node = tf.reshape(output_node, [-1])
        return output_node

    @property
    def metric(self):
        return tf.keras.metrics.MeanSquaredError(name='mse')

    @property
    def loss(self):
        return tf.keras.losses.MeanSquaredError(name='mse')



class PointWiseOptimizer(Block):
    """
    latent factor optimizer for cateory datas
    """

    def build(self, hp, inputs=None):
        input_node = tf.concat(inputs, axis=1)
        output_node = tf.keras.layers.Dense(1, activation='sigmoid')(input_node)
        output_node = tf.reshape(output_node, [-1])
        return output_node

    @property
    def metric(self):
        return tf.keras.metrics.BinaryCrossentropy(name='BinaryCrossentropy')

    @property
    def loss(self):
        return tf.keras.losses.BinaryCrossentropy(name='BinaryCrossentropy')
