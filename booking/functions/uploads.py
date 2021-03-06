from booking import ALLOWED_EXTENSIONS
from werkzeug.utils import secure_filename
# Import the app itself
from booking import app


def allowed_file(filename):
    # Checks that the file being uploaded has a "." in it's name
    # and that everything following the "." is a real extension
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def new_file_name(client, extension):
    new_name = secure_filename("%r-%r-1" % (client.business_id, client.id))
    return app.config['UPLOAD_FOLDER'] + new_name + extension


def resize_image(file):
    # Shrinks the image by 15% repeatedly until it has a length and width both less than 2500px
    while file.size[0] > 2500 or file.size[1] > 2500:
        width = int(file.size[0] * 0.85)
        height = int(file.size[1] * 0.85)
        file = file.resize((width, height))
    return file
