"""
Created on Thu Dec 22 20:44:03 2022

@author: Focus
"""

import cv2
from pyzbar.pyzbar import decode
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
import time
from upload_video import upload_video

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
valid_codes=[]
used_codes=[]

start = True
while start == True:
    print("To start scan type 1 or to exit type 2 : ")
    gonext=int(input())
    if gonext==2:
        camera=False
        start==False
        frame1=cap.read()
        cap.release() 
        break
    elif gonext ==1:
        camera=True
        while camera == True:
            success, frame1=cap.read()
            for code in decode(frame1):
                
                if code.data.decode('utf-8') not in used_codes:
                    print("Approved "+code.data.decode('utf-8')+" is added to your lists.")
                    print("\n")
                    used_codes.append(code.data.decode('utf-8')) 
                    time.sleep(1)
                    print("Start Recording.............\n")
                    time.sleep(1)
                    # open output video file stream
                    named="Recorded_"+str(code.data.decode('utf-8'))
                    video = VideoWriter(named+".avi", VideoWriter_fourcc(*'MP42'), 25.0, (640, 480))
                    # main loop
                    while True:
                        # get the frame from the webcam
                        stream_ok, frame = cap.read()
                        
                        # if webcam stream is ok
                        if stream_ok:
                            # display current frame
                            cv2.imshow('Webcam', frame)
                            
                            # write frame to the video file
                            video.write(frame)

                        # escape condition
                        if cv2.waitKey(1) & 0xFF == 27: break
                    # release web camera stream
                    #cap.release()
                    # clean ups
                    cv2.destroyAllWindows()
                    
                    # release video output file stream
                    video.release()
                    camera=False
                    
                    
                
                elif code.data.decode('utf-8') in used_codes:
                    print("Uploading a video to Youtube")
                    video_data = {
            "file": named+".avi",
            "title": named,
            "description": "Video for GoDangCorp Customer",
            "keywords":"GoDangCorp",
            "privacyStatus":"unlisted"
    }
                    print(video_data["title"])
                    print("Posting Video...")
                    upload_video(video_data)
                    
                    camera=False
                    #cap.release()
                else:
                    pass
        
       # cv2.imshow('Testing-code-scan',frame)
        #cv2.waitKey(1)
        
        
print("NOT in while True\n")
print(used_codes)
print(upload_video.response)


