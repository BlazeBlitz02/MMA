# load teh video
# split it into frames
# proses each frame

import cv2


def show_image(image, title="debug"):
    cv2.imshow(title, image)
    if cv2.waitKey(0):
        return


def adjust_frame(image):
    # resize -- maybe later we can pass the wanted size as an argument
    # (width, height)
    new_size = (int(image.shape[1] / 4), int(image.shape[0] / 4))
    resized_image = cv2.resize(image, new_size)
    show_image(resized_image)

    # convert to grayscale
    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    show_image(gray)

    # blur image
    blurred_frame = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred_frame


def frame_capture():
    print("start")

    # give this as arguments
    file_path = "dev_video.mp4"
    sample_frequency = 1

    # open the video
    video = cv2.VideoCapture(file_path)
    if not video.isOpened():
        print("error opening file: " + file_path)

    # split into frames
    frames = []
    total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    count = 0
    frame_sample_frequency = int(video.get(cv2.CAP_PROP_FPS) / sample_frequency)
    for frame_index in range(0, int(total_frames), frame_sample_frequency):
        video.set(1, frame_index)
        is_successful, frame = video.read()
        if is_successful:
            count += 1
            processed_frame = adjust_frame(frame)
            frames.append(processed_frame)
            show_image(processed_frame)

    print("frame total", count)
    print("end")


frame_capture()