from ultralytics import YOLO

model = YOLO("model/best.pt")

# Object Detection
results = model.predict(source="input_videos/video.mp4", save=True)

# Tracking
# results = model.track(source = "input_videos/video.mp4", save=True, persist=True)