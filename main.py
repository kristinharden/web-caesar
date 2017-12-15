from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>

    <body>
        <form action="/" method="POST">
            <label for="rot_input">Rotate by:</label>
            <input id="rot_input" type="text" name="rot" value="0"/>
            <br>
            <br>
            <textarea name="text">Please type your message here.</textarea>
            <br>
            <br>
            <input type="submit" value="Submit Query" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=["POST"])
def encrypt():
    rot = int(request.form["rot"])
    text = request.form["text"]
    rotated_message = rotate_string(text, rot)

    return "<h1>" + rotated_message + "</h1>"


app.run()
