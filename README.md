## Vehicle Registration Authentication

A authorization-based project, which verifies a vehicle's number plate registration details with the database to approve or deny entry into any premises along with recording the entry time.
This project enhances security measures by allowing only authorized vehicles to enter the premises.

## Features 
- Locates the number plate on a vehicle with a camera using YOLOv8
- Extracts the registration text from the number plate using PaddleOCR
- Matches the extracted text with the database which has authorized vehicle registrations for verification
- If registration matched, vehicle is approved for entry. If not matched, vehicle is denied for entry
- Automatically logs the vehicle's entry time in Excel sheet

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: PaddleOCR, Openpyxl
- **Object Detection Model**: Yolov8
- **Database**: XAMPP (MySQL)

## Future Enhancements

- Send real-time notifications during vehicle entry
- Extending the YOLO model to classify the type of vehicle during entry
- Validate detected license plates with government databases for more secured authorization
- Store all vehicle data and logs in the cloud for remote access and monitoring.
