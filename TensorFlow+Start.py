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
	R = tf.Variable(0, name='counter')
	one = tf.constant([1,2])
	two = tf.constant([2,3])
	new_value = tf.add(R,1)
	update = tf.assign(R, new_value)
	with tf.Session() as sess:
		print sess.run(one+two)
		#sess.run(new_value)
		#sess.run(update)


# Math function
def mathFunction():
	a = tf.constant(10)
	b = tf.constant(32)
	with tf.Session() as sess:
		print 'a = 10,b = 32'
		print 'Addition with constants: %i' % sess.run(a+b)
		print 'Multiplication with constants %i' % sess.run(a*b)

	sess1 = tf.Session()
	print sess1.run(a-b)


# Create Image
def CreateImage():
	matrix1 = tf.constant([3,3])
	matrix2 = tf.constant([2,2])
	# multiplication
	product = matrix1+matrix2
	with tf.Session() as sess:
		result = sess.run([product])
		print result



# Fetches
def FetchesFunction():
	print 'Fetches ...'
	input1 = tf.constant(3.0)
	input2 = tf.constant(2.0)
	input3 = tf.constant(5.0)
	intermed = tf.add(input2,input3)
	mul = tf.multiply(input1,intermed)
	# session run
	with tf.Session() as sess:
		result = sess.run([mul, intermed])
		print result

# Feeds
def FeedsFunction():
	input1 = tf.placeholder(tf.float32)
	input2 = tf.placeholder(tf.float32)
	output = tf.multiply(input1,input2)
	# session run
	with tf.Session() as sess:
		print (sess.run([output], feed_dict={input1:[7.], input2:[2.]}))


FeedsFunction()









