import tensorflow as tf

x = tf.placeholder(tf.float32,[1, 5],name='input')
y = tf.placeholder(tf.float32,[None, 5],name='input')

sess = tf.InteractiveSession()
print x