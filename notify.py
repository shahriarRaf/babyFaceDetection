import os
import cv2
import firebase_admin
from firebase_admin import credentials, messaging, db
from ultralytics import YOLO

BASE = os.path.dirname(__file__)
cred_path = os.path.join(BASE, "service-account.json")
print("Using credentials:", cred_path)

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://childpresence-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

model = YOLO(os.path.join(BASE, "baby_detect", "baby_detect", "weights", "best.pt"))
cap = cv2.VideoCapture(0)

def write_counts(babies, adults):
    ref = db.reference("detection")
    ref.set({'babies': babies, 'adults': adults})
    print("Wrote to DB:", babies, adults)

def maybe_alert(babies, adults):
    write_counts(babies, adults)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    results = model.predict(frame, stream=False, verbose=False)
    result = results[0]

    # Extract boxes, scores, and class ids
    boxes = result.boxes.cpu().numpy()
    class_ids = result.boxes.cls.cpu().numpy().astype(int)
    scores = result.boxes.conf.cpu().numpy()

    babies = adults = 0

    # Draw boxes and labels on the frame
    for box, cls_id, score in zip(boxes, class_ids, scores):
        # Box format: [x1, y1, x2, y2]
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        label = f"{model.names[cls_id]}: {score:.2f}"

        # Count babies and adults
        if model.names[cls_id].lower() in ['baby', 'child']:
            babies += 1
        elif model.names[cls_id].lower() == 'adult':
            adults += 1

        # Draw rectangle
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Put label above the rectangle
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    print("Detect:", babies, adults)
    maybe_alert(babies, adults)

    cv2.imshow("YOLOv8 Baby Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




