#!/usr/bin/env python3

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	print("Left: " + str(l) + ", Middle: " + str(m) + ", Right: " + str(r))

	if l == m and m == r:
		return arr 

	larr = arr[l:l + n1] + ['end']
	rarr = arr[m + 1: m + 1 + n2] + ['end']

	print("Left array: " + str(larr))
	print("Right array: " + str(rarr))

	i = j = 0
	for k in range(l, r+1):
		if (rarr[j] == 'end') or (larr[i] != 'end' and larr[i] <= rarr[j]):
			arr[k] = larr[i]
			i += 1
		else:
			arr[k] = rarr[j]
			j += 1
		print("i, j: " + str((i, j)))
		print("K: " + str(k) + ", arr[K]: " + str(arr[k]))

	print("Mergestep: " + str(arr))
	return arr

def mergeSort(arr, l, r):
	if l < r:
		m = (l + r) // 2
		arr = mergeSort(arr, l, m)
		arr = mergeSort(arr, m+1, r)
		arr = merge(arr, l, m, r)
	return arr

if __name__=='__main__':
	arr = [7, 6, 2, 4, 1, 3, 5]
	print(arr)
	print("Mergesort...")
	sortedarr = mergeSort(arr, 0, len(arr) - 1)
	print("Sorted\n" + str(sortedarr))