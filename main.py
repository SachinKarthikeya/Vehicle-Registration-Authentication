import cv2
import streamlit as st
from paddleocr import PaddleOCR
from ultralytics import YOLO
from openpyxl import Workbook
from datetime import datetime
import mysql.connector

# Initialize PaddleOCR and YOLO
ocr = PaddleOCR(use_angle_cls=True, lang='en')
model = YOLO('/Users/sachinkarthikeya/Desktop/Projects/VRA-YOLO/best.pt')

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="VehicleDB"
)

# Workbook setup for logging
workbook = Workbook()
sheet = workbook.active
sheet.append(["Time", "Vehicle Number", "Status"])

def extract_text(image):
    results = ocr.ocr(image, cls=True)
    if results and results[0]:
        return results[0][0][1][0]
    return None

def authorization(plate_number):
    cursor = db.cursor()
    query = "SELECT plate_number FROM authorized_plates WHERE plate_number = %s"
    cursor.execute(query, (plate_number,))
    return cursor.fetchone() is not None

def log_entry(plate_number, status):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append([time, plate_number, status])
    workbook.save("vehicle_entry_log.xlsx")

# Streamlit UI
st.title("Vehicle Recognition System")
start_camera = st.button("Start Camera")
stop_camera = st.button("Stop Camera")

if start_camera:
    st.text("Starting live camera feed...")
    cap = cv2.VideoCapture(0)

    frame_placeholder = st.empty()
    terminate_program = False

    try:
        while not terminate_program:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to access the webcam.")
                break

            results = model(frame)
            for result in results:
                for box in result.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    cropped_plate = frame[y1:y2, x1:x2]
                    plate_text = extract_text(cropped_plate)

                    if plate_text:
                        if authorization(plate_text):
                            log_entry(plate_text, "Approved")
                            st.success(f"Entry Approved: {plate_text}")
                            terminate_program = True  # Terminate on approval
                            break
                        else:
                            log_entry(plate_text, "Denied")
                            st.error(f"Entry Denied: {plate_text}")

            frame_placeholder.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")

            if stop_camera:
                terminate_program = True

    except Exception as e:
        st.error(f"An error occurred: {e}")

    finally:
        cap.release()
        db.close()
        st.text("Camera feed stopped. Resources released.")