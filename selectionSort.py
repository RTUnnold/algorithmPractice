#!/usr/bin/env python3

def selectionSort(arr):
	for i in range(len(arr) - 1):
		k = -1
		minval = arr[i]
		for j in range(i+1, len(arr)):
			if arr[j] < minval:
				k = j
				minval = arr[j]
		if k != -1:
			print("Swap: " + str(arr[i]) + " and " + str(arr[k]))
			swap = arr[k]
			arr[k] = arr[i]
			arr[i] = swap
		else:
			print("No swap")
		print(arr)
	return arr

if __name__=='__main__':
	arr1 = [7,2,3,1,6,5,4]
	print(arr1)
	print("Selection sort...")
	sortedarr = selectionSort(arr1)
	print("Sorted:\n" + sortedarr)
