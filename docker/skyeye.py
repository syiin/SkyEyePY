from openalpr import Alpr
import numpy as np
import cv2
import faulthandler


RTSP_SOURCE = "rtsp://admin:password@192.168.0.2:8554/profile0"
FRAME_SKIP = 15

def main():

    faulthandler.enable()

    alpr = Alpr("eu", "/usr/share/openalpr/config/openalpr.conf.user", "/usr/share/openalpr/runtime_data/")
    if not alpr.is_loaded():
        print("Error loading OpenALPR")
        sys.exit(1)
        
    alpr.set_top_n(3)
    # alpr.set_default_region("md")

    #Capture video data
    videoData = cv2.VideoCapture(RTSP_SOURCE)

    _frameNumber = 0

    while(videoData.isOpened()):
        # Capture frame-by-frame
        ret, frame = videoData.read()
        
        _frameNumber += 1
        if _frameNumber % FRAME_SKIP != 0:
            continue

        # Our operations on the frame come here
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # frame = cv2.transpose(frame)
        # frame = cv2.flip(frame, 1)

        # Display the resulting frame
        cv2.imshow('Open ALPR Test',frame)
        # results = alpr.recognize_array(frame.tobytes('C'))
        # print(results)
        print(frame)
        results = alpr.recognize_ndarray(frame)
        # print(frame.size)
        # print(_frameNumber)

        for i, plate in enumerate(results['results']):
            print('Recognising')
            best_candidate = plate['candidates'][0]
            print('Plate #{}: {:7s} ({:.2f}%)'.format(i, best_candidate['plate'].upper(), best_candidate['confidence']))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    videoData.release()
    cv2.destroyAllWindows()
    # Call when completely done to release memory
    alpr.unload()

if __name__ == "__main__":
    main()







# i = 0
# for plate in results['results']:
#     i += 1
#     print("Plate #%d" % i)
#     print("   %12s %12s" % ("Plate", "Confidence"))
#     for candidate in plate['candidates']:
#         prefix = "-"
#         if candidate['matches_template']:
#             prefix = "*"

#         print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))

# Call when completely done to release memory
# alpr.unload()

#rtsp://192.168.0.3:8554/profile0
#username: admin, password: password