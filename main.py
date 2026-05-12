from flask import Flask, request, render_template_string
import requests
import os

app = Flask(__name__)

API_KEY = "56d05eb3990544d2a82261365441605b"

HTML = """

<!DOCTYPE html>
<html>

<head>

<title>AI Voice Generator</title>

<style>

body{
background:#0f172a;
font-family:sans-serif;
text-align:center;
padding:30px;
color:white;
}

h1{
font-size:40px;
}

textarea{
width:90%;
height:140px;
padding:15px;
border:none;
border-radius:20px;
font-size:18px;
margin-top:20px;
}

select{
width:90%;
padding:15px;
border:none;
border-radius:15px;
font-size:18px;
margin-top:20px;
}

button{
margin-top:25px;
padding:15px 35px;
border:none;
border-radius:15px;
font-size:20px;
background:#2563eb;
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

<select name="voice">

<option value="male">Deep Male Voice</option>

<option value="female">Soft Female Voice</option>

<option value="robot">Robot Voice</option>

<option value="funny">Funny Voice</option>

</select>

<br>

<textarea
name="text"
placeholder="Type something..."
></textarea>

<br>

<button type="submit">
Generate Voice
</button>

</form>

{% if audio %}

<audio controls autoplay>
<source src="{{ audio }}">
</audio>

<br><br>

<a href="{{ audio }}" download>
<button>Download MP3</button>
</a>

{% endif %}

</body>
</html>

"""

@app.route("/", methods=["GET","POST"])

def home():

    audio = None

    if request.method == "POST":

        text = request.form["text"]
        voice = request.form["voice"]

        headers = {
            "Authorization": f"Bearer {API_KEY}"
        }

        data = {
            "text": text,
            "voice": voice
        }

        response = requests.post(
            "https://api.fish.audio/v1/tts",
            headers=headers,
            json=data
        )

        if response.status_code == 200:

            if not os.path.exists("static"):
                os.makedirs("static")

            with open("static/output.mp3", "wb") as f:
                f.write(response.content)

            audio = "/static/output.mp3"

    return render_template_string(
        HTML,
        audio=audio
    )

app.run(host="0.0.0.0", port=10000)
