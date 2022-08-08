import cv2
import mediapipe as mp


class fingerCounter(object):
    def __init__(self, close = 0):
        self.close = close

    def checkClose():
        if self.close == 0:
            self.getfingers()
        else:
            print('Program paused/finished.')

    def getfingers(self):
        try:
            cap = cv2.VideoCapture(0)
            mp_Hands = mp.solutions.hands
            hands = mp_Hands.Hands()
            mpDraw = mp.solutions.drawing_utils
            
            finger_Coord = [(8, 6), (12, 10), (16, 14), (20, 18)]
            thumb_Coord = (4,2)

            while True:
                success, image = cap.read()
                RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = hands.process(RGB_image)
                multiLandMarks = results.multi_hand_landmarks


                if multiLandMarks:
                    handList = []
                    for handLms in multiLandMarks:
                        mpDraw.draw_landmarks(image, handLms, mp_Hands.HAND_CONNECTIONS)
                        for idx, lm in enumerate(handLms.landmark):
                            h, w, c = image.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            handList.append((cx, cy))

                    upCount = 0
                    for coordinate in finger_Coord:
                        if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
                            upCount += 1
                    if handList[thumb_Coord[0]][0] > handList[thumb_Coord[1]][0]:
                        upCount += 1

                    upCount = str(upCount)
                    with open('fingercount.txt', 'w+') as f:
                        f.write('{}'.format(upCount))
                    
                    if self.close == 1:
                        break
            cap.release()
            cv2.destroyAllWindows()
        except KeyboardInterrupt:
            exit("Process canceled")
