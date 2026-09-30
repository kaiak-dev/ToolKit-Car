import cv2
import RPi.GPIO as GPIO
from ultralytics import YOLOE
import numpy as np

model = YOLOE("yoloe-26n-seg.pt")  # load an official segmentation model
names = ["person"]
model.set_classes(names, model.get_text_pe(names))

vertical_PWM = 12
vertical_IN1 = 11
vertical_IN2 = 13

horizontal_PWM = 33
horizontal_IN1 = 15
horizontal_IN2 = 16

height, width = 480, 640
DEADZONE = 50
window_center_x = width // 2
window_center_y = height // 2

# --- INITIALIZE MOTOR HARDWARE ---
GPIO.setmode(GPIO.BCM)

# Setup Vertical & Horizontal tracking pins
pins = [vertical_PWM, vertical_IN1, vertical_IN2, horizontal_PWM, horizontal_IN1, horizontal_IN2]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

# Start PWM for both tracking motors
pwm_vertical = GPIO.PWM(vertical_PWM, 1000)
pwm_horizontal = GPIO.PWM(horizontal_PWM, 1000)
pwm_vertical.start(0)
pwm_horizontal.start(0)


def set_tracking_motors(v_speed, h_speed):
    """Maps speeds (-100 to 100) directly to vertical and horizontal tracking motors"""
    # Vertical Motor Control
    if v_speed >= 0:
        GPIO.output(vertical_IN1, GPIO.HIGH)
        GPIO.output(vertical_IN2, GPIO.LOW)
    else:
        GPIO.output(vertical_IN1, GPIO.LOW)
        GPIO.output(vertical_IN2, GPIO.HIGH)
        v_speed = abs(v_speed)

    # Horizontal Motor Control
    if h_speed >= 0:
        GPIO.output(horizontal_IN1, GPIO.HIGH)
        GPIO.output(horizontal_IN2, GPIO.LOW)
    else:
        GPIO.output(horizontal_IN1, GPIO.LOW)
        GPIO.output(horizontal_IN2, GPIO.HIGH)
        h_speed = abs(h_speed)

    # Constraint to valid duty cycle limits
    v_speed = int(np.clip(v_speed, 0, 100))
    h_speed = int(np.clip(h_speed, 0, 100))

    pwm_vertical.ChangeDutyCycle(v_speed)
    pwm_horizontal.ChangeDutyCycle(h_speed)


try:
    results = model(source="0", conf=0.3, tracker="bytetrack.yaml", stream=True)

    # Main video streaming loop (Everything below here is indented cleanly)
    for result in results:
        boxes = result.boxes
        frame = result.orig_img.copy()

        # Check if boxes list has elements
        if len(boxes) > 0:
            # Check if boxes list has elements
            if len(boxes) > 0:
                # 1. Convert the data tensor to a clean numpy matrix
                box_matrix = boxes.xywh.cpu().numpy()  # matrix shape: (N, 4)

                # 2. Extract row 0 (the first detected person)
                first_box = box_matrix[0]  # array shape: (4,)

                # 3. Pull out the distinct center coordinates safely
                x_center = int(first_box[0])
                y_center = int(first_box[1])

                relative_x = x_center - window_center_x
                relative_y = y_center - window_center_y

        else:
            x_center = window_center_x
            y_center = window_center_y
            relative_x = 0
            relative_y = 0

        # --- MOTOR ACTION LOGIC (Using DEADZONE) ---
        # If displacement is larger than DEADZONE, calculate scaling, else stay still.
        # Proportional multiplier (0.3) scales pixel error down to a 0-100 speed value.

        if abs(relative_y) > DEADZONE:
            vertical_motor_speed = relative_y * 0.3
        else:
            vertical_motor_speed = 0

        if abs(relative_x) > DEADZONE:
            horizontal_motor_speed = relative_x * 0.3
        else:
            horizontal_motor_speed = 0

        # Send calculated values directly to the motors
        set_tracking_motors(vertical_motor_speed, horizontal_motor_speed)

        # Draw target circle on the current frame
        cv2.circle(frame, (window_center_x, window_center_y), 10, (0, 0, 255), 2)
        cv2.circle(frame, (x_center, y_center), 10, (0, 0, 225), 2)

        # Update GUI window display
        cv2.imshow("predict", frame)

        # Wait 1 millisecond per frame so the video runs smoothly
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Safely stop PWM instances and release pins
    pwm_vertical.stop()
    pwm_horizontal.stop()
    GPIO.cleanup()
    cv2.destroyAllWindows()
    print("exit")
