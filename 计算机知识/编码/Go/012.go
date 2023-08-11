package main

import "os"

func main() {
	//放出错误，pinic 相当于一个断言函数
	panic("a problem")

	// os.Create("/tmp/file")

	os.Create("/home/wuming/tmpfile")
}
