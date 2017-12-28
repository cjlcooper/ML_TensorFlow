import numpy as np
import tensorflow as tf 

# y = x * 0.1 + 0.3
x_data = np.random.rand(100).astype("float32")
y_data = x_data * 0.1 + 0.3

# if y=kx+b,we should get k and b.
# set k and b value
k = tf.Variable(tf.random_uniform([1],-1.0,1.0))
b = tf.Variable(tf.zeros([1]))
y = k * x_data + b

# Mini func loss
loss = tf.reduce_mean(tf.square(y - y_data))#get ping jun zhi
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)