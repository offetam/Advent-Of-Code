#Day 3 Part 1
#Santa is travelling. His untrustworthy elf is giving him directions. Count how many houses Santa travels to at elast once
def santaTravelling(): 
    housesEntered = 1 #counter for houses entered
    travelArr = [[0,0]] #start off with origin pos
    rowIterator = 0
    colIterator = 0
    pos = rowIterator, colIterator
    with open('input.txt') as fp:
        for line in fp:
            line = line.strip()
            for direction in line: 
                if(direction == '>'): #right
                    rowIterator += 1
                elif(direction == '<'): #left
                    rowIterator -= 1
                elif(direction == '^'): #up
                    colIterator += 1
                else: #down
                    colIterator -= 1
                    #go down
                #print("X:", rowIterator, "Y:", colIterator)
                #print(pos)
                if([rowIterator,colIterator] not in travelArr):
                    travelArr.append([rowIterator, colIterator])
                    housesEntered += 1
                    #print(travelArr)
                    #print(pos)
            #print(line)
    #print(travelArr)
    return housesEntered

#Day 3 Part 2
def duoSantas(): #Santa enlisted the help of Robosanta to deliever gifts! Slightly modified as Santa and RoboSanta takes turns.
    housesEntered = 1 #counter for houses entered

    #travelArr = [] #start off with empty arr
    travelArr = [[0,0]] #start off with arr containing starting (origin) pos
    rowIteratorSanta = 0
    colIteratorSanta = 0

    rowIteratorRoboSanta = 0
    colIteratorRoboSanta = 0

    with open('input.txt') as fp:
        for line in fp:
            line = line.strip() #strip any new lines to prevent issues
            for i in range(0, len(line)): #Iteration
                if(i % 2 == 0):#Santa's Turn                      
                    if(line[i] == '>'): #right
                        rowIteratorSanta += 1
                    elif(line[i] == '<'): #left
                        rowIteratorSanta -= 1
                    elif(line[i] == '^'): #up
                        colIteratorSanta += 1
                    else: #down
                        colIteratorSanta -= 1
                    if([rowIteratorSanta,colIteratorSanta] not in travelArr):
                        travelArr.append([rowIteratorSanta, colIteratorSanta])
                        housesEntered += 1
                    #print(f"Current Direction, {line[i]}, [{rowIteratorSanta, colIteratorSanta}], - Santa, {housesEntered}")     
                else: #RoboSanta's turn
                    if(line[i] == '>'): #right
                        rowIteratorRoboSanta += 1
                    elif(line[i] == '<'): #left
                        rowIteratorRoboSanta -= 1
                    elif(line[i] == '^'): #up
                        colIteratorRoboSanta += 1
                    else: #down
                        colIteratorRoboSanta -= 1
                    if([rowIteratorRoboSanta,colIteratorRoboSanta] not in travelArr):
                        travelArr.append([rowIteratorRoboSanta, colIteratorRoboSanta])
                        housesEntered += 1   
                    #print(f"Current Direction, {line[i]}, [{rowIteratorRoboSanta, colIteratorRoboSanta}], - RoboSanta, {housesEntered}")          
    return housesEntered

print(santaTravelling()) 
print(duoSantas())