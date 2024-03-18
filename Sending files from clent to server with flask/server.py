from flask import Flask, request
'''
Server tp handle post request from clinet
'''

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    file.save(file.filename)
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
