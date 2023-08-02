package main

import "fmt"

func aaa(s *string) {
	s = nil
}

func bbb(s *string) {
	x := "hello"
	s = &x
}

func main() {
	var s *string
	aaa(s)
	if s == nil {
		fmt.Println("s is nil")
	} else {
		fmt.Println("%s", *s)
	}

	//发生错误
	bbb(s)
	fmt.Println("%s", *s)
}
