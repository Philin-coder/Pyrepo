MyList = ["Самара", "Сочи", "Мурманск", "Анапа"] 
MyFile=open('output.txt', 'w', encoding='utf-8')
for element in MyList:
     MyFile.write(element)
     MyFile.write('\n')
MyFile.close()