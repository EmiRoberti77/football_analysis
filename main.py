from utils.video_utils import read_video, save_video
from trackers.tracker import Tracker

VIDEO_INPUT = 'input_videos/video.mp4'
VIDEO_OUTPUT = 'output_videos/output.mp4'
MODEL_PATH = 'model/best.pt'
__MAIN__ = "__main__"

def main():
  print(VIDEO_INPUT)
  video_frames = read_video(VIDEO_INPUT)
  tracker = Tracker(MODEL_PATH)
  tracks = tracker.get_object_tracks(video_frames, read_from_stub=False, stub_path="tracker_stub/player_detection.pkl")
  output_video_frames = tracker.draw_annotations(video_frames, tracks)
  save_video(output_video_frames, VIDEO_OUTPUT)
  print(VIDEO_OUTPUT)


if __name__ == __MAIN__:
  main()
