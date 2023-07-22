import kivy
kivy.require('1.9.0')
import cv2
import numpy as np
import face_recognition as fr
import os
import pyttsx3
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture


path="images"
images=[]
className=[]
myList=os.listdir(path)
# print(myList)

for cls in myList:
    crntImage=cv2.imread(f'{path}/{cls}')
    images.append(crntImage)
    className.append(os.path.splitext(cls)[0])

print(className)
## Encoding

def find_encoding(images):
    encode_list=[]

    for img in images:    
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=fr.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list


encodeListKnown=find_encoding(images)

class MainApp(MDApp):


    def build(self):
        layout=MDBoxLayout(orientation="vertical")
        self.image=Image()
        layout.add_widget(self.image)
        self.save_img_button=MDRaisedButton(
            text="Click here",
            pos_hint={'center_x': .5,"center_y": .5},
            size_hint=(None,None)

        )
        self.save_img_button.bind(on_press=self.save_frame)
        layout.add_widget(
            self.save_img_button
        )
        self.cap=cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video,1.0/30.0)


        return layout
    

    def load_video(self, *args):
        ret,frame=self.cap.read()

        self.image_frame=frame 
        buffer=cv2.flip(frame,0).tostring()
        texture=Texture.create(size=(frame.shape[1],frame.shape[0]),colorfmt='bgr')
        texture.blit_buffer(buffer,colorfmt='bgr',bufferfmt='ubyte')
        self.image.texture=texture
        


    def save_frame(self, *args):
        cv2.imwrite(r"C:\Users\Nurhan\Desktop\face_detection\frames\frame.png",self.image_frame)
        # Now, use the face recognition code to check if the person in the saved frame is your friend or not
        captured_frame = cv2.imread(r"C:\Users\Nurhan\Desktop\face_detection\frames\frame.png")
        captured_frame_rgb = cv2.cvtColor(captured_frame, cv2.COLOR_BGR2RGB)
        captured_frame_small = cv2.resize(captured_frame_rgb, (0, 0), None, 0.25, 0.25)
        faces_current_frame = fr.face_locations(captured_frame_small)
        encode_current_frame = fr.face_encodings(captured_frame_small, faces_current_frame)

        for encode_face, location in zip(encode_current_frame, faces_current_frame):
            matches = fr.compare_faces(encodeListKnown, encode_face)
            face_distances = fr.face_distance(encodeListKnown, encode_face)
            match_index = np.argmin(face_distances)

            if matches[match_index]:
                name = className[match_index].upper()
                print(f"The person in the captured frame is {name}!")

                # Optional: Use pyttsx3 to speak the result
                engine = pyttsx3.init()

                engine.say(f"The person in the captured frame is {name}!")
                engine.runAndWait()
            else:
                print("Unknown person!")
                engine = pyttsx3.init()
                engine.say(f"I do not know that person!")
                engine.runAndWait()




if __name__=='__main__':
    MainApp().run()













































































