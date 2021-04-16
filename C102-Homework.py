import cv2
import dropbox
import random
import time

beginTime = time.time()

def snapshot():
     n = random.randint(0,100)

     videoCaptureObject = cv2.VideoCapture(0)
     result = True

     while(result):
         ret, frame = videoCaptureObject.read()

         imageName = "imageNo." + str(n) + ".jpg"
         cv2.imwrite(imageName, frame)
         beginTime = time.time()
         result = False

     return imageName
     print("Image captured! LOL u were being surveli...en......ce...d(I dunno the spelling)")
     videoCaptureObject.release()

     cv2.destroyAllWindows()

def updateDb(imageName):
     accessToken = "oxw2lm8DSoAAAAAAAAAAActbWO4xrTI1o4AyepzIkKGdNyKXlXOJRoSX6ukQ2rEL"

     fileFrom = imageName
     fileTo = "/C102-Homework/" + imageName

     db = dropbox.Dropbox(accessToken)

     with open(fileFrom, "rb") as f:
          db.files_upload(f.read(), fileTo, mode = dropbox.files.WriteMode.overwrite)
          print("Your image uploaded!!! Calling 911 for using my laptop without permission!")

def main():
     while(True):
           if((time.time() - beginTime) >= 5):
               name = snapshot()
               updateDb(name)

main()
