package main

import (
	"fmt"
	"math/rand"
)


func create_array(h int, size int) []int{
  array := make([]int, size)

  for i:= 0; i < size; i++ {
    array[i] = rand.Intn(h +1)
  }

  return array
}

func partition(arr []int, lo int, hi int) int{
  pivot := arr[hi]
  i := lo -1
  for j := lo; j < hi; j++ {
    if arr[j] <= pivot{
      i++
      tmp := arr[i]
      arr[i] = arr[j]
      arr[j] = tmp
    }
  }

  tmp := arr[i+1]
  arr[i+1] = arr[hi]
  arr[hi] = tmp

  return i+1
}

func quicksort(arr []int, low, high int) {
  if low < high {
    pIdx := partition(arr, low, high)
    quicksort(arr, low, pIdx -1)
    quicksort(arr, pIdx +1, high)
  }
}


func main(){
  var arr []int= create_array(10, 100)
  fmt.Println(arr)
  quicksort(arr, 0, len(arr) - 1)
  fmt.Println("New Array: ", arr)
}
