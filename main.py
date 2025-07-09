from utils.video_utils import read_video, save_video

VIDEO_INPUT = 'input_videos/video.mp4'
VIDEO_OUTPUT = 'output_videos/output.mp4'
__MAIN__ = "__main__"

def main():
  print(VIDEO_INPUT)
  video_frames = read_video(VIDEO_INPUT)
  save_video(video_frames, VIDEO_OUTPUT)
  print(VIDEO_OUTPUT)




if __name__ == __MAIN__:
  main()
