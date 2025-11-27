def response(hey_bob):
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    hey_bob = hey_bob.strip()
    if '?' in hey_bob and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif '?' in hey_bob and hey_bob[len(hey_bob) - 1] == '?':
        return "Sure."
    else:
        return "Whatever."
