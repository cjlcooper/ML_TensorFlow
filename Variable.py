import tensorflow as tf

sess = tf.InteractiveSession()

tensor = tf.fill([9,9],9)
variable = tf.Variable(tensor)
sess.run(tf.global_variables_initializer())
print (sess.run(variable))