import os
import mmap

filepath = input("Please enter your filepath: ")

wordToReplace = input("Word to replace: ")

#File is opened in read mode
f = open(filepath, "r+")
data = f.read()

wordToReplaceWith = input("Word to replace with: ")

#The words which will be replaced in the textfile are saved into a variable, the file is closed
data = data.replace(wordToReplace, wordToReplaceWith)
f.close

#The file is opened in write mode, the variable is written into the file, the file is closed
f = open(filepath, "w+")
f.write(data)
f.close

if (wordToReplace == wordToReplaceWith):
    print("The two words are the same, please try again")
else:
    print("Every instance of " + wordToReplace + " has been replaced with " + wordToReplaceWith)
