import os
import string
import cv2


dataset = './data'
if not os.path.exists(dataset):
    os.makedirs(dataset)

#number_of_classes = list(string.ascii_uppercase) #total classs all alphabet
number_of_classes = [c for c in string.ascii_uppercase if c not in ['J', 'Z']] #total class all alphabet kecuali J dan Z 

dataset_size = 100 

cap = cv2.VideoCapture(0) 
for i in number_of_classes:
    if not os.path.exists(os.path.join(dataset, str(i))):
        os.makedirs(os.path.join(dataset, str(i)))
    print('Collecting data for class {}'.format(i))

    done = False
    while True:
        ret, frame = cap.read() #baca frame 
        cv2.putText(frame, f'Collecting: {i} | Press "Q" to start', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,cv2.LINE_AA) #masukin kata kata di layar
        cv2.imshow('frame', frame) # live view
        if cv2.waitKey(25) & 0xFF  == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(dataset, str(i), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()