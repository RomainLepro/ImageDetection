import cv2
import time


thres = 0.55 # Threshold to detect object
t = time.time()
tbegin = time.time()
cap = cv2.VideoCapture(0)
cap.set(3,1920)
cap.set(4,1080)
cap.set(10,70)



success,img = cap.read()


 
classNames= []
globalPath = ".\\"
classFile = globalPath+"coco.names"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")
 
configPath = globalPath+"ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = globalPath+"frozen_inference_graph.pb"
 
net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(300,150)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


print(classNames)
print(len(classNames))

while True:

    dt = time.time()-t
    t = time.time()
    fps_value = 1/dt

    success,img = cap.read()
    
    if img is None:
        print("failed to access webcam")
        path = "./lena.png"
        img = image = cv2.imread(path)
    
    classIds, confs, bbox = net.detect(img,confThreshold=thres)
    print(classIds,bbox)
    print(fps_value)
 
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(img,box,color=(0,255,0),thickness=2)
            cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    cv2.putText(img,str(round(fps_value,2)),(10,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
 
    cv2.imshow("Output",img)

    if cv2.waitKey(1) == 27 :#or cv2.XDestroyWindowEvent: 
            cv2.destroyAllWindows()
            cap.release()
            break  # esc to quit
            
    if(t>tbegin+15): # break after 5s
            cv2.destroyAllWindows()
            cap.release()
            break
        

    