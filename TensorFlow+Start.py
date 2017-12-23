import numpy as np
import tensorflow as tf 

#Tensor
def addTensor():
	a = tf.constant([1.0, 2.0], name = 'a')
	b = tf.constant([3.0, 4.0], name = 'b')
	a+b
	print a.shape

#Session
def tfSession():
	# create a session
	sess = tf.Session()
	# use this session to run a result
	sess.close()

#Variable
def tfVariable():
	R = tf.Variable(tf.random_normal([2,3],mean=1,stddev=2))
	print R


#addTensor()
#tfSession()
#tfVariable()