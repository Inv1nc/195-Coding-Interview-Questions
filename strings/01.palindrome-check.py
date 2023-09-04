# O(n^2) time | O(n) space
'''
def isPalindrome(string):
	reverse_string = ""
	for i in reversed(string):
		reverse_string += i
	return string == reverse_string
'''

# O(n) time | O(n) space
'''
def isPalindrome(string):
	reversechar = []
	for i in reversed(string):
		reversechar.append(i)
	return string == "".join(reversechar)
'''

# O(n) time | O(n) space
'''
def isPalindrome(string,i=0):
	j = len(string) - 1 - i
	return True if i >= j else string[i] == string[i] and isPalindrome(string, i+1)
'''

# O(n) | O(1) space
def isPalindrome(string):
	i = 0
	j = len(string) - 1
	while i < j:
		if string[i] != string[j]:
			return False
		i += 1
		j -= 1
	return True

if __name__ == "__main__":
	print('Palidrome') if isPalindrome(input("Enter: ")) else print("Not Palidrome")