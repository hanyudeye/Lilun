
## gcc 编译

### 工作流程

- 1. 预处理 -E
 xxx.c -> xxx.i

 命令为 gcc -E hello.c hello.i
gcc默认的编译工具 cpp

- 2. 编译 -S
xxx.i -> xxx.s

gcc -S hello.i hello.s
gcc默认工具为gcc
gcc默认工具为as

- 3. 汇编 -c
xxx.s -> xxx.o

gcc -c hello.s -o hello.o

- 4. 链接 
xxx.o -> xxx
gcc hello.o -o hello
gcc默认工具为ld


- 5. 调试
-g 使用gdb调试的时候必须加的参数