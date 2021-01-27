def palin(text):
    if len(text)<=1:
        print("Palindrome")
    else:
        if text[0]==text[-1]:
            palin(text[1:-1])
        else:
            print("Not a Palindrome")

palin("Mysore")
