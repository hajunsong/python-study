# -*- coding: utf-8 -*-
import cv2


def face_detect_mosaic():
    video_name = 'demo_video.mp4'

    cap = cv2.VideoCapture(video_name)
    ret, image = cap.read()

    cascade_file = "haarcascade_frontalface_alt.xml"
    mosaic_rate = 5

    while ret:
        ret, image = cap.read()

        image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cascade = cv2.CascadeClassifier(cascade_file)
        face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(20, 20))

        if len(face_list) == 0:
            print "no face"
        # 확인한 부분에 모자이크 걸기 -- (※4)

        for (x, y, w, h) in face_list:
            # 얼굴 부분 자르기 --- (※5)
            face_img = image[y:y + h, x:x + w]
            # 자른 이미지를 지정한 배율로 확대/축소하기 --- (※6)
            face_img = cv2.resize(face_img, (w // mosaic_rate, h // mosaic_rate))
            # 확대/축소한 그림을 원래 크기로 돌리기 --- (※7)
            face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)
            # 원래 이미지에 붙이기 --- (※8)
            image[y:y + h, x:x + w] = face_img

        # 렌더링 결과를 파일에 출력
        cv2.imshow("mosaic", image)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break

    print 'end'

if __name__ == '__main__':
    face_detect_mosaic()