import tensorflow as tf

def constant_():
    a = tf.constant([[1, 2, 3], [4, 5, 6]], tf.int32)
    b = tf.constant(1)
    print(a)
    print(b)

def zeros_ones_():
    zeros = tf.zeros([1,2,1], dtype=tf.int32)
    ones = tf.ones_like(zeros, dtype=None, name=None)
    print(zeros)
    print(ones)

def concat_():
    enroll = tf.placeholder(shape=[None, 20, 40], dtype=tf.float32, name="enroll") 
    verif = tf.placeholder(shape=[None, 20, 40], dtype=tf.float32, name="verif") 
    fingerprint_input = tf.concat([enroll, verif], axis=0, name="fingerprint_input")

    print(enroll)
    print(verif)
    print(fingerprint_input)

def random_():
    tensor_r = tf.random_normal(shape=[2,3], mean=0, stddev=1)
    print(tensor_r.shape)
    print(tensor_r)

def variable_():
    a1 = tf.Variable(tf.random_normal(shape=[2,3], mean=0, stddev=1), name='a1')
    a2 = tf.Variable(tf.constant(1), name='a2')
    a3 = tf.Variable(tf.ones(shape=[2,3]), name='a3')
    print(a1)
    print(a2)
    print(a3)

def get_variable_():
    init = tf.constant_initializer([5])
    x = tf.get_variable('x', shape=[1], initializer=init)
    print(init)
    print(x)

def variable_scope_():
    with tf.variable_scope('scope1'):
        v1 = tf.get_variable('var', shape=[1])
        with tf.variable_scope('scope2'):
            v2 = tf.get_variable('var', shape=[1])
    print(v1.name, v2.name)
    with tf.variable_scope('scope'):
        v3 = tf.Variable(1, name='var')
        v4 = tf.Variable(2, name='var')
    print(v3.name, v4.name)

def name_scope_():
    with tf.variable_scope('v_scope'):
        with tf.name_scope('n_scope'):
            x = tf.Variable([1], name='x')
            y = tf.get_variable('x', shape=[1], dtype=tf.int32)
            z = x + y
    print(x.name, y.name, z.name)

def reshape_():
    with tf.name_scope('reshape'):
        enroll = tf.placeholder(shape=[20, 40], dtype=tf.float32, name="enroll")
        a = tf.reshape(enroll,[4,5,-1])

        b = tf.constant([1,2,3,4,5,6,7,8,9],dtype=tf.int32)
        c = tf.reshape(b,[3,3])
    print(a)
    print(c)

def reduce_sum_():
    x = tf.constant([[1, 1, 1], [1, 1, 1]])
    y1 = tf.reduce_sum(x)  
    y2 = tf.reduce_sum(x, 0)  
    y3 = tf.reduce_sum(x, 1) 
    y4 = tf.reduce_sum(x, 1, keepdims=True)
    y5 = tf.reduce_sum(x, [0, 1])
    print(x)
    print(y1)
    print(y2)
    print(y3)
    print(y4)
    print(y5)

def reduce_min_max_():
    x = tf.constant([[1, 1, 1], [1, 1, 1]])
    y1 = tf.reduce_min(x)  
    y2 = tf.reduce_min(x, 0)  
    y3 = tf.reduce_min(x, 1) 
    y4 = tf.reduce_min(x, 1, keepdims=True)
    y5 = tf.reduce_min(x, [0, 1])
    print(x)
    print(y1)
    print(y2)
    print(y3)
    print(y4)
    print(y5)

    y6 = tf.reduce_max(x)  
    y7 = tf.reduce_max(x, 0)  
    y8 = tf.reduce_max(x, 1) 
    y9 = tf.reduce_max(x, 1, keepdims=True)
    y0 = tf.reduce_max(x, [0, 1])
    print(y6)
    print(y7)
    print(y8)
    print(y9)
    print(y0)


def reduce_mean_():
    x = tf.constant([[1., 1.], [2., 2.]])
    y1 = tf.reduce_mean(x)
    y2 = tf.reduce_mean(x, 0)
    y3 = tf.reduce_mean(x, 1)
    print(x)
    print(y1)
    print(y2)
    print(y3)

def reduce_prod_():
    x = tf.constant([[1, 2, 3], [4, 5, 6]])
    y1 = tf.reduce_prod(x)  
    y2 = tf.reduce_prod(x, 0)  
    y3 = tf.reduce_prod(x, 1) 
    y4 = tf.reduce_prod(x, 1, keepdims=True)
    y5 = tf.reduce_prod(x, [0, 1])
    print(x)
    print(y1)
    print(y2)
    print(y3)
    print(y4)
    print(y5)


def global_variables_():
    a1 = tf.Variable(tf.random_normal(shape=[2,3], mean=0, stddev=1), name='a1')
    a2 = tf.Variable(tf.constant(1), name='a2')
    a3 = tf.Variable(tf.ones(shape=[2,3]), name='a3')
    a = tf.global_variables()
    print(a)

def global_variables_initializer_():
    x  = tf.placeholder(tf.float32, [None, 784])
    W = tf.Variable(tf.zeros([784,10]), name='W')
    b = tf.Variable(tf.zeros([10]), name='b') 
    y = tf.matmul(x, W) + b
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)

if __name__=="__main__":
    # constant_()
    # zeros_ones_()
    # concat_()
    # random_()
    # variable_()
    # get_variable_()
    # variable_scope_()
    # name_scope_()
    # reshape_()
    # reduce_sum_()
    # reduce_min_max_()
    # reduce_mean_()
    # reduce_prod_()
    # global_variables_()
    global_variables_initializer_()


