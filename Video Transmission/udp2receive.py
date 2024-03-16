
# This is client code to receive video frames over UDP
import cv2, imutils, socket
import numpy as np
import time
import base64
from ultralytics import YOLO
import math 

BUFF_SIZE = 65536
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
host_ip = 'raspberrypi.local'#  socket.gethostbyname(host_name)
print(host_ip)
port = 8080
message = b'Hello'

# model
model = YOLO("yolo-Weights/yolov8n.pt")

# object classes
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]



client_socket.sendto(message,(host_ip,port))
fps,st,frames_to_count,cnt = (0,0,20,0)
while True:
	packet,_ = client_socket.recvfrom(BUFF_SIZE)
	data = base64.b64decode(packet,' /')
	npdata = np.fromstring(data,dtype=np.uint8)
	frame = cv2.imdecode(npdata,1)
	results=model(frame,stream=True)
	for r in results:
		boxes = r.boxes
		for box in boxes:
            # bounding box
			x1, y1, x2, y2 = box.xyxy[0]
			x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
			cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confidence
			confidence = math.ceil((box.conf[0]*100))/100
			print("Confidence --->",confidence)

            # class name
			cls = int(box.cls[0])
			print("Class name -->", classNames[cls])

            # object details
			org = [x1, y1]
			font = cv2.FONT_HERSHEY_SIMPLEX
			fontScale = 1
			color = (255, 0, 0)
			thickness = 2
			cv2.putText(frame, classNames[cls], org, font, fontScale, color, thickness)
	frame =cv2.resize(frame, (1600, 900)) #Control the size of the window 
	results=model(frame,stream=True)
	cv2.imshow("RECEIVING VIDEO",frame)
	
	key = cv2.waitKey(1) & 0xFF
	if key == ord('q'):
		client_socket.close()
		break
	if cnt == frames_to_count:
		try:
			fps = round(frames_to_count/(time.time()-st))
			st=time.time()
			cnt=0
		except:
			pass
	cnt+=1

