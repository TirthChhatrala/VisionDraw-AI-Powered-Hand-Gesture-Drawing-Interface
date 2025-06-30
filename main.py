import cv2
import mediapipe as mp
from utils import fingers_open
from color_popup import choose_color

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

draw_color = (0, 0, 255)
brush_thickness = 5
drawing = False
color_popup_open = False
prev_point = None

canvas = None

while True:
    success, img = cap.read()
    if not success:
        break
    img = cv2.flip(img, 1)

    if canvas is None:
        canvas = img.copy() * 0

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)

    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            h, w, _ = img.shape
            mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)

            open_fingers = fingers_open(handlms, img.shape)
            cx, cy = int(handlms.landmark[8].x * w), int(handlms.landmark[8].y * h)

            if open_fingers == 1:
                drawing = True
                if prev_point is not None:
                    cv2.line(canvas, prev_point, (cx, cy), draw_color, brush_thickness)
                prev_point = (cx, cy)

            elif open_fingers == 2:
                drawing = False
                prev_point = None
                color_popup_open = False

            elif open_fingers == 3 and not color_popup_open:
                drawing = False
                color = choose_color()
                if color:
                    draw_color = color
                color_popup_open = True
                prev_point = None

            elif open_fingers == 4:
                canvas[:] = 0
                prev_point = None

            elif open_fingers == 5:
                cv2.imwrite("drawing_output.png", cv2.add(img, canvas))
                prev_point = None

    else:
        prev_point = None

    # Overlay canvas on real-time image
    combined = cv2.addWeighted(img, 0.5, canvas, 0.5, 0)
    cv2.imshow("Drawing App", combined)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('+') or key == ord('='):
        brush_thickness += 1
    elif key == ord('-') and brush_thickness > 1:
        brush_thickness -= 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
