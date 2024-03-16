# Communication
The Repo involves establishing communication between Rover and Base Station.
These Python scripts enable real-time video transmission over UDP. updtransmission.py acts as the server, capturing video from a webcam and sending frames to a client. udpreciever.py serves as the client, receiving and displaying the video frames.
**Update:**
The system can now transmit the video over UDP and classify the objects in the POV of the camera using **YOLOV8**
**Dependencies:**
1. cv2
2. imutils
3. socket
4. numpy
5. time
6. base64
7. YoloV8

# Getting Started:
1. pip install opencv-python numpy imutils
2. pip install ultralytics

   
# Instructions:

1. Edit the host_ip variables in both scripts to match the IP address of the transmitting device (server) and receiving device (client). You can find the IP addresses using ifconfig or ip addr commands.
2. Run updtransmission.py first. The terminal should display "Listening at:" followed by the server's IP address and port.
3. Then, run udpreciever.py. The client will begin receiving and displaying the video frame.

If one wishes to transmit the data from a local CPU like Nividia Jetson Orin, Nano or any other microcontroller, it comes with restriction that we don't want to join the monitor to our micro-controller everytime we want to execute udptransmission.py. To resolve this issue one can easily ssh the ipconfig and then execute udptransmision.py.

Specifically for Team Vicharaka:
We have set the name of ssh for our Raspberry pi as rover@raspberrypi.local. So, type ssh rover@raspberrypi.local and type password to access raspberrypi of Team vicharaka and work according to the instructions provided.
These Python scripts, updtransmission.py and udpreciever.py, enable real-time video transmission over UDP. Imagine a live video feed between devices! The server script captures webcam footage, processes it, and sends it as encoded frames to the client script. There, the frames are decoded, displayed, and FPS is calculated for smooth viewing. 
Feel free to fork this repository, improve the code, and submit pull requests.
