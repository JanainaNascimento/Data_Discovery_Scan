import re

with open('Projeto TCC.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()

    print(content) #The entire file
    
    for line in content:
        if re.search('de', line):
            print(line, re.findall('de', line))

'''find = re.compile(r'de')
print(find.search(line))
print(find.findall(line))
print(find.sub('of', line))'''