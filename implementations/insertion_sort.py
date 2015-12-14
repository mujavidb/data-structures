# Best O(n)
# Average O(n^2)
# Worst O(n^2)
# 
# How it works:
# 1. Array is divided into sorted and unsorted parts
# 2. First item in unsorted is compared right to left to numbers in sorted
# 3. If it is greater than the current number, it is inserted after it
# 4. Repeat from step 2 for all items in unsorted

def insertion(array):
	for i in range(len(array)):
		element = array[i]
		j = i
		while j > 0 and array[j-1] > element:
			array[j] = array[j - 1]
			j -= 1
		array[j] = element
	return array

def recursive_insertion(array,i=1):
  if i >= len(array):
    return array
  if array[i-1] > array[i]: 
    temp = array[i]
    for a in range(0, i): 
      if temp < array[a]:
        array.insert(a,temp)
        del array[i+1]
        break
  return recursive_insertion(array, i+1)

print insertion([4,3,2,1])