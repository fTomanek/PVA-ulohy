import math

def distances(x1, y1, x2, y2):
    dis = math.sqrt((x1-x2)**2 + (y1 - y2)**2)
    return dis




def user_input():
    planes = []

    while True:
        user_input = input("Enter data of a plane (or press Enter to stop): ")
    
        if user_input == "":
            break
    
        split1 = user_input.split(": ")
        if len(split1) != 2:
            print("Input error")
            continue
        
        cords, name= split1
        cordinates = cords.split(",")
    
        try:
            x = float(cordinates[0])
            y = float(cordinates[1])
        except ValueError:
            print("Input error")
            continue

        if " " in name:
            print("Input error")
            continue

        if len(name) > 199:
            print("Input error")
            continue
        if name == "":
            print("Input error")   


        planes.append([x, y, name])

        if len(planes) == 1:
            continue
    
    return planes


def compare_distances():
    plane_distances = []
    for i in range(len(planes)-1):
        for j in range(i+1, len(planes)):
            distance = distances(planes[i][0], planes[i][1], planes[j][0], planes[j][1])
            plane_distances.append([distance, planes[i][2], planes[j][2]])
    return plane_distances

#Main
planes = user_input()

if len(planes) <= 1:
    print("Not enough planes.")
    exit()

plane_distances = compare_distances()


plane_distances.sort(key=lambda x: x[0])

print(" ")                        


distance = plane_distances[0][0]



print("The distance is: " + str(distance))

pairs = 0
for i in range(len(plane_distances)):
    print(plane_distances[i][1] + " - " + plane_distances[i][2])
    pairs += 1
    try:
        if plane_distances[i][0] != plane_distances[i+1][0]:
            break
    except:
        break
    
print("There are " + str(pairs) + " pairs of planes.")