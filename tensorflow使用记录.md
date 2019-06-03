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

- [`tf.Variable(initializer, name)`](tensorflow/tf_api.py)

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
enroll : (?, 20, 40)
verif  : (?, 20, 40)
fingerprint_input : (?, 20, 40)

执行：
fingerprint_input = tf.concat([enroll, verif], axis=1, name="fingerprint_input")

结果：
enroll : (?, 20, 40)
verif  : (?, 20, 40)
fingerprint_input : (?, 40, 40)


执行：
fingerprint_input = tf.concat([enroll, verif], axis=2, name="fingerprint_input")

结果：
enroll : (?, 20, 40)
verif  : (?, 20, 40)
fingerprint_input : (?, 20, 80)
```
