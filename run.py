import time
from datetime import datetime

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
prev_frame_time = 0
new_frame_time = 0

if not cap.isOpened():
    print("Failed to launch camera")
    exit()
while True:
    ret, frame = cap.read()

    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time

    FPS = "FPS : " + str(fps)

    cv2.putText(
        frame,
        FPS,
        (1, 55),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2,
    )

    DT = "Timestamp : " + str(datetime.now())

    cv2.putText(
        frame,
        DT,
        (1, 25),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
    )

    print("Console Log | ", DT, " | ", FPS)

    if not ret:
        break

    feed1 = frame
    feed2 = cv2.edgePreservingFilter(frame, flags=1, sigma_s=60, sigma_r=0.4)

    feed = np.concatenate((feed1, feed2), axis=1)

    cv2.imshow("CAM FEED", feed)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
