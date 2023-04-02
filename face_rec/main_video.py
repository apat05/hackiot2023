def captureimage():
    import cv2
    import time
    import face_recognition
    #from face_rec import simple_facerec as sf
    from picamera.array import PiRGBArray
    from picamera import PiCamera


    # Encode faces from a folder
   # sfr = sf.SimpleFacerec()
   # sfr.load_encoding_images("face_rec/images/")

    # Load Camera

    camera = PiCamera()
   # camera.resolution = (2592, 1944)
   # camera.resolution = (640, 480)
    rawCapture = PiRGBArray(camera)
    time.sleep(0.1)
    camera.capture('face_rec/images/image.jpg')
    camera.stop_preview()
    camera.close()

    img = cv2.imread("face_rec/images/image.jpg")    
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_encoding = face_recognition.face_encodings(rgb_img)[0]

    aum = cv2.imread("face_rec/images/Aum.jpg")
    rgb_aum = cv2.cvtColor(aum, cv2.COLOR_BGR2RGB)
    aum_encoding = face_recognition.face_encodings(rgb_aum)[0]

    Quoc = cv2.imread("face_rec/images/Quoc.jpg")
    rgb_Quoc = cv2.cvtColor(Quoc, cv2.COLOR_BGR2RGB)
    quoc_encoding = face_recognition.face_encodings(rgb_Quoc)[0]

    Russell = cv2.imread("face_rec/images/Russell.jpg")
    rgb_Russell = cv2.cvtColor(Russell, cv2.COLOR_BGR2RGB)
    rus_encoding = face_recognition.face_encodings(rgb_Russell)[0]

    Kevin = cv2.imread("face_rec/images/Kevin.jpg")
    rgb_Kevin = cv2.cvtColor(Kevin, cv2.COLOR_BGR2RGB)
    kev_encoding = face_recognition.face_encodings(rgb_Kevin)[0]

    if face_recognition.compare_faces([img_encoding], aum_encoding):
        idx = 0
    elif face_recognition.compare_faces([img_encoding], quoc_encoding):
        idx = 1
    elif face_recognition.compare_faces([img_encoding], kev_encoding):
        idx = 2
    elif face_recognition.compare_faces([img_encoding], rus_encoding):
        idx = 3
    else:
        idx = 0

        # if name == "Aum" or name == "Quoc" or name == "Kevin" or name == "Russell" or name == "unknown":
        #     if (name == "Aum"):
        #         idx = 0
        #     elif (name == "Quoc"):
        #         idx = 1
        #     elif (name == "Kevin"):
        #         idx = 2
        #     elif (name == "Russell"):
        #         idx = 3
        #     break

    
    cv2.destroyAllWindows()
    return idx
