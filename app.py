from pytube import YouTube
from flask import Flask, request, redirect, render_template
app = Flask(__name__)


# @app.errorhandler(404)
# def nsot(e):
#     return render_template('index.html')


# @app.errorhandler(500)
# def smm(e):
#     return render_template('index.html')

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/video', methods=['GET', 'POST'])
def downloadVideo():
    if request.method == 'POST':
        url = request.form['url']
        # YouTube(url).streams.first().download()
        yt = YouTube(
            url)
        # yt.streams
        yt.title
        yt.thumbnail_url
        yt.streams.all()
        stream = yt.streams.first()
        stream.download()
    return render_template('videos.html')
    return render_template('videos.html')


@app.route('/audio', methods=['GET', 'POST'])
def downloadAudio():
    if request.method == 'POST':
        url = request.form['url']
        yt = YouTube(url)
        yt.title
        yt.thumbnail_url
        stream = yt.streams.all()
        down = stream[(len(stream))-1]
        down.download()
        return render_template('audios.html')
    return render_template('audios.html')

# def downloadVideo():
#     YouTube('https://www.youtube.com/watch?v=m8YHvXcegD0&list=PL7551852FC6526D5D&index=4').streams.first().download()
#     yt = YouTube(
#         'https://www.youtube.com/watch?v=m8YHvXcegD0&list=PL7551852FC6526D5D&index=4')
#     yt.streams
#     yt.filter(progressive=True, file_extension='mp4')
#     yt.order_by('resoultion')
#     yt.desc()
#     yt.first()
#     yt.download()


# def downloadAudio():
    # yt = YouTube('https://www.youtube.com/watch?v=UyQn0BhVqNU&t=356s')
    # yt.title
    # yt.thumbnail_url
    # stream = yt.streams.all()
    # # stream = yt.streams.first()
    # down = stream[(len(stream))-1]
    # down.download('C:/Users/ECC/Desktop/songs')
#     # stream.download()
#     # yt = YouTube(
#     #     'https://www.youtube.com/watch?v=m8YHvXcegD0&list=PL7551852FC6526D5D&index=4')
#     # yt.title
#     # yt.thumbnail_url
#     # stream = yt.streams.all()
#     # stream = stream[0]

#     # # stream = yt.streams.first()
#     # stream.download()
#     # youtube_link = 'https://www.youtube.com/watch?v=m8YHvXcegD0&list=PL7551852FC6526D5D&index=4'

#     # w = YouTube(youtube_link).streams.first()
#     # w.download(output_path="/your/target/directory")

#     # # download a file with only audio, to save space
#     # # if the final goal is to convert to mp3
#     # youtube_link = 'https://www.youtube.com/watch?v=m8YHvXcegD0&list=PL7551852FC6526D5D&index=4'
#     # y = YouTube(youtube_link)
#     # t = y.streams.filter(only_audio=True).all()
#     # t[0].download(output_path="/your/target/directory")


# downloadAudio()
if __name__ == '__main__':
    app.run(debug=True)
