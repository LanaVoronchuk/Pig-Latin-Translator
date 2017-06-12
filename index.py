print ('Welcome to Pig Latin Translator')

pyg="ma"

original=input('Enter a word:')
if len(original)>0 and original.isalpha():
    print(original)
    word=original.lower()
    first=word[0]
    new_word=word[1:0]+first+pyg
    print(original[1:]+original[0]+pyg)
else:
    print("empty")