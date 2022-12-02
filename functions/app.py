from flask import Flask, render_template
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

#PATH = D:\User\Documents\Iago\Programas\node_modules\npm\bin\npm-cli.js