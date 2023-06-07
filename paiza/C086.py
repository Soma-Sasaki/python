S = list(input())

vowel = 'aeiouAEIOU'
name = ''.join(s for s in S if s not in vowel)
print(name)
