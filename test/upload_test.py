# -*- coding: utf-8 -*-
"""使用requests上传, 请自行安装"""
import os.path
import zlib

import requests


def test():
    local_prefix = os.path.expanduser('~')
    remote_prefix = '/home/ubuntu'

    file_path = os.path.abspath(__file__)
    print file_path

    zlib_data = zlib.compress(open(file_path, 'rb').read(), 5)
    remote_path = os.path.join(remote_prefix, file_path[len(local_prefix)+1:]) 
    print remote_path


    upload_url = 'http://127.0.0.1:9876/?r=random+string'
    r = requests.post(upload_url, data=dict(path=remote_path),
                      files=dict(file=zlib_data))
    print r.text


if __name__ == '__main__':
    test()

