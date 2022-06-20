#! /usr/local/bin


input_txt=$1
input_file=$2

# 打印文档input_file 中包含 input_txt 的行
sed -n "/$input_txt/p" $input_file

# 删除文档input_file 中包含 input_txt 的行
sed -i "/$input_txt/d" $input_file

# 替换文档中的某一个字符, s代表取代, -i表示直接在文档上操作, g表示全局操作,替换整个文档,不加就只替换第一行, 举例 \t 为原始字符, | 为替换字符,将文档中的 \t 全部替换为 |
sed -i "s/\t/|/gp" $input_file
