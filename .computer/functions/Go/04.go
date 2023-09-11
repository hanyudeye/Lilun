package main

import (
	"fmt"
	"sort"
)

func main() {
	strs := []string{"flower", "flow", "flight"}
	fmt.Println("排序前 Strings 是", strs)
	sort.Strings(strs)
	fmt.Println("排序后 Strings 是", strs)

	ints := []int{3, 2, 1}
	sort.Ints(ints)
	fmt.Println("排序后 Ints 是否正确", ints)

	s := sort.IntsAreSorted(ints)
	fmt.Println("Sorted", s)

}
