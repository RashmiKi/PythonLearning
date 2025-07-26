word1 = input("Enter a word: ")
word2 = input("Enter second word: ")

word1.strip()
word2.strip()
if word1[-1] == word2[0]:
    print("Anagrams")
else:
    print("Not Anagrams String")