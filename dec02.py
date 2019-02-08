file = open("dec02.txt", "r")

"""
total_doubles = 0
total_triples = 0

for line in file:
    doubles = 0
    triples = 0
    for i in range(len(line) - 1):
        count = line.count(line[i])
        if  count == 2:
            doubles = 1
        if count == 3:
            triples = 1
    total_doubles += doubles
    total_triples += triples

print (total_doubles*total_triples)

"""
list = []

for line in file:
    temp = []
    for i in range (len(line) - 1):
        temp.append(line[i])
    list.append(temp)

list = sorted(list)
#print(list)

print (len (list[0]))

for i in range(len(list)):
    #print (list[i])
    for j in range(i+1, len(list)):
        #print (list[j])
        #print ("---------------")
        counter = 0
        answer = ""
        for k in range(len (list[i])):
            character = list[i][k]
            if list[i][k] == list[j][k]:
                #print("match")
                counter += 1
                answer = answer + character

        if counter == 25:
            print("ANSWER:")
            print (list[i], list[j])
            print (answer)


file.close()
