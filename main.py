from flask import Flask, request
from caesar import rotate_string, rotate_character, alphabet_position, rotate_string_13

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="post">
                
            <label="rot">Rotate by:</label>
            <input id-"rot" type="text" name="rot" value='0'>   
                
            <br>
            <textarea id-'text' type= "text" name="text" >{0}</textarea>
            <br>
            <input type="submit" value="Submit Query">
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    new_form= form.format('')
    
    return new_form

@app.route("/", methods=['POST'])
def encrypt():
    
    rot = request.form['rot']
    rot = int(rot)
    text = request.form ['text']
    new_message = ''
    
    new_message += rotate_string(text, rot)
    new_message = form.format(new_message)
    
        
    
    
    
    
    
    return new_message

app.run()