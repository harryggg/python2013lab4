with open('flintstones.txt','r') as file:
    newless=''
    nindex=[]
    for line in file.readlines():
        nindex.append(len(line))
        
        newless += line.replace('\n','')
    currentletter = newless[0]
    currentcounter = 0
    compresslist=[]
    for letter in newless:
        if letter == currentletter:
            currentcounter += 1
        else:
            compresslist += [currentcounter,currentletter]
            currentcounter = 1
            currentletter = letter


file = open('result.txt','w')
for element in compresslist:
    file.write(str(element)+' ')

file.write('\n')

for element in nindex:
    file.write(str(element))


file.close()
        
        
