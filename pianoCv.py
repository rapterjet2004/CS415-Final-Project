import cv2
import mediapipe as mp
import pygame

pygame.mixer.init()

piano_notes = ['C4.mp3', 'Db4.mp3', 'D4.mp3', 'Eb4.mp3', 'E4.mp3', 'F4.mp3', 'Gb4.mp3', 'G4.mp3']
sounds = [pygame.mixer.Sound(note) for note in piano_notes]

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils


num_keys = len(piano_notes)
width, height = 1280, 720
key_width = width // num_keys

last_key = -1

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    for i in range(num_keys):
        color = (200, 200, 200) if i != last_key else (0, 255, 0)
        cv2.rectangle(frame, (i * key_width, 0), ((i + 1) * key_width, 100), color, -1)
        cv2.rectangle(frame, (i * key_width, 0), ((i + 1) * key_width, 100), (0, 0, 0), 2)
        cv2.putText(frame, piano_notes[i][:2], (i * key_width + 10, 60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

    current_key = -1
    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:

            index_finger_tip = hand_lms.landmark[8]
            x, y = int(index_finger_tip.x * width), int(index_finger_tip.y * height)

            cv2.circle(frame, (x, y), 15, (255, 0, 255), cv2.FILLED)


            if y < 100:
                current_key = x // key_width

                if current_key != last_key:
                    sounds[current_key].play()
                    last_key = current_key

            if y > 100:
                last_key = -1

            mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Air Piano", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 