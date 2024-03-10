# import cv2
# import numpy as np
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
# import threading

# # Set up your email and password (use an App Password if you have 2-factor authentication enabled)
# email_address = "adnanjawaad100@gmail.com"
# email_password = "wmqx yffp sxqr ivtm"

# # Recipient's email address
# recipient_email = "adnanjawaad99@gmail.com"

# def capture_and_send():
#     # Create the email message
#     msg = MIMEMultipart()
#     msg["From"] = email_address
#     msg["To"] = recipient_email
#     msg["Subject"] = "Webcam Image Example"

#     # Initialize the webcam capture
#     cap = cv2.VideoCapture(0)  # 0 for the default camera; change it as needed

#     # Capture an image from the webcam
#     ret, frame = cap.read()

#     # Check if the image was captured successfully
#     if ret:
#         # Enhance brightness and contrast
#         alpha = 1.2  # Brightness control (1.0 is neutral)
#         beta = 30    # Contrast control
#         enhanced_frame = np.clip(alpha * frame + beta, 0, 255).astype(np.uint8)

#         # Save the enhanced image to a temporary file
#         cv2.imwrite("captured_image.png", enhanced_frame)

#         # Attach the enhanced image to the email
#         image_path = "captured_image.png"
#         with open(image_path, 'rb') as image_file:
#             image = MIMEImage(image_file.read())
#             msg.attach(image)

#         # Create a server connection
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()
#         server.login(email_address, email_password)

#         # Send the email
#         server.sendmail(email_address, recipient_email, msg.as_string())

#         # Close the server connection
#         server.quit()

#         # Release the webcam
#         cap.release()

#     else:
#         print("Failed to capture an image from the webcam.")

#     # Release the webcam even if an error occurred
#     cap.release()

# # Use threading to capture and send the image in the background
# t = threading.Thread(target=capture_and_send)
# t.start()



























import cv2
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import threading
import serial  # Import the pyserial library

# Set up your email and password (use an App Password if you have 2-factor authentication enabled)
email_address = "doraemonhattori5@gmail.com"
email_password = "fogceycdwrgtojkd"

# Recipient's email address
recipient_email = "samiyaprithula@gmail.com"

def capture_and_send():
    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = email_address
    msg["To"] = recipient_email
    msg["Subject"] = "Webcam Image Example"

    # Initialize the webcam capture
    cap = cv2.VideoCapture(0)  # 0 for the default camera; change it as needed

    # Capture an image from the webcam
    ret, frame = cap.read()

    # Check if the image was captured successfully
    if ret:
        # Enhance brightness and contrast
        alpha = 1.2  # Brightness control (1.0 is neutral)
        beta = 30    # Contrast control
        enhanced_frame = np.clip(alpha * frame + beta, 0, 255).astype(np.uint8)

        # Save the enhanced image to a temporary file
        cv2.imwrite("captured_image.png", enhanced_frame)

        # Attach the enhanced image to the email
        image_path = "captured_image.png"
        with open(image_path, 'rb') as image_file:
            image = MIMEImage(image_file.read())
            msg.attach(image)

        # Create a server connection
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_address, email_password)

        # Send the email
        server.sendmail(email_address, recipient_email, msg.as_string())

        # Close the server connection
        server.quit()

        # Release the webcam
        cap.release()

    else:
        print("Failed to capture an image from the webcam.")

    # Release the webcam even if an error occurred
    cap.release()

# Use threading to capture and send the image in the background
t = threading.Thread(target=capture_and_send)
t.start()

# Initialize the serial connection with the Arduino
arduino = serial.Serial('COM3', 9600)  # Adjust the COM port and baud rate accordingly

while True:
    arduino_data = arduino.read().decode('utf-8')
    if arduino_data.strip() == "1":
        # Trigger image capture and email sending
        capture_and_send()
        print("papap")
