import os, glob
from flask import Blueprint, request, render_template, redirect, url_for, jsonify, send_file
from flask import current_app as app
from flask_login import login_required
from datetime import datetime
from .records import generate_path, get_records

api_bp = Blueprint('api_bp', __name__, url_prefix = '/api')

@api_bp.route('/records', methods = ['GET'])
@login_required
def image_records():
    return jsonify(get_records())

@api_bp.route('/images')
@login_required
def download_image():
    if 'imageId' not in request.args:
        return "Nothing", 404

    imageId = request.args['imageId']

    if not os.path.exists(generate_path(imageId)):
        return "Nothing", 404

    return send_file(generate_path(imageId), mimetype="image/jpeg")

# Writing shit code :(
@api_bp.route('/upload_image', methods = [ 'GET','POST' ])
@login_required
def upload_image():

    if request.method == 'POST':
        # Test if the image was in the request result
        if 'image' not in request.files or request.files['image'] == '':
            return "Where is the file?", 400

        image = request.files['image']

        allowed_file = lambda filename: '.' in filename and filename.rsplit('.',1)[1].lower() == "jpg"
        # if the file is valid, save it
        if image and allowed_file(image.filename):
            filename = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".jpg"
            image.save(generate_path(filename))
            return "success", 200
 
    return '''
        <form method="post" enctype=multipart/form-data>
            <input type=file name=image>
            <input type=submit value=Go>
        </form>
    '''
