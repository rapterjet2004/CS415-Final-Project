import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import pygame

# Set up key sounds
pygame.mixer.init()
white_names = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
black_names = ['Db4', 'Eb4', 'Gb4', 'Ab4', 'Bb4']

sounds = {}
for name in white_names + black_names:
    try:
        sounds[name] = pygame.mixer.Sound(name + ".mp3")
    except:
        print(f"Warning: Missing {name}.mp3")

# Setup piano screen
screen_width = 1280
screen_height = 720
key_w = screen_width // 7 
key_h = 400

# Add labels to white keys
white_keys = []
for i in range(7):
    x1 = i * key_w
    x2 = (i + 1) * key_w
    if i == 6: x2 = screen_width 
    white_keys.append([x1, 0, x2, key_h, white_names[i]])

# Add labels to black keys
black_keys = []
bw, bh = 100, 250
seams = [1, 2, 4, 5, 6] 
for i in range(5):
    center_x = seams[i] * key_w
    x1 = center_x - (bw // 2)
    black_keys.append([x1, 0, x1 + bw, bh, black_names[i]])

# Setup finger tracking
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, screen_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, screen_height)

# Last positions of left and right fingers
last_left, last_right = "", ""

cv2.namedWindow("Air Piano", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Air Piano", screen_width, screen_height)

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (screen_width, screen_height))
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    result = detector.detect(mp_image)

    # Finds fingers 
    current_touch_left = ""
    current_touch_right = ""
    finger_positions = [] # Stores finger positions

    if result.hand_landmarks:
        for idx, hand in enumerate(result.hand_landmarks):
            tip = hand[8]
            fx, fy = int(tip.x * screen_width), int(tip.y * screen_height)
            finger_positions.append((fx, fy)) 

            if fy < key_h:
                note = ""
                for k in black_keys:
                    if fx > k[0] and fx < k[2] and fy < k[3]:
                        note = k[4]
                if note == "":
                    for k in white_keys:
                        if fx > k[0] and fx < k[2]:
                            note = k[4]
                
                if idx == 0: current_touch_left = note
                else: current_touch_right = note

    # Draw white keys
    for k in white_keys:
        pressed = (k[4] == current_touch_left or k[4] == current_touch_right)
        color = (150, 255, 150) if pressed else (255, 255, 255)
        cv2.rectangle(frame, (k[0], k[1]), (k[2], k[3]), color, -1)
        cv2.rectangle(frame, (k[0], k[1]), (k[2], k[3]), (0, 0, 0), 2)
        cv2.putText(frame, k[4][0], (k[0] + 70, 370), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,0), 3)

    # Draw black keys
    for k in black_keys:
        pressed = (k[4] == current_touch_left or k[4] == current_touch_right)
        color = (0, 200, 0) if pressed else (30, 30, 30)
        cv2.rectangle(frame, (int(k[0]), k[1]), (int(k[2]), k[3]), color, -1)
        cv2.rectangle(frame, (int(k[0]), int(k[1])), (int(k[2]), int(k[3])), (0, 0, 0), 2)
        cv2.putText(frame, k[4][:2], (int(k[0]) + 15, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    # Draw finger tracking circles
    for pos in finger_positions:
        # Draw the purple circle on top of everything else
        cv2.circle(frame, pos, 20, (255, 0, 255), -1)
        cv2.circle(frame, pos, 22, (255, 255, 255), 2)

    # Play each sound
    if current_touch_left != last_left:
        if current_touch_left: sounds[current_touch_left].play()
        last_left = current_touch_left
        
    if current_touch_right != last_right:
        if current_touch_right: sounds[current_touch_right].play()
        last_right = current_touch_right

    cv2.imshow("Air Piano", frame)
    if cv2.waitKey(1) == ord('q'): break

cap.release()
cv2.destroyAllWindows()
