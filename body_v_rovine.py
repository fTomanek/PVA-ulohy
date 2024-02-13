#vypsani pozitivniho vysledku
def positive_output():
    print("Body lezi na jedne primce.")
    

#vypsani negativniho vysledku
def negative_output():
    print("Body nelezi na jedne primce.")
    


#input format
points = []
def coordinates_format(inputs):

    temp = inputs[-1].split()
    points.append(temp)
    
    return(points)


#input konrola
def coordinates_check(points):

    try:
        a = float(points[-1][0])
        a = float(points[-1][1])

        if len(points[-1]) != 2:
            exit()
    except:
        print("Nespravny vstup.")
        exit()


#kontrola zda nejsou 2 body stejne
def same_cords_check():
    if points[0] == points[1]:
        print("Nektere body splyvaji.")
        exit()
    elif points[1] == points[2]:
        print("Nektere body splyvaji.")
        exit()
    elif points[0] == points[2]:
        print("Nektere body splyvaji.")
        exit()

  

#vypocet prostredniho bodu
def midle_point_calc(sorted_points):
    side_names = ["A", "B", "C"]
    midle_point = sorted_points[1]
    for i in range(3):
        if midle_point == points[i]:
            print("Prostredni je bod " + side_names[i] + ".")

#najit prostredni bod
def midle_point():
    sorted_points = sorted(points, key=lambda x: float(x[0]))
    midle_point_calc(sorted_points)

#najit prostredni bod pro stejna x
def same_x_midle_point():
    sorted_points = sorted(points, key=lambda x: int(x[1]))
    midle_point_calc(sorted_points)



#nulove souradnice
def same_x_check(points):
    
    same_x = 0
    for i in range(2):
        if points[i][0] == points[i+1][0]:
            same_x += 1
    
    if same_x == 2:
        positive_output()
        same_x_midle_point()
        exit()

    if same_x == 1:
        negative_output()
        exit()
        


#input
inputs = []

input_1 = input("Napis souradnice prvniho bodu: ")
inputs.append(input_1)
points = coordinates_format(inputs)
coordinates_check(points)

input_2 = input("Napis souradnice druheho bodu: ")
inputs.append(input_2)
points = coordinates_format(inputs)
coordinates_check(points)

input_3 = input("Napis souradnice tretiho bodu: ")
inputs.append(input_3)
points = coordinates_format(inputs)
coordinates_check(points)

print("")

same_cords_check()
same_x_check(points)



#spocitat sklopeni
slopes = []
for i in range(2):
    x1 = float(points[i][0])
    x2 = float(points[i+1][0])
    y1 = float(points[i][1])
    y2 = float(points[i+1][1])

    slope = abs(y2 - y1) / abs(x2 - x1)
    slopes.append(round(slope, 10))
    


#porovnat sklopeni
if slopes[0] == slopes[1]:
    positive_output()
    midle_point()
else:
    negative_output()
    