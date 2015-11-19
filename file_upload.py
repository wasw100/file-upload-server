# -*- coding: utf-8 -*-
import zlib
import os
import os.path
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request

app = Flask(__name__)
app.debug = False

# log to file
app.logger.setLevel(logging.INFO)
log_path = os.path.join(os.path.dirname(__file__), 'logs/web.log')
handler = RotatingFileHandler(log_path, maxBytes=10*1024*1024, backupCount=1)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s'
                              '- %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)


@app.before_request
def before_request():
    # 通过传参或者IP做访问限制
    r = request.args.get('r', '')
    if r == 'random string':
        return

    if not request.headers.getlist('X-Forwarded-For'):
        ip = request.remote_addr
    else:
        ip = request.headers.getlist('X-Forwarded-For')[0]

    if ip not in ['ip addr']:
        return 'no permission - {0}'.format(ip)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    ''' if method is GET, can return, but you should upload zlib file
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
        <input type=file name=file><br>
        <input name=path><br>
        <input type=submit value=Upload>
    </form>
    '''
    if request.method == 'POST':
        file_ = request.files['file']
        filename = request.form['path']
        app.logger.debug('upload - {0}'.format(filename))
        app.logger.info('upload - {0}'.format(filename))
        app.logger.error('upload - {0}'.format(filename))
        if file_ and filename:
            directory = os.path.dirname(filename)
            if not os.path.exists(directory):
                os.makedirs(directory)

            zlib_data = file_.stream.read()
            data = zlib.decompress(zlib_data)
            with open(filename, 'wb') as f:
                f.write(data)
            return 'OK, save - {0}'.format(filename)
        else:
            return 'Error, path - {0}'.format(filename)

    return 'test'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876)
