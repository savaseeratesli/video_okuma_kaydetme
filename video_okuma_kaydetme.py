import cv2

# #Kameradan görüntü alma

# cam=cv2.VideoCapture(0)

# #Kamera Ozellikleri iiçn
# print(cam.get(3))

# cam.set(3,320)#Ayar


# #Kamera portu hatası almamak için
# if not cam.isOpened():
#     print("Tanimsiz Kamera")
#     exit()


# while True:
#     ret,frame=cam.read() #ret->görüntü okundu mu? frame->cerceve
    
#     if not ret:
#         print("Kamera Goruntusu Yok")
#         break
    
#     cv2.imshow("Kamera1",frame)
    
#     if cv2.waitKey(1)&0xFF==ord("q"):
#         print("Kamera Kapatildi")
#         break
    
# cam.release()#Kameranın kapanması için
# cv2.destroyAllWindows()
    
#######################################

# #Görüntü kaydetme

# cam=cv2.VideoCapture(0)

# fourrc=cv2.VideoWriter_fourcc(*'XVID')#Video formatı

# out=cv2.VideoWriter("Video.avi",fourrc,30.0,(640,480))

# while cam.isOpened():
    
#     ret,frame=cam.read()
    
#     if not ret:
#         print("Kamera Acilmadi")
#         break
    
#     out.write(frame)
    
#     cv2.imshow("Kamera1",frame)
    
#     if cv2.waitKey(1)==ord("q"):
#         print("Cikis")
#         break

# cam.release()
# out.release()
# cv2.destroyAllWindows()

#######################################

#IP telefon kamerası
#IP Webcam uygulamasını indiriniz ve çıkan http://IP:PORT/video not alınız

url="http://192.168.1.20:8080/video"

cam=cv2.VideoCapture(url)

while cam.isOpened():
    ret,frame=cam.read()
    
    if not ret:
        print("Baglanti Yok")
        
    cv2.imshow("KameraIP",frame)
    
    if cv2.waitKey(1)==ord("q"):
        print("Cikis")
        break



















