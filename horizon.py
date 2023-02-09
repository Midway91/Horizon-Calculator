import math
while True:
    
    scale = input("(1.) Freedom Units, (2.) Metric Units >> ")

    if scale == '1':
        
        height = input("What is the hight(ft) >> ")
        heights = int(height)

        h = math.sqrt(heights)

        horizon = 1.22459 * h

        print(horizon, "Miles")

    elif scale == '2':
        height = input("What is the height(m) >> ")
        heights = int(height)

        h = math.sqrt(heights)

        horizon = 3.56972 * h

        print(horizon, "Kilometers")
