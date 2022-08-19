#Day 2 Part 1
def calcWrappingPaper(): #Calculate wrapping paper needed for presents
    wrappingPaper = 0
    with open('Day2_Input.txt') as fp:
        for line in fp:
            clearline = line.strip() #strip \n (new line)

            numArr = list(map(int, clearline.split('x'))) #convert string of nums to int of nums
            numArr.sort() #sort function builtin python
            
            wrappingPaper += (2 * numArr[0] * numArr[1]) + (2 * numArr[1] * numArr[2]) + (2 * numArr[0] * numArr[2]) + (numArr[0] * numArr[1] )
            # numArr[0] - l
            # numArr[1] - w
            # numArr[2] - h
            #2*lw + 2*lh + 2wh + smallest area

    return wrappingPaper #1606483 is the result.    

#Day 2 Part 2
def calcRibbon(): #Calculate ribbon need for presents
    ribbon = 0
    with open('Day2_Input.txt') as fp:
        for line in fp:
            clearline = line.strip() #strip \n (new line)

            numArr = list(map(int, clearline.split('x'))) #convert string of nums to int of nums
            numArr.sort() #sort function builtin python
            ribbon += (2 * numArr[0] + 2 * numArr[1]) + (numArr[0] * numArr[1] * numArr[2])
            
            #print(ribbon)
    return ribbon

print(calcWrappingPaper())
print(calcRibbon())