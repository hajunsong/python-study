import requests
import json


def transmit_server():
    data = {}
    data['cpass'] = '13EAQR38TPE88291BNQI'
    data['datetime'] = '2018-03-19 17:00:00'
    data['rono'] = '507'
    data['personCnt'] = '0'
    data['imgName'] = '507_2018-03-19 12:24:25_in.png'

    transmit_list = []
    transmit_list.append(data)

    data = {}
    data["pinoutlist"] = transmit_list

    result = json.dumps(data)

    url = 'http://dz1.doongzi.co.kr/pinout/api/personInOutList_insert.do' + '?pinoutlist=' + result

    request = requests.post(url)

    # if res == '\r\n\r\nres : 0\r\n':
    # if int(request.content.split('\r\n')[2].split('res : ')[1]) == 0:
    #     gv.transmit_list = []
    response = request.content.splitlines()
    indx = response.index('res : 0')

    print response


if __name__ == '__main__':
    transmit_server()
