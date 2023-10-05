import datetime
import time

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

now_begin = int(round(time.time() * 1000))



X = tf.Variable(initial_value=np.random.randn(3,2)+3,dtype=float)
Y = tf.Variable(initial_value=1,dtype=float)

print('X',X)
# np.random.randn(100)表示
W = tf.Variable(initial_value=np.random.randn(3,2)+7,name="weight",dtype=float)

print('W',W)

# b= tf.Variable(tf.zeros([1,3]),name="bias",dtype=float)
# shape必须相同才可相乘
z = tf.multiply(X,W)

print('z',z)

now_end = int(round(time.time() * 1000))
print('execution time {} milliseconds'.format(now_end-now_begin))