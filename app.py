from flask import Flask, render_template, Response, jsonify, request
import face_recognition
import cv2
import os
import numpy as np

app = Flask(__name__)

video_capture = cv2.VideoCapture(0)

# Directory for storing captured images
CAPTURED_IMAGES_DIR = "static/captured_images"
os.makedirs(CAPTURED_IMAGES_DIR, exist_ok=True)

# Load known images and encodings
sid_image = face_recognition.load_image_file("Sidd/Siddhramayya.jpg")
sid_face_encoding = face_recognition.face_encodings(sid_image)[0]

hrithik_image = face_recognition.load_image_file("Hrithik/hrithik.jpg")
hrithik_face_encoding = face_recognition.face_encodings(hrithik_image)[0]

salman_image = face_recognition.load_image_file("Salman/salman.jpeg")
salman_face_encoding = face_recognition.face_encodings(salman_image)[0]

sharukh_image = face_recognition.load_image_file("Sharukh/sharukh.jpeg")
sharukh_face_encoding = face_recognition.face_encodings(sharukh_image)[0]



known_face_encodings = [sid_face_encoding, hrithik_face_encoding, sharukh_face_encoding, salman_face_encoding]
known_face_names = ["Siddharamayya", "Hrithik", "Shah Rukh Khan", "Salman Khan"]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

def gen_frames():
    global process_this_frame
    while True:
        success, frame = video_capture.read()
        if not success:
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 5)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (139, 128, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    # Load image previews for the gallery
    images = os.listdir(CAPTURED_IMAGES_DIR)
    image_paths = [f"{CAPTURED_IMAGES_DIR}/{img}" for img in images]
    return render_template('index.html', images=image_paths)

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture_image')
def capture_image():
    success, frame = video_capture.read()
    if success:
        # Save captured image
        image_path = os.path.join(CAPTURED_IMAGES_DIR, f"captured_{len(os.listdir(CAPTURED_IMAGES_DIR)) + 1}.jpg")
        cv2.imwrite(image_path, frame)
        return jsonify({"status": "success", "image": image_path})
    return jsonify({"status": "failed"})

@app.route('/delete_image', methods=['POST'])
def delete_image():
    image_path = request.json.get('image_path')
    if os.path.exists(image_path):
        os.remove(image_path)
        return jsonify({"status": "success"})
    return jsonify({"status": "failed", "message": "Image not found"})

if __name__ == '__main__':
    app.run(debug=True)