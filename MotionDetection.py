import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

# iterating lets camera have the timet to adjust to the lightening and aspect ratios
for _ in range(10):
    _, background = cap.read()
background = cv2.resize(background, (1280, 720))
background = cv2.flip(background, 1)
background = cv2.cvtColor(background,cv2.COLOR_BGR2GRAY)

while True:
    # reading, resizing and fliping the frame
    _, frame = cap.read()
    frame = cv2.resize(frame, (1280, 720))
    frame = cv2.flip(frame,1)

    # processing the frame
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    foreground = grey - background

    cv2.imshow("Webcam",foreground)

    if cv2.waitKey(1) == ord('q'):
        break

