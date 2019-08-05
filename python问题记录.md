# python 使用中的问题记录

## numpy

- 使用np.array()将多个二维array组成的列表转化为三维失败

```
np.array([np.array(99,40),np.array(99,40),np.array(99,40)]) => np.array(3,99,40)
np.array([np.array(80,40),np.array(99,40),np.array(99,40)]) => np.array(3,)
原因是二维数组的维度不一致
```
