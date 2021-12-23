import numpy as np
import tensorflow as tf


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
    new_input = tf.stack(pad_list, axis=2)
    out_put = tf.reshape(new_input, [shape[0], out_shape[1], out_shape[2], -1])
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


def conv_bn_relu(inputs, out_channels, kernel_size, stride, is_training, padding='SAME',
                 use_norm=True, use_act=True, scope='conv', skip_input=None):
    """
    Conv layer with batch_norm and relu.
    :param inputs:  input tensor with shape as [batch, height, width, in_channels]
    :param out_channels: int
    :param kernel_size: tuple as (3,3)
    :param stride:  tuple as (1,1)
    :param is_training: True or False
    :param padding: "SAME" or "VALID"
    :param use_norm: True or False
    :param use_act: True or False
    :param scope: layer name
    :param skip_input: skip connection or resdual connection
    :return: tensor with shape as [batch, height, width, in_channels]
    """
    if padding.lower() == "same":
        conv = tf.layers.conv2d(inputs, out_channels, kernel_size, stride, padding, name=scope)
    elif padding.lower() == "valid":
        h_left = int((kernel_size[0] - 1) / 2)
        h_right = kernel_size[0] - 1 - h_left
        w_left = int((kernel_size[1] - 1) / 2)
        w_right = kernel_size[1] - 1 - w_left
        inputs = tf.pad(inputs, tf.constant([[0, 0], [h_left, h_right], [w_left, w_right], [0, 0]]), "CONSTANT")
        conv = tf.layers.conv2d(inputs, out_channels, kernel_size, stride, padding, name=scope)
    else:
        raise ValueError("Wrong input of padding: {}. Should be SAME or VALID!")
    if use_norm:
        conv = tf.layers.batch_normalization(conv, training=is_training, name=scope + '/batch_norm')
    if use_act:
        conv = tf.nn.relu(conv)
    if skip_input is not None:
        conv = conv + skip_input
    return conv



def involution_layer(input_x, in_channels, kernel_size, strides, padding, group=1, ratio=4, is_training=True, scope='involution'):
    shape = tf.shape(input_x)
    #
    reduce_channels = int(in_channels / ratio)
    span_channels = group * kernel_size[0] * kernel_size[1]
    # reduce conv bn relu
    conv_1 = tf.layers.conv2d(input_x, reduce_channels, (1, 1), name=scope + '/reduce')
    conv_1 = tf.layers.batch_normalization(conv_1, training=is_training, name=scope + '/reduce/batch_norm')
    conv_1 = tf.nn.relu(conv_1)
    #
    weight = tf.layers.conv2d(conv_1, span_channels, (1, 1), name=scope + '/span')
    #
    weight = tf.reshape(weight, [shape[0], shape[1], shape[2], group, 1, kernel_size[0] * kernel_size[1]])
    weight = tf.concat([weight] * int(in_channels / group), axis=4)
    #
    output_1 = unfold(input_x, ksizes=kernel_size, strides=stride, padding=padding)
    output_1 = tf.reshape(output_1, [shape[0],
                                     shape[1],
                                     shape[2],
                                     group,
                                     int(in_channels / group),
                                     kernel_size[0] * kernel_size[1]])

    output_2 = tf.reshape(tf.multiply(output_1, weight), [shape[0], shape[1] * shape[2], in_channels,
                                                          kernel_size[0] * kernel_size[1]])
    output_2 = tf.reduce_sum(output_2, axis=3)
    output_2 = tf.reshape(output_2, [shape[0], shape[1], shape[2], in_channels])
    return output_2


if __name__ == "__main__":
    input_x = tf.placeholder(dtype=tf.float32, shape=[None, None, 257, 32])
    in_channels = 1
    ratio = 1

    scope = "conv"
    kernel_size = [3,3]
    padding=[1, 1]
    strides=[1, 1]
    group = 1

    x = np.random.random((2, 10, 257, 32))

    unfold_out_1 = unfold(input_x, ksizes=kernel_size, strides=stride, padding=padding)
    unfold_out_2 = unfold_2(input_x, inchannels, kernel_size, strides)
    involution_out = involution_layer(input_x, in_channels, kernel_size, strides, padding, group=group, ratio=ratio, is_training=True, scope='involution')

    sess = tf.Session()
    sess.as_default()
    sess.run(tf.global_variables_initializer())

    feed_dict = {input_x: x}

    out_1, out_2, invo_out = sess.run([unfold_out_1, unfold_out_2, involution_out], feed_dict=feed_dict)

    print(out_1.shape)
    print(out_2.shape)
    print(invo_out.shape)

    total_params = tf.trainable_variables()
    for i in total_params:
        print('{} layer parameter shape: {} | numbers: | {}'.format(i.name, i.shape,
                                                                    np.prod(tf.shape(i.value()).eval(session=sess))))
    num_params = sum(map(lambda t: np.prod(tf.shape(t.value()).eval(session=sess)), total_params))
    print('\nTotal number of Parameters: {}\n'.format(num_params))


