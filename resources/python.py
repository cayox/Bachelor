from flask import Flask, send_from_directory

app = Flask(__name__)
app.config.from_object(__name__)

# add file endpoint that serves the testfile
@app.route('/file')
def send_report():
    return send_from_directory('.', "testfile.html")

# run app on Port 3000
if __name__ == '__main__':
    app.run(port=3000)