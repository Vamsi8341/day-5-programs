def findPeakUtil(arr, lowerBound, upperBound, n):
	
    # Find the middle index
	mid = lowerBound + (upperBound - lowerBound)/2
	mid = int(mid)
	
	# Compare middle element with its
	# neighbours
	if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
		(mid == n - 1 or arr[mid + 1] <= arr[mid])):
		return mid


	elif (mid > 0 and arr[mid + 1] > arr[mid]):
		return findPeakUtil(arr, (mid + 1), upperBound, n)

	else:
		return findPeakUtil(arr, lowerBound, (mid - 1), n)


arr = [1,1,1,3,2,1,2]
n = len(arr)
print("The peak point is", arr[findPeakUtil(arr, 0, n - 1, n)])
