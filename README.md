# Detecting Unattended Children in Cars: An Automated Approach

## Overview
This project uses Ultralytics YOLO object detection to classify people in camera frames into two classes:
- **Baby/Child**
- **Adult**

The goal is to support early safety alerts in vehicle-like monitoring scenarios by continuously counting detected children and adults in real time.

## Key Features
- Real-time webcam inference with bounding boxes and confidence scores
- Binary human age-group classification (Baby/Child vs Adult)
- Live class-wise counting logic
- Firebase Realtime Database integration (`notify.py`) for remote monitoring
- Reproducible training setup through `baby_detect/args.yaml`

## Project Outcome (Elaborate)
This project delivers a complete end-to-end computer vision workflow for child-safety monitoring use cases:

1. **A trained detection model is available and usable immediately**
   - The repository includes trained weights in `baby_detect/weights/`.
   - Users can run inference without retraining from scratch.

2. **Real-time detection pipeline is operational**
   - `main.py` captures frames from a webcam, runs YOLO inference, and overlays readable labels and confidence values.
   - This demonstrates practical live deployment behavior rather than only offline evaluation.

3. **Remote event/state visibility is supported**
   - `notify.py` extends local inference by pushing baby/adult counts to Firebase Realtime Database.
   - This enables dashboard, mobile, or alert-system integrations where camera operators are not physically present.

4. **Dataset-to-training-to-inference lifecycle is defined**
   - The repo contains YOLO-style dataset splits (`train/`, `valid/`, `test/`) and `data.yaml` class mapping.
   - Training parameters are centralized in `baby_detect/args.yaml`, making experiments repeatable and easier to tune.

5. **A practical foundation for safety automation is established**
   - The current system can serve as a baseline for unattended-child risk detection workflows.
   - Teams can extend it with temporal rules, occupancy logic, alerts, or hardware-specific deployment.

In short, the outcome is not only a trained model, but a working prototype ecosystem: data, training config, inference scripts, and cloud logging integration.

## Repository Structure
```text
.
├── main.py
├── notify.py
├── data.yaml
├── baby_detect/
│   ├── args.yaml
│   └── weights/
│       ├── best.pt
│       └── last.pt
├── train/
├── valid/
└── test/
```

## Installation
```bash
pip install ultralytics opencv-python firebase-admin
```

## Run Inference
### Local webcam demo
```bash
python main.py
```
- Opens default camera (`0`)
- Draws detections and labels on frames
- Press `q` to quit

### Firebase-enabled demo
```bash
python notify.py
```
- Requires a valid `service-account.json`
- Pushes baby/adult count updates to Firebase Realtime Database
- Press `q` to quit

## Training
You can retrain with Ultralytics CLI using the existing dataset and parameters:
```bash
yolo task=detect mode=train model=yolo11n.pt data=data.yaml epochs=150 batch=16 imgsz=640 project=baby_detect name=baby_detect exist_ok=True
```

## Important Notes
- Keep `service-account.json` private and never commit credentials.
- If your script cannot find weights, confirm the path used in code matches your local `best.pt` location.

## Requirements
- Python 3.8+
- ultralytics
- opencv-python
- firebase-admin

## License
MIT License
<img width="1920" height="1920" alt="val_batch2_pred" src="https://github.com/user-attachments/assets/eb8ddf57-b189-445d-8b8a-2607829087d8" />
<img width="1920" height="1920" alt="val_batch2_labels" src="https://github.com/user-attachments/assets/48e5141e-e6f6-4e4d-bda6-3ff50c018449" />
<img width="1920" height="1920" alt="val_batch1_pred" src="https://github.com/user-attachments/assets/40c966bc-71c4-48c4-8380-0a0e73ba3486" />
<img width="1920" height="1920" alt="val_batch1_labels" src="https://github.com/user-attachments/assets/c56c7a68-7479-4a6b-8135-67f64425c4d2" />
<img width="1920" height="1920" alt="val_batch0_pred" src="https://github.com/user-attachments/assets/bf177b99-7d8a-480b-8d3f-48b2edd4fe0a" />
<img width="1920" height="1920" alt="val_batch0_labels" src="https://github.com/user-attachments/assets/5755149c-e326-4dc8-9a5d-3d8e807b9f1d" />
<img width="1920" height="1920" alt="train_batch13022" src="https://github.com/user-attachments/assets/951de17c-c63a-4c7e-9e34-1f991f5695a7" />
<img width="1920" height="1920" alt="train_batch13021" src="https://github.com/user-attachments/assets/2c267284-0e4c-4668-ab38-8370d24d5a4a" />
<img width="1920" height="1920" alt="train_batch13020" src="https://github.com/user-attachments/assets/2c289631-05d6-49df-a5a8-77c49657d3f5" />
<img width="1920" height="1920" alt="train_batch2" src="https://github.com/user-attachments/assets/f762658d-632a-4b3f-9f5e-1709d2f6017d" />
<img width="1920" height="1920" alt="train_batch1" src="https://github.com/user-attachments/assets/b40cb9ca-2d00-471c-9b3e-5ab6fd2643dc" />
<img width="1920" height="1920" alt="train_batch0" src="https://github.com/user-attachments/assets/2a8efc86-19ed-40ce-bd3e-86859626b50f" />
<img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/bddcc796-bd0b-454e-aa31-eee9507bdf09" />
<img width="1600" height="1600" alt="labels" src="https://github.com/user-attachments/assets/41e0ce9e-ed5b-47b0-aafb-d80986567453" />
<img width="3000" height="2250" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/35532e52-fa1f-490a-8837-7e93415fbf81" />
<img width="3000" height="2250" alt="confusion_matrix" src="https://github.com/user-attachments/assets/5ad62ca1-33a3-4eb3-a992-9a97b76f8239" />
<img width="2250" height="1500" alt="BoxR_curve" src="https://github.com/user-attachments/assets/f25b705b-824d-4fa2-956e-85f841aa3651" />
<img width="2250" height="1500" alt="BoxPR_curve" src="https://github.com/user-attachments/assets/bc8bbb93-3f3e-48e7-b734-333db3faba9b" />
<img width="2250" height="1500" alt="BoxP_curve" src="https://github.com/user-attachments/assets/55d4a666-f84d-4b1b-bf1b-f2b31aac5c2b" />
<img width="2250" height="1500" alt="BoxF1_curve" src="https://github.com/user-attachments/assets/6f4d0f3a-31fb-4ef1-9c5d-60570566d1d7" />

