Sign Language Alphabet Recognition

A real-time American Sign Language (ASL) alphabet recognition system built using MediaPipe, OpenCV, and Scikit-learn.
This project recognizes static ASL alphabet gestures (A–Z), except for letters J and Z, which require motion.

Note : 
- This version cannot recognize letters J and Z, since they require motion tracking.
- The system currently focuses on static ASL alphabet gestures.
- The project is still under development, and future updates will include motion-based gesture learning.

Requirements : 
numpy                 2.0.1
opencv-python         4.10.0.84
mediapipe             0.10.14
scikit-learn          1.7.2

Steps:

Save all .py files in one folder.
Run collect_image.py → capture gesture images using your webcam.
Create your own dataset (each gesture will saved in a folder data and have own folder for each alphabet).
Run create_data.py → extract landmarks and store as dataset.
Run train_classifier.py → train your model using the dataset.
Run inference_classifier.py → start real-time recognition from webcam.
Use and test → show hand gestures in front of the camera to see predictions.


