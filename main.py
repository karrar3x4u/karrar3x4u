from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__)
VIDEO_DIR = "/mnt/sdcard/Movies"  # غيّره لو مسار مختلف

@app.route("/")
def index():
    videos = [f for f in os.listdir(VIDEO_DIR) if f.lower().endswith(('.mp4', '.mkv', '.avi'))]
    return render_template_string("""
        <html>
        <head><title>StreamSanctum</title></head>
        <body style='background:black; color:white; font-family:sans-serif'>
        <h2>StreamSanctum</h2>
        <ul>
            {% for video in videos %}
            <li><a style='color:cyan' href='/video/{{ video }}'>{{ video }}</a></li>
            {% endfor %}
        </ul>
        </body>
        </html>
    """, videos=videos)

@app.route("/video/<path:filename>")
def video(filename):
    return send_from_directory(VIDEO_DIR, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
