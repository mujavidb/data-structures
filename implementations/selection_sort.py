def selection(array):
	for i in range(len(array)):
		mini = min(array[i:])
		min_index = array[i:].index(mini)
		array[i + min_index] = array[i]
		array[i] = mini
	return array

print selection([4,3,2,1])