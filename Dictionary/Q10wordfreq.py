'''
Q.10
Word Frequency
Write a Python program to take a sentence from the user and store each word and its frequency in a 
dictionary. Display the resulting dictionary.'''
sentence=input("Enter Sentence")
word=sentence.split()
freq={}
for w in word:
    if w in freq:
        freq[w]=freq[w]+1
    else:
        freq[w]=1
        
for k,v in freq.items():
    print(k,"\t",v)
    