package main

import "fmt"

func ping(pings chan<- string, msg string) {
	pings <- msg
}

func main() {
	// make创建贴片
	pings := make(chan string, 1)
	ping(pings, "hello")

	fmt.Println(<-pings)
}
