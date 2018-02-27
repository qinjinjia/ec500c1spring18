# Copyright 2018 Qinjin Jia qjia@bu.edu Github:qinjinjia

# API Library Unit Test 1

""" EC500_C1_S'18_HW2_Code_Review_Unit_Test
File Description and Instruction:

HW1_API is a LIBRARY developed in EC500_HW1:
link: https://github.com/qinjinjia/ec500c1spring18
there are three functions you could call:
1. get_tweets_imgs_url(screen_name)
   input: screen_name
   output: urls of all images
   description: utilize Twitter API to access the twitter content
2. conv_imgs2video(media_names)
   input: images
   output: a video
   description: utilize FFMPEG to convert images to video
3. describe_imgs(media_names)
   input: images
   output: description of each image
   description: utilize Google Vision analysis to describe the content

Enjoy and have fun!
"""

"""
Note: To use this library, use 'import HW1_API' in your code.
Additionally, you need to set up a Cloud Platform
Console project and Download a private key as JSON
then, run export GOOGLE_APPLICATION_CREDENTIALS="[PATH]" in terminal.
"""


# Please check my Github @qinjinjia for configuing environment

import HW1_API

import subprocess
import time

def unit_test_one():
    start_time = time.time()
    account_list = ["osamaamaso", "BU_Tweets"]
    for account in account_list:
        try:
        	imgs_url = HW1_API.get_tweets_imgs_url(account)
            
        except Exception as error:
            print("----------Error Description----------")
            print(str(error))
            print("-------------------------------------")
    elapse = time.time() - start_time

     

if __name__ == "__main__":
	unit_test_one()

