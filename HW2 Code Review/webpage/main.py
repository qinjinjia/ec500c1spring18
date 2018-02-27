# Copyright 2018 Qinjin JIA. All Rights Reserved.

import HW1_API

import logging
import os
from flask import Flask, render_template, request, make_response, send_file


app = Flask(__name__)

# [START Transfer to the main page]
@app.route('/')
def form():
    return render_template('form.html')
# [END of Transfer to the main page]


# [START Displaying Result]
@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    
    try:
        media_names = HW1_API.get_tweets_imgs_url(name)
        HW1_API.conv_imgs2video(media_names)
        description = HW1_API.describe_imgs(media_names)

    except Exception as errors:
        print(str(errors))
    return render_template('submitted_form.html', name = name, description = description)
# [END of Displaying Result]


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    Copyright 2018 Qinjin JIA qjia@bu.edu
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
