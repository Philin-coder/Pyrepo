import cv2

capture = cv2.VideoCapture(0)
while (True):
    ret, frame = capture.read()
    grv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('my win', frame)
    # cv2.imshow('frame',grv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('stopeed')
        break

capture.release()
cv2.destroyAllWindows()
