# Best O(nlog(n))
# Average O(nlog(n))
# Worst O(n^2)
# 
# How it works:
# 1. Pivot is chosen
# 2. All element smalller than pivot placed before and all greater placed after
# 3. This is repeated for each smaller and larger array, until each array is one item
# 4. Non-tail recursive backwards construction

def quick(array):
	pivot = array[-1]
	mini = 0
	iMini = 0
	for x in range(len(array)):
		mini = min(array[x:])
		if mini < pivot:
			iMini = array[x:].index(mini) + x
			buffer = array[x]
			array[x] = array[iMini]
			array[iMini] = buffer
		elif mini >= pivot:
			buffer = array[x]
			array[x] = pivot
			array[-1] = buffer
			pivot = buffer
	return array

def recursive_quick(array):
	if not array: 
		return []
	less_array = filter(lambda x: x <= array[0], array[1:])
	more_array = filter(lambda x: x > array[0], array[1:])
	return recursive_quick(less_array) + [array[0]] + recursive_quick(more_array)

print quick([4,3,2,1])
print quick([4,3,2,1,9,3,4,7,2])
print quick([34,5,21,-23,-4,0,2,5,8])

print recursive_quick([4,3,2,1])
print recursive_quick([4,3,2,1,9,3,4,7,2])
print recursive_quick([34,5,21,-23,-4,0,2,5,8])