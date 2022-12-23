"""
Created on Thu Dec 22 20:44:03 2022

@author: Focus
"""
import cv2
from pyzbar.pyzbar import decode
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
valid_codes=[]
used_codes=[]
link_data={}

#Class for Customer data
# define a class
class customer:
    # define a property
    name_ = ""
    tel_=""
    link_=""
    

import readingExcel

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
                    named=str(code.data.decode('utf-8'))
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
                    upload_file_list = [named+'.avi']
                    for upload_file in upload_file_list:
                    	gfile = drive.CreateFile({'parents': [{'id': '1bbF4m3RZOJC3_eJeafXsEnFU4Il0OgAq'}]})
                    	# Read file and set it as the content of this instance.
                    	gfile.SetContentFile(upload_file)
                    	gfile.Upload() # Upload the file.
                    
                    
                    camera=False
                    #cap.release()
                else:
                    pass
        
            cv2.imshow('Testing-code-scan',frame1)
            cv2.waitKey(1)
        


print("NOT in while True\n")
file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1bbF4m3RZOJC3_eJeafXsEnFU4Il0OgAq')}).GetList()
for file in file_list:
    print('title: %s, id: %s' % (file['title'], file['id']));
    link_data[file['title']] = customer()
    link_data[file['title']].link_ = file['alternateLink']
    link_data[file['title']].name_ = readingExcel.get_customername(named)
    link_data[file['title']].tel_= readingExcel.get_customernumber(named)
    # readingExcel.get_customername(named)
    # readingExcel.get_customernumber(named)
    # readingExcel.writetofile(" "+file['alternateLink'])
print(link_data)



############################ SEND SMS ####################
for key in link_data:
    print("\nSending SMS to number "+link_data[key].tel_+"\n")
    print("เรียนคุณ"+link_data[key].name_+"\nลูกค้าสามารถตรวจสอบวีดีโอการจัดส่งสินค้าได้ที่ลิงค์ "+link_data[key].link_+"\n ทางร้านขอขอบพระคุณเป็นอย่างสูง")