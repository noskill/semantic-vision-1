import argparse
from PIL import Image

import numpy as np
import math

import tensorflow as tf
from keras.datasets import mnist
from tensorflow.contrib.layers import conv2d, conv2d_transpose, layer_norm, fully_connected

import random
import os
import time
import  rotatepair_batch
import plot_funs
""" Parameters """

BATCH_SIZE = 128
IMG_DIM    = (28, 28, 1)

CONV_DIM = (7, 7, 20)
INNER_LAYER_DIM = int(np.prod(CONV_DIM))

OUTPUT_DIM = 200
ITERS      = 200000
LEARNING_RATE = 1e-3

""" Model Definitions """

def prepare_mnist(X):
    X = (X.astype(np.float32) - 127.5)/127.5
    X = X[:, :, :, None]
    return X


def get_batch_only_Xb(X, Y):
    idx = np.random.randint(len(X), size=BATCH_SIZE)
    return X[idx], Y[idx]

def get_batch(X,Y):
    a = np.random.uniform(-1, 1, size=(BATCH_SIZE,))
    Xb,Yb  = get_batch_only_Xb(X, Y)
    sel_idx = (Yb == 4) | (Yb == 9)
    a[sel_idx] /= 4
    Xb_rot = rotatepair_batch.rotate_batch(Xb, a*180)
    return a, Xb, Xb_rot


def  plot_pair_samples(X1, X2, save_path):
    X1 = np.squeeze(X1)
    X2 = np.squeeze(X2)
    sh     = list(X1.shape)
    sh[0] += X2.shape[0]
    X = np.zeros(sh)

    X[0::2] = X1
    X[1::2] = X2
    plot_funs.plot_img_1D_given_2D(X, 8, 32, save_path)


def train():
    # Prepare Training Data
    (X_train, Y_train), (X_test, Y_test) = mnist.load_data()

    X_train = prepare_mnist(X_train)
    X_test = prepare_mnist(X_test)

    # Initialize Models
    real_data = tf.placeholder(tf.float32, (None, *IMG_DIM))
    real_data_rot = tf.placeholder(tf.float32, (None, *IMG_DIM), name="input_img")

    W = tf.constant(np.ones((OUTPUT_DIM, OUTPUT_DIM)), dtype=tf.float32, name="W")
	#use W=tf.constant... or W=tf.get_variable to use trainable W or constant W (different results)
	#W = tf.get_variable("W",(OUTPUT_DIM, OUTPUT_DIM))
    W = tf.reshape(W, (1, OUTPUT_DIM, OUTPUT_DIM))
    W = tf.tile(W, [tf.shape(real_data_rot)[0], 1, 1])

    W_control = tf.layers.conv2d(real_data_rot, 20, 5, 2, padding='same', activation=tf.nn.relu)
    W_control = tf.layers.conv2d(W_control, 10, 5, 2, padding='same', activation=tf.nn.relu)
    W_control = tf.contrib.layers.flatten(W_control)
    W_control = tf.layers.dense(W_control, OUTPUT_DIM * OUTPUT_DIM, activation=None)
    W_control = tf.reshape(W_control, [-1, OUTPUT_DIM, OUTPUT_DIM])

    W_control = tf.nn.softmax(W_control, dim=1)

    W_rez = W * W_control

    x = tf.contrib.layers.flatten(real_data_rot)

    x = tf.reshape(x, shape=[-1, 28, 28, 1])

    x = tf.layers.conv2d(x, 10, 5, 2, padding='same', activation=tf.nn.relu)
    x = tf.layers.conv2d(x, 20, 5, 2, padding='same', activation=tf.nn.relu)
    x = tf.contrib.layers.flatten(x)
    x = tf.layers.dense(x, 200, activation=None)
    x = tf.einsum('bi,bij->bj', x, W_rez)
    x = tf.layers.dense(x, INNER_LAYER_DIM, activation=None)
    x = tf.reshape(x, [-1, 7, 7, 20])
    y = tf.layers.conv2d_transpose(x, 10, 5, 2, padding='same', activation=tf.nn.relu)
    y = tf.layers.conv2d_transpose(y, 1, 5, 2, padding='same', activation=tf.nn.tanh)
    rec_data = tf.identity(y, "output_img")

    r_cost = tf.losses.mean_squared_error(rec_data, real_data)

    r_train_op = tf.train.AdamOptimizer(learning_rate=LEARNING_RATE).minimize(r_cost)

    saver = tf.train.Saver(max_to_keep=20)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    f_train_stat = open("train_log.txt", "w", buffering = 1)
    f_test_stat  = open("test_log.txt",  "w", buffering = 1)

    os.system("mkdir -p figs_rec")
    for it in range(ITERS):
        start_time = time.time()

        parameters, Xb, Xb_rot = get_batch(X_train, Y_train)
        r_cost_rez, _ = sess.run( [r_cost, r_train_op], feed_dict={real_data: Xb, real_data_rot: Xb_rot})

        f_train_stat.write("%i %g\n"%(it, r_cost_rez))

        print(it, (time.time() - start_time ))

        if ((it + 1) % 500 == 0):

            parameters, Xb, Xb_rot = get_batch(X_train, Y_train)
            samples = sess.run([rec_data], feed_dict={real_data: Xb, real_data_rot: Xb_rot})
            plot_pair_samples(Xb, samples, 'figs_rec/samples_%.6i_seen.png'%(it))

            parameters, Xb, Xb_rot = get_batch(X_test, Y_test)
            samples = sess.run([rec_data], feed_dict={real_data: Xb, real_data_rot: Xb_rot})
            plot_pair_samples(Xb, samples, 'figs_rec/samples_%.6i_unseen.png'%(it))


            r_cost_rez = sess.run(r_cost, feed_dict={real_data: Xb, real_data_rot: Xb_rot})
            f_test_stat.write("%i %g\n"%(it, r_cost_rez))

        if ((it + 1) % 10000 == 0):
            saver.save(sess, 'save/model', global_step=it)

    saver.save(sess, 'save/final-model')




train()
