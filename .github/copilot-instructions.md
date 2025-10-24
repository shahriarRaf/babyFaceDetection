## babyFaceDetection — Copilot instructions

Short, actionable notes to help an AI agent be productive working in this repo.

1) Big picture
- This repo trains and runs an Ultralytics/YOLO model to detect "baby/child" vs "adult" from camera frames.
- Major entry points:
  - `main.py` — simple local webcam inference that draws boxes and labels (no cloud integration).
  - `notify.py` — similar to `main.py` but additionally writes baby/adult counts to a Firebase Realtime Database using `service-account.json`.
  - `baby_detect/args.yaml` — canonical training parameters used by the author (model name, data, epochs, imgsz, etc.).
- Trained weights live under `baby_detect/weights/` (e.g. `best.pt`, `last.pt`). `main.py` and `notify.py` reference `baby_detect/baby_detect/weights/best.pt` — note the duplicated `baby_detect/baby_detect` path in code.

2) How to run (inference)
- Install minimal deps (use your venv):
  pip install ultralytics opencv-python firebase-admin
- Local webcam demo (draw boxes):
  python main.py
- Firebase-enabled demo (writes counts to RTDB):
  - Ensure `service-account.json` is present and points to a valid Firebase service account.
  - Then run: python notify.py
- Notes:
  - Both scripts open the default camera (index 0) and exit on pressing `q`.
  - If weights are at `baby_detect/weights/best.pt`, either update the model path in code or place a copy under the path used in code (`baby_detect/baby_detect/weights/best.pt`).

3) How to train
- Data layout follows standard YOLO format. See top-level `data.yaml` and folders: `train/ images & labels`, `valid/`, `test/`.
- The project uses Ultralytics' CLI/API. The repository includes a canonical `baby_detect/args.yaml` describing training params. Example train command (uses Ultralytics `yolo` CLI):
  yolo task=detect mode=train model=yolo11n.pt data=data.yaml epochs=150 batch=16 imgsz=640 project=baby_detect name=baby_detect exist_ok=True
- Alternatively, adapt `baby_detect/args.yaml` into the CLI or API call. Key settings to preserve: seed=0, deterministic=true, imgsz=640, batch=16, epochs=150.

4) Important patterns & conventions (project-specific)
- Model path duplication: code references `baby_detect/baby_detect/weights/...`. Search-and-replace or symlink may be necessary when moving weights.
- `baby_detect/args.yaml` is the authoritative training config. Prefer editing it (or passing equivalent CLI args) instead of editing training scripts.
- The code relies on Ultralytics `YOLO(...)` object and uses `result.boxes` -> `.cls`, `.conf`, `.xyxy` arrays. When generating examples, follow that API (see `main.py` and `notify.py`).

5) Integration points / sensitive files
- `service-account.json` — Firebase service account used by `notify.py`. Keep it secret. `notify.py` initializes Firebase and writes to the RTDB at the URL hardcoded in the file.
- `google-services.json` and other Google files are present but unused by the local demo scripts; examine if you add mobile/other integrations.

6) Common tasks an agent may be asked to do (examples + quick hints)
- Replace model path: update `YOLO(".../weights/best.pt")` in `main.py` and `notify.py` or create the expected subfolder and copy/move weights.
- Add CLI flags: follow patterns in `args.yaml` for parameter names and expected value types.
- Update training params: change `baby_detect/args.yaml` and run the `yolo` CLI; do not hardcode values in scripts.
- Add unit tests: there are no test harnesses — prefer small smoke tests that load the model and run inference on a single image from `test/images/`.

7) Files to reference when coding
- `main.py` — inference example
- `notify.py` — Firebase integration + inference + count logic
- `baby_detect/args.yaml` — training parameters
- `data.yaml` — dataset mapping and class names
- `baby_detect/weights/` — trained weights (best.pt, last.pt)
- `test/` and `train/`/`valid/` — sample images and labels (YOLO format)

8) Safety & verification notes
- Do not commit `service-account.json` or other credentials; they are sensitive. If you need to test cloud code, use a throwaway Firebase account and never publish keys.
- When changing inference loops, keep the `q` keypress exit and `cap.release()` / `cv2.destroyAllWindows()` cleanups.

If anything here looks wrong or you want more detail (e.g., a sample smoke test, or a recommended requirements.txt), tell me which section and I'll iterate.
