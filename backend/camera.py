import cv2
import threading
import time
import os

camera_running = False
camera_thread = None

camera_status = {
    "camera_open": False,
    "face": False,
    "multiple_faces": False,
    "face_count": 0,
    "frames": 0,
    "left_camera_count": 0,
    "reference_saved": False,
    "reference_image": ""
}


def camera_loop():

    global camera_running

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        camera_status["camera_open"] = False
        return

    camera_status["camera_open"] = True

    detector = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    os.makedirs("recordings", exist_ok=True)

    while camera_running:

        success, frame = cap.read()

        if not success:
            time.sleep(0.2)
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(80, 80)
        )

        camera_status["frames"] += 1
        camera_status["face_count"] = len(faces)

        # -----------------------------
        # Exactly one face
        # -----------------------------
        if len(faces) == 1:

            camera_status["face"] = True
            camera_status["multiple_faces"] = False

            if not camera_status["reference_saved"]:

                image_path = "recordings/reference.jpg"

                cv2.imwrite(image_path, frame)

                camera_status["reference_saved"] = True
                camera_status["reference_image"] = image_path

        # -----------------------------
        # Multiple faces
        # -----------------------------
        elif len(faces) > 1:

            camera_status["face"] = True
            camera_status["multiple_faces"] = True

        # -----------------------------
        # No face
        # -----------------------------
        else:

            camera_status["face"] = False
            camera_status["multiple_faces"] = False
            camera_status["left_camera_count"] += 1

        time.sleep(0.25)

    cap.release()

    camera_status["camera_open"] = False


def start_camera():

    global camera_running
    global camera_thread

    if camera_running:
        return

    camera_running = True

    camera_thread = threading.Thread(
        target=camera_loop,
        daemon=True
    )

    camera_thread.start()


def stop_camera():

    global camera_running

    camera_running = False


def get_camera_status():

    return camera_status