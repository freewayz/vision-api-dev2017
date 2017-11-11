#!/usr/bin/env python
import os
import requests
from flask import ( Flask,
                    jsonify, 
                    render_template)

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

def make_http_call(json_data):
    return requests.post(GOOGLE_VISION_API, json=json_data)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/v1/test/', methods=['GET'])
def test_sample_image():
    # so we make our request here
    http_response = make_http_call(VRequestJSON)
    if http_response.status_code == 200:
        print(http_response.json())
    
    return jsonify(http_response.json())


@app.route('/v1/vision/', methods=['POST'])
def vision_this():
    upload_file = 

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run(debug=True)