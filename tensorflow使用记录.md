# tensorflow

## api 使用

### 常量值函数

- [`tf.constant(value, dtype, shape, name)`](tensorflow/tf_api.py)

```
生成常量：

a = tf.constant([[1, 2, 3], [4, 5, 6]], tf.int32)
b = tf.constant(1)

结果：
Tensor("Const:0", shape=(2, 3), dtype=int32)
Tensor("Const_1:0", shape=(), dtype=int32)
```

- [`tf.zeros(shape, dtype=tf.float32, name=None)`](tensorflow/tf_api.py)
- [`tf.zeros_like(tensor, dtype=None, name=None)`](tensorflow/tf_api.py)
- [`tf.ones(shape, dtype=tf.float32, name=None)`](tensorflow/tf_api.py)
- [`tf.ones_like(tensor, dtype=None, name=None)`](tensorflow/tf_api.py)

```
执行：
zeros = tf.zeros([1,2,1], dtype=tf.int32)
ones = tf.ones_like(zeros, dtype=None, name=None)

结果：
Tensor("zeros:0", shape=(1, 2, 1), dtype=int32)
Tensor("ones_like:0", shape=(1, 2, 1), dtype=int32)
```

### 生成随机数函数

- [`tf.random_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None`)](tensorflow/tf_api.py)

```
执行：
tf.random_normal(shape=[2,3], mean=0, stddev=1)

结果：
Tensor("random_normal:0", shape=(2, 3), dtype=float32)
```

### 变量函数

- [`tf.Variable(initializer, name, trainable)`](tensorflow/tf_api.py)

```
initializer是初始化参数，可以有tf.random_normal，tf.constant

执行：
a1 = tf.Variable(tf.random_normal(shape=[2,3], mean=0, stddev=1), name='a1')
a2 = tf.Variable(tf.constant(1), name='a2')
a3 = tf.Variable(tf.ones(shape=[2,3]), name='a3')

结果：
<tf.Variable 'a1:0' shape=(2, 3) dtype=float32_ref>
<tf.Variable 'a2:0' shape=() dtype=int32_ref>
<tf.Variable 'a3:0' shape=(2, 3) dtype=float32_ref>
```

- [`tf.get_variable(name, shape, dtype, initializer)`](tensorflow/tf_api.py)

```
执行：
init = tf.constant_initializer([5])
x = tf.get_variable('x', shape=[1], initializer=init)

结果：
<tensorflow.python.ops.init_ops.Constant object at 0x7fc3b83be588>
<tf.Variable 'x:0' shape=(1,) dtype=float32_ref>
```

### 张量操作函数

- [`tf.placeholder(shape, dtype, name)`](tensorflow/tf_api.py)

```
定义一个张量格式的数据

执行：
fingerprint_input = tf.placeholder(shape=[None, 1, 40], dtype=tf.float32, name="fingerprint_input") 

结果：
fingerprint_input : (?, 1, 40) ，网络中该层的名称为 “fingerprint_input”
```

- [`tf.concat([tensor_a,tensor_b], axis, name)`](tensorflow/tf_api.py)

```
enroll = tf.placeholder(shape=[None, 20, 40], dtype=tf.float32, name="enroll") 
verif = tf.placeholder(shape=[None, 20, 40], dtype=tf.float32, name="verif") 

执行：
fingerprint_input = tf.concat([enroll, verif], axis=0, name="fingerprint_input")

结果：
Tensor("enroll:0", shape=(?, 20, 40), dtype=float32)
Tensor("verif:0", shape=(?, 20, 40), dtype=float32)
Tensor("fingerprint_input:0", shape=(?, 20, 40), dtype=float32)

执行：
fingerprint_input = tf.concat([enroll, verif], axis=1, name="fingerprint_input")

结果：
Tensor("enroll:0", shape=(?, 20, 40), dtype=float32)
Tensor("verif:0", shape=(?, 20, 40), dtype=float32)
Tensor("fingerprint_input:0", shape=(?, 40, 40), dtype=float32)

执行：
fingerprint_input = tf.concat([enroll, verif], axis=2, name="fingerprint_input")

结果：
Tensor("enroll:0", shape=(?, 20, 40), dtype=float32)
Tensor("verif:0", shape=(?, 20, 40), dtype=float32)
Tensor("fingerprint_input:0", shape=(?, 20, 80), dtype=float32)
```

### scope如何划分命名空间

- tf.variable_scope()

```
使用tf.get_variable定义变量时:
执行：
with tf.variable_scope('scope1'):
	v1 = tf.get_variable('var', shape=[1])
	with tf.variable_scope('scope2'):
		v2 = tf.get_variable('var', shape=[1])	
v1.name, v2.name

结果：
('scope1/var:0', 'scope1/scope2/var:0')

使用tf.Variable定义变量时:
执行：
with tf.variable_scope('scope'):
	v1 = tf.Variable(1, name='var')
	v2 = tf.Variable(2, name='var')
v1.name, v2.name

结果：
('scope/var:0', 'scope/var_1:0')
```

- tf.name_scope()

```
当tf.get_variable遇上tf.name_scope，它定义的变量的最终完整名称将不受这个tf.name_scope的影响

执行：
with tf.variable_scope('v_scope'):
	with tf.name_scope('n_scope'):
		x = tf.Variable([1], name='x')
		y = tf.get_variable('x', shape=[1], dtype=tf.int32)
		z = x + y
x.name, y.name, z.name

结果：
('v_scope/n_scope/x:0', 'v_scope/x:0', 'v_scope/n_scope/add:0')
```

