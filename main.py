from flask import Flask, request, render_template_string
from gtts import gTTS
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>AI Voice Generator</title>
<style>
body{
background:#0f172a;
font-family:sans-serif;
color:white;
text-align:center;
padding:40px;
}
textarea{
width:90%;
height:120px;
border-radius:15px;
padding:15px;
font-size:18px;
}
button{
margin-top:20px;
padding:15px 30px;
font-size:20px;
border:none;
border-radius:15px;
background:#3b82f6;
color:white;
}
audio{
margin-top:30px;
width:90%;
}
</style>
</head>
<body>

<h1>🎤 AI Voice Generator</h1>

<form method="POST">
<textarea name="text" placeholder="Type something..."></textarea>
<br>
<button type="submit">Generate Voice</button>
</form>

{% if audio %}
<audio controls autoplay>
<source src="{{ audio }}">
</audio>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():
    audio = None

    if request.method == "POST":
        text = request.form["text"]

        tts = gTTS(text=text, lang='en')
        tts.save("static/output.mp3")

        audio = "/static/output.mp3"

    return render_template_string(HTML, audio=audio)

if not os.path.exists("static"):
    os.makedirs("static")

app.run(host="0.0.0.0", port=10000)
