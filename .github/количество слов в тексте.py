import re
 
text = input('Text: ')
word = input('Word: ')
print(len(re.findall(fr'\b{word}\b', text)))