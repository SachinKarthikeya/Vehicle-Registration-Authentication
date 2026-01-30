## 🚘 Vehicle Registration Authentication

A authorization-based project, which verifies a vehicle's number plate registration details with the database to approve or deny entry into any premises along with recording the entry time.
This project enhances security measures by allowing only authorized vehicles to enter the premises.

## 🚀 Features
- **YOLOv8**: Locates the number plate on a vehicle through Webcam/CCTV
- **PaddleOCR**: Extracts registration text from the number plate 
- **XAMPP MySQL**: Matches the extracted text with the database 
- **OpenPyXL**: Automatically logs the vehicle's entry time in Excel sheet
- **Streamlit**: Interactive dashboard for displaying live footage

## 📄 Workflow
- The Webcam/CCTV camera is presented live on the Streamlit dashboard
- YOLOv8 actively locates the number plate on the vehicle
- Once located, PaddleOCR extracts the text from the number plate
- The extracted text is matched with the MySQL database of registered vehicles for verification
- Once the registration matches, the vehicle is approved for entry. If not, it is denied of entry
- Logs the approved vehicle details with time of entry in Excel sheet

## 🧰 Tech Stack
- **Frontend**: Streamlit
- **Backend**: OpenCV, PaddleOCR, Openpyxl
- **Object Detection Model**: YOLOv8
- **Database**: XAMPP (MySQL)

## 📢 Future Improvements

- Send real-time notifications during vehicle entry
- Extend the YOLO model to classify the type of vehicle during entry
- Validate detected license plates with government databases for more secured authorization
- Registers a new vehicle from Streamlit into the database 
