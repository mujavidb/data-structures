def insertion(array):
	for i in range(len(array)):
		element = array[i]
		j = i
		while j > 0 and array[j-1] > element:
			array[j] = array[j - 1]
			j = j - 1
		array[j] = element
	return array

print insertion([4,3,2,1])
