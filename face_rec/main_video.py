def capture():
    import cv2
    import time
    from face_rec import simple_facerec as sf
    from picamera.array import PiRGBArray
    from picamera import PiCamera


    # Encode faces from a folder
    sfr = sf.SimpleFacerec()
    sfr.load_encoding_images("face_rec/images/")

    # Load Camera
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))
    time.sleep(0.1)
    # cap = cv2.VideoCapture(1)
    idx = -100
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(image)
        # for face_loc, name in zip(face_locations, face_names):
        #     y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        #     cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        #     cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        # cv2.imshow("Frame", frame)
        print(len(sfr.known_face_names))
        print((sfr.best_match_index))
        rawCapture.truncate(0)
        name = sfr.known_face_names[sfr.best_match_index]
        print(name)
        for i in sfr.known_face_names:
            print(i)
        if name == "Aum" or name == "Quoc" or name == "Kevin" or name == "Russell" or name == "unknown":
            if (name == "Aum"):
                idx = 0
            elif (name == "Quoc"):
                idx = 1
            elif (name == "Kevin"):
                idx = 2
            elif (name == "Russell"):
                idx = 3
            break

    
    cv2.destroyAllWindows()
    camera.stop_preview()
    camera.close()
    return idx
