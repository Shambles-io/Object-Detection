

    # https://www.youtube.com/watch?v=T-0lZWYWE9Y&list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn&index=7

    #Template (object) Detection

import numpy as np
import cv2

img = cv2.resize(cv2.imread('soccer_practice.jpg', 0), (0, 0), fx=0.75, fy=0.75)

template = cv2.resize(cv2.imread('ball.png', 0), (0, 0), fx=0.75, fy=0.75)
template = cv2.resize(cv2.imread('shoe.png', 0), (0, 0), fx=0.75, fy=0.75)

height, width = template.shape

    #All/Different methods for doing template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, 
            cv2.TM_CCORR_NORMED, cv2. TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    #Here, we are going to loop through all of the different methods to see which one 
    #gives us the best template mathing result
for method in methods:
    img2 = img.copy()

        #matchTemplate takes the template image and moves it sround out source image 
        #to see if/where there could be a match
        #Returns a 2-D array that tells us roughly how accurate of a mathc there is in each
        #region of our image (H - h + 1, W - w + 1)
    result = cv2.matchTemplate(img2, template, method)

        #returns the minimum and maximum values and respective locations within result array
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # print(min_loc, max_loc)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + width, location[1] + height)

    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
