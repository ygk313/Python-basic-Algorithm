def panlidrome_ds(s):

    for i in range(0, len(s)):
        if s[i].isalpha():
            if s[i].lower() == s[len(s)-i-1].lower():
                return True
            else:
                return False


print(panlidrome_ds("wow"))
