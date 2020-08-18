import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'files/'
ALLOWED_EXTENSIONS = {'asc', 'pgp', 'gpg'}

GPG_EXCHANGE = Flask(__name__)
GPG_EXCHANGE.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

FILES = []


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_data(title, description, email, filename):
    file_entry = (title, description, email, filename)
    FILES.append(file_entry)


@GPG_EXCHANGE.route('/')
def home():
    get_data("title1", "desc1", "email@mail.com", "file.txt")
    get_data("title2", "desc2", "boomer@mail.com", "test.txt")
    return render_template("home.html", files=FILES)


@GPG_EXCHANGE.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(GPG_EXCHANGE.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))

    return render_template("upload.html")


if __name__ == "__main__":
    GPG_EXCHANGE.run()
