import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# Import Data
mnist = input_data.read_data_sets("../MNIST_data", one_hot=True)
print mnist

# create session
sess = tf.InteractiveSession()

# Create Modle -----------
# y = kx + b
# a = softmax(y)
# get a

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])
k = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
a = tf.nn.softmax(tf.matmul(x, k)+b)
sess.run(tf.global_variables_initializer())

# loss function
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y * tf.log(a), reduction_indices=[1])) 
optimizer = tf.train.GradientDescentOptimizer(0.5) # rate is 0.5
train = optimizer.minimize(cross_entropy) # goal:min loss function

# Test trained model
correct_prediction = tf.equal(tf.argmax(a, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    train.run({x: batch_xs, y: batch_ys})
print(sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels}))