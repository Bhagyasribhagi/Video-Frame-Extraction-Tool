import cv2

video = cv2.VideoCapture("video1.mp4") 
numberof_frames = video.get(cv2.CAP_PROP_FRAME_COUNT) 
print(numberof_frames)
frame_ps = video.get(cv2.CAP_PROP_FPS) 
print(frame_ps)
timestamp =input("Enter timestamp in the form of 00:00:00: ")

timestamp_list = timestamp.split(":") 
timestamp_list_floats = [float(i) for i in timestamp_list]
print(timestamp_list_floats)
hours, minutes, seconds = timestamp_list_floats
frame_nr = hours * 3600 * frame_ps + minutes * 60 * frame_ps + seconds * frame_ps

video.set(cv2.CAP_PROP_POS_FRAMES, frame_nr)
success, frame = video.read()
print(success)
if success:   
    cv2.imwrite(f'Frame at {hours}_{minutes}_{seconds}_cv2.jpg', frame)
else:
    print("Frame is not found")

video.release()


