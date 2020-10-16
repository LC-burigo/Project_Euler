Palindrome_list = []
for a in range(100, 1000):
    for b in range(100, 1000):
        n = a * b
        temp = n
        rev = 0
        while n > 0:
            dig = n % 10
            rev = rev * 10 + dig
            n = n // 10
        if temp == rev:
            Palindrome_list.append(temp)

print(max(Palindrome_list))




