#!/usr/bin/env python
import os
import requests
from flask import ( Flask,
                    jsonify, 
                    request,
                    render_template)

ENV = os.environ.get('ENV', 'prod')
API_KEY = os.environ.get('API_KEY')
GOOGLE_VISION_API = 'https://vision.googleapis.com/v1/images:annotate?key={API_KEY}'.format(API_KEY=API_KEY)
VRequestJSON = {
  "requests": [
      {
        "image": {
          "source": {
              "imageUri": "https://cdn.pixabay.com/photo/2012/02/28/00/47/berliner-17811__340.jpg"
          } 
        },
        "features": [
          {
            "type": "LABEL_DETECTION",
            "maxResults": 10
          }
        ]
      }
  ]
}

UPLOAD_FOLDER = os.path.basename('uploads')
STATIC_FOLDER = os.path.basename('templates')

def make_http_call(json_data):
    return requests.post(GOOGLE_VISION_API, json=json_data)


def base64fyImage(image):
    print('Images is ', dir(image))
    import base64
    image_content = image.read()
    return base64.b64encode(image_content)

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/v1/test/', methods=['GET'])
def test_sample_image():
    # so we make our request here
    http_response = make_http_call(VRequestJSON)
    if http_response.status_code == 200:
        print(http_response.json())
    
    return jsonify(http_response.json())


@app.route('/v1/vision/', methods=['POST'])
def vision_this():
    upload_file = request.files['image']
    filename = os.path.join(app.config['UPLOAD_FOLDER'], upload_file.filename)
    # upload_file.save(filename)
    print(base64fyImage(upload_file))
    return jsonify(VRequestJSON)


def start_server():
    DEBUG = False
    if ENV == 'dev':
        DEBUG = True
    app.run(debug=DEBUG)

    
if __name__ == '__main__':
    start_server()