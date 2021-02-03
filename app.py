from flask import Flask


app = Flask(__name__)

#stub out test route
@app.route('/')
def index():
    return 'hello world'

if __name__=='__main__':
    app.run(port=8000, debug=True)

