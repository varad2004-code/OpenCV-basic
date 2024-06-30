import os
import cv2 as cv
import numpy as np

# List of people (directories) to process
people = ["Ben afflek", "Elton John"]
# Directory containing the training images
DIR = r"D:\Python\Computer vision\faces\train"

# Load the Haar Cascade classifier
haar_cascade = cv.CascadeClassifier("haar_face.xml")

# Lists to store features and labels
features = []
labels = []

def create_train():
    for person in people:
        # Construct the path to the person's directory
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        # Debugging: Print the constructed path
        print(f"Processing directory: {path}")

        # Check if the directory exists
        if not os.path.exists(path):
            print(f"Error: Directory {path} does not exist")
            continue

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            # Debugging: Print the image path
            print(f"Processing image: {img_path}")

            img_array = cv.imread(img_path)
            if img_array is None:
                print(f"Error: Failed to read image {img_path}")
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

# Create training data
create_train()

# Print the lengths of the features and labels lists
print(f"Length of the features list = {len(features)}")
print(f"Length of the labels list = {len(labels)}")

features=np.array(features,dtype="object")
labels=np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#train the Recognizer on the features list and labels list
face_recognizer.train(features,np.array(labels))

face_recognizer.save("face_trained.yml")
np.save("Features.npy",features)
np.save("labels.npy",labels)