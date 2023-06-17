from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    tipo = request.form['tipo']

    if tipo.lower() == "vídeo":
        download_video(url)
    elif tipo.lower() == "áudio":
        download_audio(url)
    else:
        return "Opção inválida!"

    return "Download concluído!"


def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
    except Exception as e:
        return "Ocorreu um erro ao fazer o download: " + str(e)


def download_audio(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download()
    except Exception as e:
        return "Ocorreu um erro ao fazer o download: " + str(e)


if __name__ == '__main__':
    app.run(debug=True)