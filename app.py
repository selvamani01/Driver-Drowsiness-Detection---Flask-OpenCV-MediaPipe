from flask import Flask, render_template, Response
import cv2
import mediapipe as mp
import winsound
from utils import eye_aspect_ratio
import threading

app = Flask(__name__)

# MediaPipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True
)

# Camera (Initialize ONCE globally)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

EAR_THRESHOLD = 0.25
FRAME_LIMIT = 20
counter = 0

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]


def beep():
    winsound.Beep(2500, 800)


def generate_frames():
    global counter

    while True:
        success, frame = cap.read()
        if not success:
            print("Camera read failed")
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                h, w, _ = frame.shape

                left_eye, right_eye = [], []

                for idx in LEFT_EYE:
                    x = int(face_landmarks.landmark[idx].x * w)
                    y = int(face_landmarks.landmark[idx].y * h)
                    left_eye.append((x, y))

                for idx in RIGHT_EYE:
                    x = int(face_landmarks.landmark[idx].x * w)
                    y = int(face_landmarks.landmark[idx].y * h)
                    right_eye.append((x, y))

                # EAR Calculation
                leftEAR = eye_aspect_ratio(left_eye)
                rightEAR = eye_aspect_ratio(right_eye)
                ear = (leftEAR + rightEAR) / 2.0

                cv2.putText(frame, f"EAR: {ear:.2f}", (20, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                # Drowsiness Detection
                if ear < EAR_THRESHOLD:
                    counter += 1
                    if counter >= FRAME_LIMIT:
                        cv2.putText(frame, "DROWSINESS ALERT!", (50, 100),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

                        # Non-blocking beep
                        threading.Thread(target=beep, daemon=True).start()
                else:
                    counter = 0

        # Encode frame for browser
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    # IMPORTANT: disable reloader to avoid camera opening twice
    app.run(debug=True, use_reloader=False)