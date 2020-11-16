introString=input("Enter your introduction:")
characterCount=0
wordCount=1
for character in introString:
    characterCount=characterCount + 1
    if(character == ' '):
         wordCount=wordCount+1

print("Number of words in the string:")
print(wordCount)
print("Number of characters in the string:")
print(characterCount)