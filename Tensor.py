import tensorflow as tf

# create session
sess = tf.InteractiveSession()

# zeros
zeros_matrix = tf.zeros(shape=[2,2])
print sess.run(zeros_matrix)

# ones
ones_matirx = tf.ones(shape=[3,3])
print sess.run(ones_matirx)

# fill
fill_matirx = tf.fill([4,4],9)
print sess.run(fill_matirx)

# constant
constant_matrix = tf.constant([1,2,3,4,5,6,7,8,9],shape=[3,3])
print sess.run(constant_matrix)