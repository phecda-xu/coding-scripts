import numpy as np
import tensorflow as tf

input_x = tf.placeholder(dtype=tf.float32, shape=[None, None, 257, 10])


def unfold(input_x, ksizes, strides, padding):
    """
    :param input_x: N*H*W*C
    :param ksizes:
    :param strides: 目前只支持 stride=1
    :param padding:
    :return:
    """
    if type(ksizes) is int:
        k_h = ksizes
        k_w = ksizes
    elif len(ksizes) == 2:
        k_h = ksizes[0]
        k_w = ksizes[1]
    elif len(ksizes) == 4:
        k_h = ksizes[1]
        k_w = ksizes[2]
    else:
        raise ValueError("'ksizes' should be 'int' or 'list' with length as in [1, 2, 4].")

    if type(strides) is int:
        stride_h = strides
        stride_w = strides
    elif len(strides) == 2:
        stride_h = strides[0]
        stride_w = strides[1]
    elif len(strides) == 4:
        stride_h = strides[1]
        stride_w = strides[2]
    else:
        raise ValueError("'ksizes' should be 'int' or 'list' with length as in [1, 2, 4].")

    shape = tf.shape(input_x)
    if type(padding) is int:
        pad_h = padding
        pad_w = padding
    elif len(padding) == 2:
        pad_h = padding[0]
        pad_w = padding[1]
    elif len(padding) == 4:
        pad_h = padding[1]
        pad_w = padding[2]
    else:
        raise ValueError("'ksizes' should be 'int' or 'list' with length as in [1, 2, 4].")

    pad_top = pad_h // 2
    pad_down = pad_h - pad_top

    pad_left = pad_w // 2
    pad_right = pad_w - pad_left

    pad_x = tf.pad(input_x,
                   tf.constant([[0, 0],
                                [pad_top, pad_down],
                                [pad_left, pad_right], [0, 0]]), "CONSTANT")
    out_shape = [shape[0],
                 shape[1],
                 shape[2],
                 shape[3]]
    pad_list = []
    for i in range(k_h):
        for j in range(k_w):
            pad_tensor = tf.slice(pad_x,
                                  [0, i, j, 0],
                                  out_shape)
            pad_tensor = tf.reshape(pad_tensor, [shape[0], -1, shape[3]])
            pad_list.append(pad_tensor)
    new_input = tf.stack(pad_list, axis=1)
    out_put = tf.reshape(tf.transpose(new_input, [0, 2, 1, 3]), [shape[0], out_shape[1], out_shape[2], -1])
    return out_put


def unfold_2(input_x, inchannels, kernel_size, strides):
    shape = tf.shape(input_x)
    filters = np.zeros([kernel_size[0], kernel_size[1], kernel_size[0] * kernel_size[1]])
    n = 0
    for i in range(kernel_size[0]):
        for j in range(kernel_size[1]):
            filters[i, j, n] = 1
            n += 1
    filters = np.expand_dims(filters, 2)
    input_list = tf.split(input_x, num_or_size_splits=inchannels, axis=3)
    output_list = []
    scope_num = 0
    for input_channel in input_list:
        scope_num += 1
        output_list.append(tf.nn.conv2d(input_channel,
                                        filter=filters,
                                        strides=strides,
                                        padding='SAME',
                                        name="unfold_{}".format(scope_num)))
    output = tf.stack(output_list, axis=-1)
    output = tf.reshape(output, [shape[0], shape[1], shape[2], -1])
    return output



shape = tf.shape(input_x)

reduce_channels = 1

scope = "conv"
kernel_size = [3,3]
strides=[1, 1]
group = 1
span_channels = group * kernel_size[0] * kernel_size[1]

conv_1 = tf.layers.conv2d(input_x, reduce_channels, (1, 1), name=scope + '_1')
conv_1 = tf.layers.batch_normalization(conv_1, training=True, name=scope + '/batch_norm')
conv_1 = tf.nn.relu(conv_1)
#
weight = tf.layers.conv2d(conv_1, span_channels, (1, 1), name=scope + '_2')
#
weight = tf.reshape(weight, [shape[0], group, 1, kernel_size[0] * kernel_size[1], shape[1], shape[2]])

output_1 = unfold(input_x, ksizes=kernel_size, strides=[1, 1, 1, 1], padding=[2, 2])

# output_1 = tf.reshape(output_1, [shape[0],
#                                  group,
#                                  shape[3] // group,
#                                  kernel_size[0] * kernel_size[1],
#                                  shape[1],
#                                  shape[2]])
# output_involution = tf.reduce_sum(output_1 * weight, axis=3)
# output_involution = tf.transpose(tf.reshape(output_involution, [shape[0], -1,  shape[1], shape[2]]), [0, 2, 3, 1])

output_2 = unfold_2(input_x, 10, kernel_size, strides=strides)


sess = tf.Session()
sess.as_default()
sess.run(tf.global_variables_initializer())

x = np.random.random((2, 10, 257, 10))

feed_dict = {input_x: x}

# out_0, out_1, out_2 = sess.run([weight, output_1, output_2], feed_dict=feed_dict)


out_1, out_2 = sess.run([output_1, output_2], feed_dict=feed_dict)

print(out_1.shape)
print(out_2.shape)
