import cv2
import face_recognition
import numpy as np
from datetime import datetime
import csv

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

        # Load known faces
        self.known_face_encodings = []
        self.known_face_names = []

        ranit_image = face_recognition.load_image_file("assets/ranit_manik.jpg")
        ranit_encoding = face_recognition.face_encodings(ranit_image)[0]
        self.known_face_encodings.append(ranit_encoding)
        self.known_face_names.append("ranit")

        salman_khan_image = face_recognition.load_image_file("assets/salman_khan.jpg")
        salman_khan_encoding = face_recognition.face_encodings(salman_khan_image)[0]
        self.known_face_encodings.append(salman_khan_encoding)
        self.known_face_names.append("salman")

        king_image = face_recognition.load_image_file("assets/shah_rukh_khan.jpg")
        king_encoding = face_recognition.face_encodings(king_image)[0]
        self.known_face_encodings.append(king_encoding)
        self.known_face_names.append("king")

        # Create CSV file for attendance
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        self.csv_file = open(f"{current_date}.csv", "w+", newline="")
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(["Name", "Date", "Time"])
        self.recorded_names = set()

    def __del__(self):
        self.video.release()
        self.csv_file.close()

    def get_frame(self):
        success, frame = self.video.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            face_distance = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]

                if name not in self.recorded_names:
                    current_time = datetime.now().strftime("%H:%M:%S")
                    self.csv_writer.writerow([name, datetime.now().strftime("%Y-%m-%d"), current_time])
                    self.recorded_names.add(name)

                top, right, bottom, left = [v * 4 for v in face_location]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, name, (left, top - 10), font, 0.75, (0, 0, 255), 2)

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
