import cv2
from ultralytics import YOLO

# Load your trained YOLOv8 model
model = YOLO("baby_detect/baby_detect/weights/best.pt")

# Open webcam (0 is the default webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Run YOLO inference on the frame
    results = model.predict(frame, stream=False, verbose=False)

    # results is a list of Results; get the first (and only) element
    result = results[0]

    # Extract boxes, scores, and class ids
    boxes = result.boxes.cpu().numpy()  # Boxes object -> numpy array
    class_ids = result.boxes.cls.cpu().numpy().astype(int)
    scores = result.boxes.conf.cpu().numpy()

    # Draw boxes and labels on the frame
    for box, cls_id, score in zip(boxes, class_ids, scores):
        # Box format: [x1, y1, x2, y2]
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        label = f"{model.names[cls_id]}: {score:.2f}"

        # Draw rectangle
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Put label above the rectangle
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("YOLOv8 Baby Detector", frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release and close windows
cap.release()
cv2.destroyAllWindows()
