from pytube3 import YouTube
from flask import Flask, request, render_template, send_file
import os
import shutil

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/download", methods=['GET', 'POST'])
def download():
    cleanOutput()
    url = request.form.get('url')
    yt = YouTube(str(url))

    video = yt.streams.filter(only_audio=True).first()

    destination = 'templates/output/'
    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)
    os.rename(out_file, base + '.mp3')
    path = out_file.replace('.mp4', '.mp3')
    return send_file(path, mimetype='mp3')


def cleanOutput():
    folder = './templates/output'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
