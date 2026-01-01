from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World! 這是我的第一個 Render 網站 🎉"

if __name__ == '__main__':
    app.run()