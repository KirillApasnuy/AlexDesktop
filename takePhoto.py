import cv2
import os

def take_screenshot_from_cam():
    cap = cv2.VideoCapture(0)
    count = 0

    if not os.path.exists("dataset_from_cam"):
        os.mkdir("dataset_from_cam")

    while True:
        fps = cap.get(cv2.CAP_PROP_FPS)
        multiplier = fps * 3
        # print(fps)
        ret, frame = cap.read()

        if ret:
            frame_id = int(round(cap.get(1)))
            # print(frame_id)
            cv2.imshow("frame", frame)
            k = cv2.waitKey(20)

            if k == ord(" "):
                cv2.imwrite(f"dataset_from_cam/{count}.jpg", frame)
                count += 1

            elif k == ord("q") or count == 5:
                break

    cap.release()
    cv2.destroyAllWindows()
