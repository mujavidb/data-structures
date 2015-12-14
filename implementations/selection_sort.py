# Best O(n^2)
# Average O(n^2)
# Worst O(n^2)
# 
# How it works:
# 1. Array is divided into sorted and unsorted parts
# 2. Minimum of unsorted is appended to end of sorted
# 3. Repeat

def selection(array):
	for i in range(len(array)):
		mini = min(array[i:])
		min_index = array[i:].index(mini)
		array[i + min_index] = array[i]
		array[i] = mini
	return array

print selection([4,3,2,1])