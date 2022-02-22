import cv2
tbegin = time.time()

def show_webcam(mirror=False):
    cam = cv2.VideoCapture()
    ret_val, img = cam.read()
    if img is None:
        path = "/home/pi/Desktop/imageDetection/ImageDetection/lena.png"
        img = image = cv2.imread(path)
    cv2.imshow('my webcam', img)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
            
            
        if(t>tbegin+5): # break after 5s
            break
    cv2.destroyAllWindows()
    


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    print("main")
    main()
