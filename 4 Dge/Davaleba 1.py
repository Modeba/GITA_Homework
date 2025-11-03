def is_palindrome_long(word):
    l, r = 0, len(word) -1
    while l <= r:
        if word[l] != word[r]:
            return False
        l += 1
        r -= 1
    
    return True

def is_palindrome_short(word):
    return word == word[::-1]

word = input()
print(is_palindrome_short(word))
print(is_palindrome_long(word))


