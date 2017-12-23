# Note

### Session
#### 会话持有并管理tensorflow程序运行时的所有资源
#### PS:所有计算均要用session.run(...)方法执行

### Tensor
#### 在Tensorflow中，所有的数据都通过张量的形式表示:
1.零阶张量表示标量，即一个数；<br/>
2.一阶张量为向量，即一维数组；n阶张量理解为一个n维的数组；<br/>
3.但是张量不真正的保存数字，它保存的是如何得道这些数字的计算过程，即操作。<br/>
#### 概要：<br/>
1.主要保存了三个重要属性(当然也具有其他属性)：name、shape(张量维度)、type(张量类型);
2.name:张量的唯一标识符，同时可以看出他的计算方式,张量的命名形式：“node:src_output”;<br/>
  node：节点名称<br/>
  src_output：张量来自节点的第几个输出(从0开始编号)<br/>

### Variable
#### 变量：保存和更新网络中的参数

### 创建tf矩阵
1.tf.zeros<br/>
2.tf.ones<br/>
3.tf.fill<br/>
4.tf.constant<br/>
