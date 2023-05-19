import cv2
cap = cv2.VideoCapture(0)
rotate_flag = False
flip_flag = False
scale_flag = False
while True:
    ret, frame = cap.read()
    key = cv2.waitKey(1)
    if key == ord('r'):
      rotate_flag = not rotate_flag
    if key == ord('l'):
        flip_flag = not flip_flag
    if key == ord('s'):
        scale_flag = not scale_flag
    if rotate_flag:
       (h, w) = frame.shape[:2]
       rotated_frame = cv2.warpAffine(frame, cv2.getRotationMatrix2D((w // 2, h // 2), 90, 1.0), (w, h))
       frame =  rotated_frame
    if flip_flag:
        frame = cv2.flip(frame, 1)
    if scale_flag:
        frame = cv2.resize(frame, None, fx=4, fy=4, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('frame', frame)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


