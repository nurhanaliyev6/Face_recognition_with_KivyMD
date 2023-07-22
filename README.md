# Face_recognition_with_KivyMD
## Description
This Python application utilizes Kivy and OpenCV to implement a simple real-time face recognition system. The app captures frames from the webcam, saves one of the frames when the "Click here" button is pressed, and then attempts to recognize the face in the saved frame using face_recognition library. It compares the captured face with a set of known faces and identifies the person if recognized.

## Requirements
Python 3.x
Kivy (1.9.0 or later)
KivyMD
OpenCV (cv2)
NumPy
face_recognition
pyttsx3


## Installation
Install Python 3.x on your system if you haven't already.
Install the required packages using pip:
pip install kivy kivymd opencv-python numpy face_recognition pyttsx3


## How to Use the App
Ensure your webcam is connected and accessible by the app.
Run the main.py file to start the app.
The app will open, and you'll see a live video stream from the webcam.
When you want to save a frame for face recognition, click the "Click here" button.
The app will save the frame as frame.png in the specified directory (change the directory path if needed).
After saving the frame, the app will attempt to recognize the face using face_recognition.
If the person in the frame matches any of the known faces, the app will display the name of the recognized person.
If the person is not recognized, the app will display "Unknown person!".
Note: The recognition process is limited to the faces present in the images directory. Ensure you have stored known faces there before using the app.

## Important Notes
The accuracy of face recognition depends on the quality of the images in the images directory and the similarity between the captured face and the known faces.
The app may not work well in low-light conditions or if the faces are not clearly visible in the images.


## Customization
You can modify the app's behavior or appearance by editing the main.py file. For example, you can change the directory path where the captured frame is saved or customize the UI using KivyMD widgets.

## Troubleshooting
If you encounter any issues while running the app, make sure you have installed all the required packages correctly. Double-check the path of the images directory, and ensure the known faces are stored there with appropriate names.

## Credits
Kivy: https://kivy.org/
KivyMD: https://github.com/HeaTTheatR/KivyMD
OpenCV: https://opencv.org/
NumPy: https://numpy.org/
face_recognition: https://github.com/ageitgey/face_recognition
pyttsx3: https://github.com/nateshmbhat/pyttsx3

