import json
import os
cur_path = os.path.abspath(os.path.dirname(__file__))


def json_read_write():
    ip = '168.188.117.160:8000'
    video_path = '/home/kpst/hajun/Deformable-ConvNets/guest_counter/data'
    video_name = 'demo_video.mp4'

    data = {}
    data['IP ADDRESS'] = ip
    data['VIDEO PATH'] = video_path
    data['VIDEO NAME'] = video_name

    with open(cur_path + '/test_file.txt', 'w') as outfile:
        json.dump(data, outfile)

    with open('test_file.txt') as infile:
        data = json.load(infile)
        ip_in = data['IP ADDRESS']
        video_path_in = data['VIDEO PATH']
        video_name_in = data['VIDEO NAME']

        print ip_in
        print video_path_in
        print video_name_in

if __name__ == '__main__':
    json_read_write()
