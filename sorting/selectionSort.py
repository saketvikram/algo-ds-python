def selectionSort(array):
	leftpointer = 0
	array_len = len(array) - 1

	while leftpointer < array_len:
        minpointer = leftpointer
        
        for index in range(leftpointer+1, array_len+1):
        	if array[index] < array[minpointer]: 
  				minpointer = index
				
		swapElements(array, leftpointer, minpointer)
		leftpointer += 1

	return array

def swapElements(array, i, j):
	array[i], array[j] = array[j], array[i]
