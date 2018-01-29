import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

# Create modle
# y = kx + b
k = tf.Variable(tf.random_uniform([1],-1.0,1.0))
b = tf.Variable(tf.zeros([1]))
y = k*x_data + b

# Set loss
loss = tf.reduce_mean(tf.square(y-y_data))

# Op
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# Training
initV = tf.global_variables_initializer()

sess = tf.Session()
sess.run(initV)

for step in range(200):
    sess.run(train)
    print (step,sess.run(k),sess.run(b))
