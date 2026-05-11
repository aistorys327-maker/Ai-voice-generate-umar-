from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1 style='font-family:sans-serif;text-align:center;margin-top:50px'>
    🎤 AI Voice Generator Working Successfully
    </h1>
    """

app.run(host='0.0.0.0', port=10000)
