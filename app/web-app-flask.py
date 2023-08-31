from flask import Flask

app = Flask(__name__)
count = 0

@app.route('/metric')
def metric():
    global count
    count += 1
    return str(count)

@app.route('/healthz')
def health():
    return "ok"

app.run()