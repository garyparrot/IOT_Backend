from flask import current_app as app
from werkzeug import secure_filename
import glob, json, os

def generate_path(filename, secure = True):
    if secure:
        filename = secure_filename(filename)
    return os.path.join(app.root_path,app.config['UPLOAD_FOLDER'], filename)

def create_record(filename):
    yymmdd = filename.split('_', 3)[:3]
    return { "id": filename, "date": "/".join(yymmdd) }

def get_records(maximum = 30):
    images = [ image.rsplit('/', 1)[1] for image in glob.glob(generate_path("*.jpg", False)) ]

    images = images[:maximum]

    records = { "records": [ create_record(filename) for filename in images ] }

    return records
