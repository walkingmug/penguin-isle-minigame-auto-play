import cv2


def click_event(event, x, y, flags, params):
   if event == cv2.EVENT_LBUTTONDOWN:
      print(f'({x},{y})')
      
      # put coordinates as text on the image
      font = cv2.FONT_HERSHEY_SIMPLEX
      cv2.putText(img, str(x) + ',' + str(y), (x,y), font, 1, (255, 0, 0), 2)
      
      # show the updated image
      cv2.imshow('image', img)


def get_markings():
    # Read and display the image
    img = cv2.imread("temp\screenshots\screenshot.png")
    cv2.imshow('image', img)

    # Read the markings
    cv2.setMouseCallback('image', click_event)

    # Exit on keypress
    cv2.waitKey(0)
    
    # lose the window
    cv2.destroyAllWindows()

    # # Calculate the distance between markings
    # distance = ((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2)**0.5
    # print(f"The distance between the marks is {distance} pixels.")

get_markings()

