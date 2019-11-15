# python 使用中的问题记录

## numpy

- 使用np.array()将多个二维array组成的列表转化为三维失败

```
np.array([np.array(99,40),np.array(99,40),np.array(99,40)]) => np.array(3,99,40)
np.array([np.array(80,40),np.array(99,40),np.array(99,40)]) => np.array(3,)
原因是二维数组的维度不一致
```

## argparse

- bool 型数据在使用的时候值一直是True

```
param.py

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--trainable', default=True, help="True or False")
hp = parser.parse_args()

$ python param.py --trainable False   => hp.trainable=True

原因是
传入的是'False'字符串，这是一个非零长度的字符串, bool('False') = True； bool('') = False
这里需要改用store_true或store_false使用动作。对于default=True，使用store_false

parser.add_argument('--trainable', default=True, action='store_false', help="True or False")


如果必须用True或False在其中解析字符串，则必须明确地这样做：

def boolean_string(s):
    if s not in {'False', 'True'}:
        raise ValueError('Not a valid boolean string')
    return s == 'True'
并将其用作转换参数：

parser.add_argument('--trainable', default=True, type=boolean_string, help="True or False")
```
参考链接[1](https://cloud.tencent.com/developer/ask/188470), [2](https://docs.python.org/3/library/argparse.html#action)

## str.format()

```
'{}-{}-{}'.format(a,b,c)            => 'a-b-c'
'{1}-{0}-{1}岁'.format('a','b')     => 'b-a-b'
'{:.4f}'.format(0.4000569789)       => '0.4001'
'{name}{age}岁'.format(age=22,name='jc') => 'jc22岁'
```
