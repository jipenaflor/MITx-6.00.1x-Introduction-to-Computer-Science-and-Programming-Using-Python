#Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
#In the case of ties, print the first substring.

tmpA = ""
tmpB = ""

for i in range(len(s)-1):
    tmpA += s[i]
    k = i
    for j in range(k+1, len(s)):
        if s[k] <= s[j]:
            tmpA += s[j]
            k += 1
        else:
            break
    if len(tmpA) > len(tmpB):
        tmpB = tmpA
    tmpA = ""
print("Longest substring in alphabetical order is: "+ tmpB)
