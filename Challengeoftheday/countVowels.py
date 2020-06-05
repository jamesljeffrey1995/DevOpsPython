

def countVowels(word):
	vowels = "aeiou"
	count = 0
	for i in range(len(word)):
		for e in range(len(vowels)):
			if vowels[e] == word[i].lower():
				count += 1
	return count

