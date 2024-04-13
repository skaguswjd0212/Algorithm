vowel = ['a', 'e', 'i', 'o', 'u']
sentence = input().lower()

while (sentence != '#'):
    sum = 0
    for i in range(len(sentence)):
        if sentence[i] in vowel:
            sum+=1
    print(sum)
    sentence = input().lower()