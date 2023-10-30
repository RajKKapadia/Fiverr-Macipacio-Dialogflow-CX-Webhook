import json
import os

from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='images/favicon.png')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/dialogflow', methods=['POST'])
def dialogflow():
    data = request.get_json()
    print(json.dumps(data))
    return jsonify(
        {
            'fulfillment_response': {
                'messages': [
                    {
                        'text': {
                            'text': ['This is a sample rewponse from webhopok.']
                        }
                    },
                    {
                        'payload': {
                            "richContent": [
                                [
                                    {
                                        "type": "button",
                                        "icon": {
                                            "type": "chevron_right",
                                            "color": "#FF9800"
                                        },
                                        "text": "Button text",
                                        "link": "https://example.com",
                                        "event": {
                                            "name": "",
                                            "languageCode": "",
                                            "parameters": {}
                                        }
                                    }
                                ],
                                [
                                    {
                                        "type": "image",
                                        "rawUrl": "https://example.com/images/logo.png",
                                        "accessibilityText": "Example logo"
                                    }
                                ]
                            ]
                        }
                    }
                ]
            }
        }
    )


if __name__ == '__main__':
    app.run(debug=True)
