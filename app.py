#!/usr/bin/env python
import os
import requests
from flask import Flask, jsonify
from collections import namedtuple


app = Flask(__name__)

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


def make_http_call(json_data):
    return requests.post(GOOGLE_VISION_API, json=json_data)

@app.route('/')
def index():
    return 'Hello DevFest 2017'


@app.route('/v1/test/', methods=['GET'])
def test_sample_image():
    # so we make our request here
    http_response = make_http_call(VRequestJSON)
    if http_response.status_code == 200:
        print(http_response.json())
    
    return jsonify(http_response.json())


if __name__ == '__main__':
    app.run(debug=True)