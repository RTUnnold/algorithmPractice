#!/usr/bin/env python3


def insertionSort(arr):
	for j in range(1, len(arr)):
		key = arr[j]
		print("Key: " + str(key))
		i = j - 1
		while (i > -1) and (arr[i] > key):
			arr[i + 1] = arr[i]
			i -= 1
			print(arr)
		arr[i + 1] = key
		print(arr)
	return arr

if __name__ == '__main__':
	arr1 = [5, 2, 1 , 4, 3]
	print(arr1)
	print("Insertion sort...")
	sortedarr = insertionSort(arr1)
	print("Sorted:\n" + sortedarr)