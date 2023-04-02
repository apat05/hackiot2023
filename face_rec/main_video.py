def capture():
    import cv2
    import time
    from simple_facerec import SimpleFacerec


    # Encode faces from a folder
    sfr = SimpleFacerec()
    sfr.load_encoding_images("images/")

    # Load Camera
    cap = cv2.VideoCapture(1)
    flag = 0
    idx = -100
    while flag == 0:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        cv2.imshow("Frame", frame)
        name = sfr.known_face_names[sfr.best_match_index]
        if name == "Aum" or name == "Quoc" or name == "Kevin" or name == "Russell" or name == "unknown":
            flag = 1
            if (name == "Aum"):
                idx = 0
            elif (name == "Quoc"):
                idx = 1
            elif (name == "Kevin"):
                idx = 2
            elif (name == "Russell"):
                idx = 3

    cap.release()
    cv2.destroyAllWindows()
    return idx
