#! /usr/local/bin


# 批量修改文件名, f 表示文件, d 表示文件夹, s 表示取代, 讲 文件名中的 .wav 替换成 _0.wav
find -type f |grep ".wav" | xargs rename 's/.wav/_0.wav/'
