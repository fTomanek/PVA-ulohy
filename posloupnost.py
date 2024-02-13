def error():
    print("Neco se nepovedlo")
    exit()
    

def User_Input():
    user_in = input("Please type in the numbers: ")

    numbers = user_in.split(' ')
    


    #ma 2 az 2000 znaku?
    if (len(numbers) < 2) or (len(numbers) > 2000):
        print("bomboclat")
        error()
    
    #je cislo?
    try:
        for each in numbers:
            int(each)
    except:
        error()
    

    return(numbers)


#parse na list
user_input = User_Input()
input = [i for i in user_input]

#najit vsechny intervaly
list = []
for i in range(len(input)):
    for j in range(i, len(input)):

        try:
            if i == j:
                temp = int(input[i]) + int(input[j+1])
                list.append(temp)

            else:
                temp = int(list[-1]) + int(input[j+1])
                list.append(temp)

        except:
            x = 1 #nevyznamna hodnota


#najit stejne dvojice
res = 0
for i in range(len(list)):
    for j in range(i, len(list)):
        
        try:
            if list[i] == list[j+1]:
                res += 1

        except:
            x = 1


#print result
print("There are " + str(res) + " same pairs.")
