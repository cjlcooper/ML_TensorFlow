# CNN

TensorFlow很适合用来进行大规模的数值计算。<br/>

### 开启TensorFlow会话

TensorFlow后台计算依赖于高效的C++，与后台的连接称为一个会话(session)。<br/>
TensorFlow中的程序使用，通常都是先创建一个图(graph)，然后在一个会话(session)里运行它。<br/>

### InteractiveSession
这里我们使用了一个更为方便的类，InteractiveSession，这能让你在构建代码时更加灵活。<br/>
