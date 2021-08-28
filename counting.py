intro=input('Give me ur introduction or else : among us music in the background: ')
wordCount=1
letterCount=0

for i in intro : 
    letterCount=letterCount+1
    if(i==' '):
        wordCount=wordCount+1

print("Number of words :"+str(wordCount))
print("Number of letters :"+str(letterCount))