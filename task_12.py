txt = input("enter text: ")
res = ""

for ch in txt.lower():
    if ch != " ":
        res += ch

print("palindrome" if res == res[::-1] else "not a palindrome")
