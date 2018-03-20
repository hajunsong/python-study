import cv2
import numpy as np


def edit_text():
    input_image = np.ones((80, 100, 3), np.uint8)
    text_list = []
    text = ""
    font_face = cv2.FONT_HERSHEY_COMPLEX
    font_size = 1.5
    font_color = (255, 255, 255)
    line_color = (0, 0, 0)
    color_count = 0
    cursor_pos = [(0, 0), (0, 0)]
    zone_id = []
    quit_flag = False
    while quit_flag is not True:
        image = np.copy(input_image)
        key = cv2.waitKey(1)
        if key != -1:
            print 'int = {}, char = {}'.format(key, str(unichr(key)))
            if 48 <= key <= 57:
                text_list.append(str(unichr(key)))
        if key == 8:  # Backspace:
            if 1 <= len(text_list):
                text_list.pop(-1)

        for txt in text_list:
            text = text + txt
        cv2.putText(image, text, (0, 50), font_face, font_size, font_color)
        text_size = cv2.getTextSize(text, font_face, font_size, 1)[0]
        print text_size
        cursor_pos[0] = (text_size[0], 50 - text_size[1])
        cursor_pos[1] = (text_size[0], 50)
        cv2.line(image, cursor_pos[0], cursor_pos[1], line_color, 3)

        if key == ord('\r'):  # Enter
            zone_id.append(text)
            text_list = []

        text = ""
        color_count += 1
        if color_count > 100:
            if line_color == (255, 255, 255):
                line_color = (0, 0, 0)
            else:
                line_color = (255, 255, 255)
            color_count = 0

        if key == ord('q'):
            quit_flag = True
        cv2.imshow("", image)

    print zone_id

if __name__ == '__main__':
    edit_text()
