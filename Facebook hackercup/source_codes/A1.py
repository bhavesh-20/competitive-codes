for _t in range(int(input())):
    s= input()
    vowels = ["A", "E", "I", "O", "U"]
    d = {}
    max_vowel, max_consonant = 0, 0
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        if i in vowels:
            max_vowel = max(max_vowel, d[i])
        else:
            max_consonant = max(max_consonant, d[i])
    number_of_vowels = 0
    for i in vowels:
        if i in d:
            number_of_vowels += d[i]
    number_of_consonant = len(s) - number_of_vowels
    if number_of_vowels == 0:
        ans = min(len(s), (number_of_consonant - max_consonant) * 2)
    elif number_of_consonant == 0:
        ans = min(len(s), (number_of_vowels - max_vowel) * 2)
    else:
        case_1, case_2 = (
            number_of_consonant + (number_of_vowels - max_vowel)*2,
            number_of_vowels + (number_of_consonant - max_consonant)*2
        )
        ans = min(case_1, case_2)
    print(f"Case #{_t+1}: {ans}")
