#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s

i = 0
ctr = 0
while i+2 != len(s):
    if s[i] == "b" and s[i+1] == "o" and s[i+2] == "b":
        ctr += 1
    i +=1
print("Number of time bob occurs is: " + str(ctr))
