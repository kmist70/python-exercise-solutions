def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = text.split()
    new_words = []
    for word in words:
        if word[:2] == 'xr' or word[:2] == 'yt' or word[0] in vowels:
            new_words.append(word + "ay")
            continue
        while word[0] not in vowels and word[0] != 'y':
            if word[:2] == "qu":
                word = word[2:] + word[0:2]
                break
            word = word[1:] + word[0]
        if word[0] == 'y' and word[1] in vowels:
            new_words.append(word[1:] + word[0] + "ay")
        else:
            new_words.append(word + "ay")

    return ' '.join(new_words)
