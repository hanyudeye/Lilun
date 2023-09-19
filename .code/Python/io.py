# 输入输出

# 读取命令行选项 sys.argv

import sys

print(sys.argv)

# if len(sys.argv) != 3:
#     sys.stdout.write("Usage: python %s inputfile outputfile \n" % sys.argv[0])
#     raise SystemExit(1)
# inputfile=sys.argv[1]
# outputfile=sys.argv[2]

# 对于更复杂的命令行处理，可以使用 optparse模块

import optparse
p=optparse.OptionParser()

# 该选项接收参数
# p.add_option("-i","--inputfile",dest="inputfile",help="input file")
# p.add_option("-d",action="store_true",dest="debug",help="debug mode")
# p.set_defaults(debug=False)

# opts,args=p.parse_args()
# inputfile=opts.inputfile
# debug=opts.debug

# print(inputfile,debug)

# 环境变量
import os
# print(os.environ['PATH'])
# print(os.environ['USER'])

# 文件
# 指定中文编码
# f=open("test.txt","r",encoding="utf-8")
# print(f.readlines())


