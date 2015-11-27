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

print quick([4,3,2,1])
print quick([4,3,2,1,9,3,4,7,2])
print quick([34,5,21,-23,-4,0,2,5,8])