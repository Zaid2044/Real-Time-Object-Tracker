# tracker.py

import cv2
from ultralytics import YOLO

print("Loading YOLOv8 model...")
model = YOLO('yolov8n.pt')
print("Model loaded successfully!")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Webcam started. Press 'q' to quit.")
print("Objects Detected:")

tracked_ids = set()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.track(frame, persist=True, verbose=False)

    if results[0].boxes.id is not None:
        
        track_ids = results[0].boxes.id.int().cpu().tolist()
        class_ids = results[0].boxes.cls.int().cpu().tolist()
        
        for track_id, class_id in zip(track_ids, class_ids):
            
            if track_id not in tracked_ids:
                tracked_ids.add(track_id)
                class_name = model.names[class_id]
                print(f"--> New object detected: {class_name} (ID: {track_id})")

    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 Real-Time Object Tracker", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
print("\n--- Summary of all tracked objects ---")
print(f"Total unique objects tracked: {len(tracked_ids)}")
print(f"Tracked IDs: {sorted(list(tracked_ids))}")
print("Program terminated.")