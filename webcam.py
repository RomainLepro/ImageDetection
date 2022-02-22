import cv2
import time
tbegin = time.time()

def show_webcam():
    cap = cv2.VideoCapture(0)
    ret_val, img = cap.read()
    if img is None:
        path = "./lena.png"
        img = image = cv2.imread(path)
    cv2.imshow('my webcam', img)
    
    while True:
         ret_val, img = cap.read()

         if cv2.waitKey(1) == 27: 
             cv2.destroyAllWindows()
             cap.release()
             break  # esc to quit
         cv2.imshow('my webcam', img)
         if(time.time()>tbegin+10): # break after 5s
             cv2.destroyAllWindows()
             cap.release()
             break
         
    cv2.destroyAllWindows()
    


def main():
    show_webcam()


if __name__ == '__main__':
    print("main")
    main()
