def isPalindrome(String):
	leftIdx = 0
	rightIdx = len(String) - 1
	while leftIdx < rightIdx:
		if String[leftIdx] != String[rightIdx]:
			return False
		leftIdx += 1
		rightIdx -= 1
	return True