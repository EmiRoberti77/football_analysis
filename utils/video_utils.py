import cv2

def read_video(video_path):
  """
    Extract all the frames from the video file and saves them
    into a frame[]

    return: frames[]
  """
  cap = cv2.VideoCapture(video_path)
  frames = []
  while True:
    ret, frame = cap.read()
    if not ret:
      break
    frames.append(frame)
  return frames


# def save_video(output_video_frames, output_video_path):
#   """
#     Save the frames into a XVID avi fie
#   """
#   if not output_video_frames:
#     raise ValueError("No frames provided")
  
#   print(f"frame buffer len:{len(output_video_frames)}")
#   # set video codec
#   fourcc = cv2.VideoWriter_fourcc(*'XVID')
#   # set the writer
#   height, width = output_video_frames[0].shape[:2]
#   print(f"saving video frame height:{height}, width:{width}")
#   out = cv2.VideoWriter(output_video_path, fourcc, 24, (height, width))
#   # iterate through the frames
#   for frame in output_video_frames:
#     # save the frame
#     out.write(frame)
#   # release the writer to clean up the resources
#   out.release()


def save_video(output_video_frames, output_video_path,):
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    out.release()
  

