#bin

import tensorflow as tf
#from matplotlib import pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
print mnist
print mnist.load_data()


