# Finding Numbers in a Haystack
#
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
#
# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_43274.txt (There are 75 values and the sum ends with 275)
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
# Data Format
# The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. Here is a sample of the output you might see:
#
# Why should you learn to write programs? 7746
# 12 1929 8827
# Writing programs (or programming) is a very creative
# 7 and rewarding activity.  You can write programs for
# many reasons, ranging from making your living to solving
# 8837 a difficult data analysis problem to having fun to helping 128
# someone else solve a problem.  This book assumes that
# everyone needs to know how to program ...
# The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none).
# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
import re

fileSum = 0
# #If you don't open you won't be able to see content
textFile = open("Assignment.txt", "r")

for i in textFile:
    #Regex Below, simple, to find numbers in the file within each line as its own str
    s = re.findall(r"[0-9]+", i)
    #As we get hits on our findall,saved as str, we add them  using int()
    for number in s:
        fileSum += int(number)
print(fileSum)

# import re
#
# fileSum = 0
# #
# # #If you don't open you won't be able to see content
# textFile = open("sample.txt", "r")
#
# for i in textFile:
#         s = re.findall(r"[0-9]+", i)
#         print(s)
#         for number in s:
#             fileSum += int(number)
# #         # fileSum += s
# #         # print(i)
# #         # print(int(re.search(r'^[0-9]+', i).group(0)))
# #         if re.match(r"[0-9]+", i) != None:
# #             fileSum += int(re.match(r'[0-9]+', i).group(0))
# #             print(fileSum)
# #     # except:
# #     #     continue
# print(fileSum)

#Code done for an exercise done on Codewars
# import re
#
# def validate_code(code):
#     test = [1,2,3]
#     try:
#         #needed to use .group() b/c it return originally return as an object not a usable string or num
#         #also had to use proper data types using str() and int()
#         print(int(re.match(r'^[1-3][0-9]*$', str(code)).group(0)))
#     except:
#         return False
# validate_code(31233421)
