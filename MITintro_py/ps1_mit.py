# Assume s is a string of lower case characters.
#
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:  Number of vowels: 5
s = 'hi there'
vowels = 0
for i in s:
    if i in 'aeiou':
        vowels += 1
print(vowels)

#################################################################################
# Assume s is a string of lower case characters.
#
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print: Number of times bob occurs is: 2
iterationCount = 0;
bobCount = 0
for i in s:
    if i == 'b':
        position = iterationCount
        if s[position : position + 3] == 'bob':
            bobCount += 1
    iterationCount += 1
print(bobCount)

#################################################################################
# Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#
# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

s = 'zyxwvutsrqponmlkjihgfedcba'
currentString = ''
longestStr = ''

for i in range(len(s)):
    try:
        if s[i] < s[i+1]:
            currentString += s[i]
        elif s[i] >= s[i+1] :
            # currentString += s[i]
                if len(currentString) > len(longestStr):
                    currentString += s[i]
                    longestStr = currentString
                    currentString = ''
                else:
                    #include z here?
                    currentString = ''
    except:
        if s[i-1] < s[i]:
            currentString += s[i]
            if len(currentString) > len(longestStr):
                currentString += s[i]
                longestStr = currentString
            elif len(currentString) <= len(longestStr):
                currentString = ''
        elif s[i-1] >= s[i]:
                if len(currentString) > len(longestStr):
                    currentString += s[i]
                    longestStr = currentString
                    currentString = ''
                elif len(currentString) <= len(longestStr):
                    currentString = ''
        # elif s[i-1] > s[i]:



        # if currentString[-1] >= s[i]:
        #     if len(currentString) > len(longestStr):
        #         longestStr = currentString
        #         currentString = ''
        #     elif len(currentString) <= len(longestStr):
        #         currentString = ''

print(longestStr)










#     print(i)
#     if alphabet[alphaCounter] == 'z':
#         if len(currentString) > len(longestStr):
#             longestStr = currentString
#             currentString = ''
#             continue
#         else:
#             currentString = ''
#             continue
#     elif i in alphabet[alphaCounter + 1:]:
#         currentString += i
#         print(longestStr)
#     elif i not in alphabet[alphaCounter + 1:]:
#         if len(currentString) > len(longestStr):
#             longestStr = currentString
#             currentString = ''
#             break
#         else:
#             currentString = ''
#             break
#     alphaCounter = alphabet.index(i)
# print(longestStr)



    # then go to the second char and see if it's value is larger, if yes : add it to he string, if it's less then cutt of the string and check with the largest string


    # alphaCounter = alphabet.index(i)
    # strCounter = s.index(i)
    # #not the strCounter but saved last letter
    # for n in range(0, (alphaCounter + 1)):
    #     if s[strCounter + n] < alphabet[alphaCounter + n]:
    #         currentString += s[strCounter + n]
    #     elif s[strCounter + n] >= alphabet[alphaCounter + n]:
    #         break
    # if longestStr < currentString:
    #     longestStr = currentString
    # else:
    #      continue
    #
#counter to move through alphabet
#check if the value is bigger or lessthan/equal.
#if less than



# for i in s:
    # start with a new character | find it in alphabet | check positions moving
    # forward one by one and save this new ordered string | compare all new strings
    # if: that the letter isn't in equal or less than any past indexes then keep moving forward
    #only other problem is the infinite loop
    # if i in alphabet:
    #     n = 0
    #     alphaindex = alphabet.index(i)
    #     for counter in range(0, len(s) + 1):
    #         if s[strindex : strindex + (n+1)] == None:
    #             break
    #         elif s[strindex : strindex + (n+1)] != alphabet[alphaindex : alphaindex + (n+1)]:
    #             currentString = s[strindex : strindex + (n+1)]
    #             n += 1
    #         elif s[strindex : strindex + (n+1)] != alphabet[alphaindex : alphaindex + (n+1)]:
    #             if len(currentString) > len(longestStr):
    #                 longestStr = currentString
    #             elif len(currentString) <= len(longestStr):
    #                 break
    # strindex += 1
# print(longestStr)
