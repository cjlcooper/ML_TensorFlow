import numpy as np
import tensorflow as tf 

#Tensor
def addTensor():
	a = tf.constant([1.0, 2.0], name = 'a')
	b = tf.constant([3.0, 4.0], name = 'b')
	print a+b

#Session
def tfSession():
	# create a session
	sess = tf.Session()
	# use this session to run a result
	a = tf.constant([1.0, 2.0], name = 'a')
	b = tf.constant([3.0, 4.0], name = 'b')
	print sess.run(a+b)
	c = tf.constant(10)
	d = tf.constant(12)
	print sess.run(c+d)
	sess.close()

#Variable
def tfVariable():
	R = tf.Variable(tf.random_normal([2,3],mean=1,stddev=2))
	print R

# Math function
def mathFunction():
	a = tf.constant(10)
	b = tf.constant(32)
	with tf.Session() as sess:
		print 'a = 10,b = 32'
		print 'Addition with constants: %i' % sess.run(a+b)
		print 'Multiplication with constants %i' % sess.run(a*b)


addTensor()
tfSession()
tfVariable()
mathFunction()