import tensorflow as tf

def get_default_graph_():
    print(tf.get_default_graph())
    graph_restore = tf.get_default_graph()
    print(graph_restore)

def default_graph_():
    g1=tf.Graph()
    print(g1)
    with g1.as_default():
        print(g1)
        v=tf.get_variable("v",[1],initializer=tf.zeros_initializer(dtype=tf.float32))

    g2=tf.Graph()
    with g2.as_default():
        print(g2)
        v=tf.get_variable("v",[1],initializer=tf.ones_initializer(dtype=tf.float32))

    with tf.Session(graph=g1) as sess:
        tf.global_variables_initializer().run()
        with tf.variable_scope("",reuse=True):  # 当reuse=True时，tf.get_variable只能获取指定命名空间内的已创建的变量
            print(sess.run(tf.get_variable("v")))

    with tf.Session(graph=g2) as sess:
        tf.global_variables_initializer().run()
        with tf.variable_scope("",reuse=True):  # 当reuse=True时，tf.get_variable只能获取指定命名空间内的已创建的变量
            print(sess.run(tf.get_variable("v")))

def reset_default_graph_():
    # tf.reset_default_graph() # 利用这个可清空defualt graph以及nodes 
    with tf.variable_scope('Space_a'): 
        a = tf.constant([1,2,3]) 
    with tf.variable_scope('Space_b'): 
        b = tf.constant([4,5,6]) 
    with tf.variable_scope('Space_c'): 
        c = a + b 
    d = a + b 
    with tf.Session()as sess: 
        print(a) 
        print(b) 
        print(c) 
        print(d) 
        print(sess.run(c)) 
        print(sess.run(d))


if __name__=="__main__":
    get_default_graph_()
    # default_graph_()
    # reset_default_graph_()


