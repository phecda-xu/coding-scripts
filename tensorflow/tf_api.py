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

if __name__=="__main__":
    # constant_()
    # zeros_ones_()
    # concat_()
    # random_()
    # variable_()
    get_variable_()