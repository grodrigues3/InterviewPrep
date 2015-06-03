
import random

g = range(200)

def binary_search(array, element, offset):
	if array == []:
		return -1
	mid = len(array)/2
	if element == array[mid]:
		return array[mid], offset+mid
	elif element < array[mid]:
		return binary_search(array[0:mid], element, offset)
	elif element > array[mid]:
		return binary_search(array[mid+1:], element, offset+mid+1)


print binary_search(g, 20, 0)
print binary_search(g, 32, 0)
print binary_search(g, 77, 0)
