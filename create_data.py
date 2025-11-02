import cv2
import mediapipe as mp
import os
import matplotlib.pyplot as plt
import pickle


DATASET = './data'

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True,min_detection_confidence=0.3)

data = []
labels = []

for dir_ in os.listdir(DATASET): 
    for img_path in os.listdir(os.path.join(DATASET,dir_)):
        data_aux = []
        img = cv2.imread(os.path.join(DATASET,dir_,img_path))
        img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        
        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x)
                    data_aux.append(y)


                data.append(data_aux)
                labels.append(dir_)

                    #mp_drawing.draw_landmarks(img_rgb, #img to drawhand_landmarks,#model outputmp_hands.HAND_CONNECTIONS, #hand connections mp_drawing_styles.get_default_hand_landmarks_style(), mp_drawing_styles.get_default_hand_connections_style())

if len(data) > 0 and len(labels) > 0:
    with open('data.pickle', 'wb') as f:
        pickle.dump({'data': data, 'labels': labels}, f)
    print("✅ data.pickle successfully created!")
else:
    print("⚠️ No hand data detected. Please check your dataset.")
