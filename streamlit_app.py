
# Step 1: Import Libraries
import cv2
import mediapipe as mp
import streamlit as st
# Step 2: Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
# Step 3: Initialize Video Capture
cap = cv2.VideoCapture(0)
# Step 4: Capture and Process Each Frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Initialize list to store landmark coordinates
            landmark_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                # Get the coordinates
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmark_list.append([cx, cy])
            # Gesture recognition logic
            if len(landmark_list) != 0:
                # Example logic for gesture recognition
                # Open Hand (Palm) Gesture
                if landmark_list[4][1] < landmark_list[3][1] and landmark_list[8][1] < landmark_list[6][1]:
                    gesture = "Welcome to Gesture Recognition Project"
                # Pointing Up Gesture
                elif landmark_list[4][1] > landmark_list[3][1] and landmark_list[8][1] < landmark_list[6][1]:
                    gesture = "Hello This is Chaitanya"
                else:
                    gesture = None
                # Display the corresponding text
                if gesture:
                    cv2.putText(frame, gesture, (landmark_list[0][0] - 50, landmark_list[0][1] - 50),cv2.FONT_HERSHEY_SIMPLEX, 2,(0, 255, 0), 3, cv2.LINE_AA)  # Increased fontScale and thickness
    # Step 5: Display the Frame
    cv2.imshow('Hand Gesture Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 6: Release Resources
cap.release()
cv2.destroyAllWindows()
