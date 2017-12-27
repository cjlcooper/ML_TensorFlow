# Note

## 简介
一个使用数据流图(data flow graphs)技术来进行数值计算的开源软件库。<br/>

### 数据流图(Data Flow Graph)
数据流图是描述有向图中的数值计算过程。<br/>

### 概览
TensorFlow是一种将计算表示为图的编程系统。<br/>
图中的节点称为ops(operation的简称),既任务。<br/>
一个ops使用0个或以上的Tensors，通过执行某些运算，产生0个或以上的Tensors。<br/>
一个Tensor是一个多维数组，例如，你可以将一批图像表示为一个四维的数组[batch, height, width, channels]，数组中的值均为浮点数。<br/>
TensorFlow中的图描述了计算过程，图通过Session的运行而执行计算。<br/>
Session将图的节点们(即ops)放置到计算设备(如CPUs和GPUs)上，然后通过方法执行它们；这些方法执行完成后，将返回tensors。<br/>
-  在Python中的tensor的形式是numpy ndarray对象，而在C/C++中则是tensorflow::Tensor。<br/>
-  将计算流程表示成图；
-  通过Sessions来执行图计算；
-  将数据表示为tensors；
-  使用Variables来保持状态信息；
-  分别使用feeds和fetches来填充数据和抓取任意的操作结果；

#### 施工阶段
创建一个图来表示和训练神经网络;<br/>
#### 执行阶段
在图中重复执行一系列的训练操作;<br/>

### Session
#### 会话持有并管理tensorflow程序运行时的所有资源
#### PS:所有计算均要用session.run(...)方法执行

### Tensor
#### 在Tensorflow中，所有的数据都通过张量的形式表示:
TensorFlow中使用tensor数据结构（实际上就是一个多维数据）表示所有的数据,并在图计算中的节点之间传递数据;<br/>
1.零阶张量表示标量，即一个数；<br/>
2.一阶张量为向量，即一维数组；n阶张量理解为一个n维的数组；<br/>
3.但是张量不真正的保存数字，它保存的是如何得道这些数字的计算过程，即操作。<br/>
#### 概要：<br/>
1.主要保存了三个重要属性(当然也具有其他属性)：name、shape(张量维度)、type(张量类型);
2.name:张量的唯一标识符，同时可以看出他的计算方式,张量的命名形式：“node:src_output”;<br/>
  node：节点名称<br/>
  src_output：张量来自节点的第几个输出(从0开始编号)<br/>

### Variable
#### 变量：保存和更新网络中的参数;
tf.Variable()<br/>

### placeholder
#### 占位符，同样是一个抽象的概念
告诉系统：这里有一个值/向量/矩阵，现在我没法给你具体数值，不过我正式运行的时候会补上的;<br/>

### 创建tf矩阵
1.tf.zeros<br/>
2.tf.ones<br/>
3.tf.fill<br/>
4.tf.constant<br/>

### Fetches（抓取）
为了抓取ops的输出，需要先执行session的run函数，可通过print函数打印状态信息。<br/>
所有tensors的输出都是一次性 [连贯] 执行的。<br/>

### Feeds（填充）
TensorFlow也提供这样的机制：先创建特定数据类型的占位符(placeholder)，之后再进行数据的填充。<br/>
如果不对placeholder()的变量进行数据填充，将会引发错误。<br/>


### Others
1.通过tf.constant创建一个常量;<br/>
