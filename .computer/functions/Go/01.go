package main

import (
	"fmt"
	"math"
	"time"
)

func main() {
	fmt.Println("hello" + "world")
	fmt.Println("hello world")
	fmt.Println(3 + 5)
	fmt.Println("3+5=", 3+5)
	fmt.Println(true || false)

	var name = "aming"
	fmt.Println(name)

	var e int
	fmt.Println(e)

	f := "apple"
	fmt.Println(f)

	fmt.Println(math.Sin(300))

	i := 1
	for i <= 3 {
		fmt.Println(i)
		i++
	}

	for j := 6; j < 9; j++ {
		fmt.Println(j)
	}

	if 7%2 == 0 {
		fmt.Println("7 is even")
	} else {
		fmt.Println("7 is odd")
	}

	fmt.Println(time.Now().Weekday())
	fmt.Println(time.Now().Year())

}
