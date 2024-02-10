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

func bubbleSort(arr []int) []int{
  n := len(arr)
  for i:=0; i< n; i++{
    for j:=0; j< (n - 1 - i); j++{
      if arr[j] > arr[j+1] {
        tmp := arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = tmp
      }
    }
  }
  return arr
}

func main() {
  arr := create_array(10, 10)
  fmt.Println(arr)
  arr2 := bubbleSort(arr)
  fmt.Println(arr2)
}
