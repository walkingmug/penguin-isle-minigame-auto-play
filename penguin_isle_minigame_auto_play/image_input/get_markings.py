import cv2


click_counter = 0
click_coords = {'X1': None, 'Y1': None, 'X2': None, 'Y2': None}


def click_event(event, x, y, flags, params):
    global click_counter
    global click_coords

    # Get click coordinates and stop after two clicks
    if event == cv2.EVENT_LBUTTONDOWN:      
        click_counter += 1
        if click_counter == 1:
            click_coords.update({'X1': x, 'Y1': y})
        else:
            click_coords.update({'X2': x, 'Y2': y})
            cv2.destroyAllWindows()
        
        print(click_coords)
    


      # put coordinates as text on the image
    #   font = cv2.FONT_HERSHEY_SIMPLEX
    #   cv2.putText(img, str(x) + ',' + str(y), (x,y), font, 1, (255, 0, 0), 2)
      
    #   # show the updated image
    #   cv2.imshow('image', img)


def get_markings():
    # Read and display the image
    img = cv2.imread("temp\screenshots\screenshot.png")
    cv2.imshow('image', img)

    # Read the markings
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)
  
    # close the window
    cv2.destroyAllWindows()

    # # Calculate the distance between markings
    # distance = ((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2)**0.5
    # print(f"The distance between the marks is {distance} pixels.")
