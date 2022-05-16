import face_recognition
import os
import cv2
import json
import requests
#from django.db import models
#import django



# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite/settings.py')
# settings.configure()



KNOWN_FACES_DIR = 'coaches'
UNKNOWN_FACES_DIR = 'whoThis'
TOLERANCE = 0.5
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'cnn'  # default: 'hog', other one can be 'cnn' - CUDA accelerated (if available) deep-learning pretrained model

print(KNOWN_FACES_DIR)
# Returns (R, G, B) 
def name_to_color(name):
    
    color = [(ord(c.lower())-97)*8 for c in name[:3]]
    return color


print('Loading known faces...')
known_faces = []
known_names = []


# Each subfolder's name becomes our label (name)
for name in os.listdir(KNOWN_FACES_DIR):


    # Next we load every file of faces of known person
    for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
        

        # Load an image
        image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')

        # Get 128-dimension face encoding
        # Always returns a list of found faces, for this purpose we take first face only (assuming one face per image as you can't be twice on one image)
        encoding = face_recognition.face_encodings(image)[0]

        # Append encodings and name
        
        known_faces.append(encoding)
        known_names.append(name)
        
        
        


print('Processing unknown faces...')
# Now let's loop over a folder of faces we want to label
for filename in os.listdir(UNKNOWN_FACES_DIR):
   

    # Load image
    # print(f'Filename {filename}', end='')
    image = face_recognition.load_image_file(f'{UNKNOWN_FACES_DIR}/{filename}')
    locations = face_recognition.face_locations(image, model=MODEL)
    encodings = face_recognition.face_encodings(image, locations)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
   

    
    # print(f', found {len(encodings)} face(s)')
    for face_encoding, face_location in zip(encodings, locations):

        
        # Returns array of True/False values in order of passed known_faces
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)

        # Since order is being preserved, we check if any face was found then grab index
        # then label (name) of first matching known face withing a tolerance
        match = None
        if True in results:  # If at least one is true, get a name of first of found labels
            match = known_names[results.index(True)]
            print(f' this is the face of {match} ')

           