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
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            p.error {
                color: red;
            }
        </style>
    </head>
    <body>
        <form method="post">
            <div>
                <label for="rotate-by">Rotate By:</label>
                <input id="rotate-by" type="text" name="rot" value="0" />
                <p class="error"></p>
           </div>
            <textarea type="text" name="text">{0}</textarea>
            <br>
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    form_rot = int(request.form['rot'])
    form_text = request.form['text']
	encrypted = rotate_string(form_text, form_rot)
    return form.format(encrypted)

app.run()    