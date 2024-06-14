# Import necessary libraries
import cv2  # OpenCV for image processing
import mediapipe as mp  # Mediapipe for hand tracking
import pyautogui  # PyAutoGUI for simulating keyboard presses
import time  # Time for time-related operations

# Function to count fingers based on landmark positions
def count_fingers(lst):
    cnt = 0  # Initialize finger count

    # Calculate threshold based on hand landmarks
    thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

    # Check each finger's position relative to the threshold
    if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:
        cnt += 1
    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
        cnt += 1
    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
        cnt += 1
    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
        cnt += 1
    if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:
        cnt += 1

    return cnt  # Return finger count

# Open video capture device
cap = cv2.VideoCapture(0)

# Initialize Mediapipe hand tracking and drawing utilities
drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)

# Initialize variables
start_init = False  # Flag to indicate the start of hand gesture
prev = -1  # Previous finger count

# Main loop for real-time hand gesture recognition
while True:
    end_time = time.time()  # Record current time
    _, frm = cap.read()  # Read frame from video capture
    frm = cv2.flip(frm, 1)  # Flip the frame horizontally (mirror effect)

    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))  # Process frame for hand landmarks

    # If hand landmarks detected
    if res.multi_hand_landmarks:
        hand_keyPoints = res.multi_hand_landmarks[0]  # Get landmarks for the first detected hand

        cnt = count_fingers(hand_keyPoints)  # Count fingers based on landmarks

        # Check for change in finger count
        if not (prev == cnt):
            # If finger count changes and initial time is not set
            if not (start_init):
                start_time = time.time()  # Record start time
                start_init = True  # Set initial flag to True

            # If time since last gesture is greater than 0.2 seconds
            elif (end_time - start_time) > 0.2:
                # Simulate keyboard presses based on finger count
                if (cnt == 1):
                    pyautogui.press("right")
                elif (cnt == 2):
                    pyautogui.press("left")
                elif (cnt == 3):
                    pyautogui.press("up")
                elif (cnt == 4):
                    pyautogui.press("down")
                elif (cnt == 5):
                    pyautogui.press("space")

                prev = cnt  # Update previous finger count
                start_init = False  # Reset initial flag

        # Draw hand landmarks and connections on the frame
        drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

    cv2.imshow("window", frm)  # Display processed frame

    # Check for Esc key press to exit
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()  # Close all OpenCV windows
        cap.release()  # Release video capture device
        break  # Exit the loop