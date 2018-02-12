# EC500_C1_HW1 API Exercise
## Brief Introduction :sunglasses:

  Hello Everyone! :trollface::trollface::trollface::trollface:
  
  This is the page for **EC500_C1(Spring 2018) HW1 API Exercise** 
  [@github/qinjinjia/ec500c1spring18/HW1_API](https://github.com/qinjinjia/ec500c1spring18/tree/master/HW1%20API)
  
  The Author: :boy: **Qinjin Jia** qjia@bu.edu   :point_right:[@github/qinjinjia](https://github.com/qinjinjia)
   
  :mailbox_closed:Please feel free to contact me, if you have any suggestions or concerns.
  
</br>

## Project Description :bowtie:
:new_moon: The aim :golf: of the project：

  * Build a library (preferable in python) that **downloads images from a twitter feed, convert them to a video and describe the content of the images in the video.**
  
  * **Twitter API** to access the twitter content.
  
  * **FFMPEG** to convert images to videos.

  * **Google Vision** analysis to describe the content.
  
  Twitter API Link: :link: https://apps.twitter.com
  
  Google API Link: :link: https://console.cloud.google.com/apis/

</br>

## Configure Enivronment :smirk:
  For running the code, you need to download and install following packages:
  
  My Environment is **macOS High Sierra Version 10.13.3** and **Python 3.5**.
  
  tweetpy (v.0.1):
  
```
  pip install tweetpy
```
  
  ffmpeg (v.3.4.1)
```
  brew install ffmpeg
```

  wget (v.3.2)
```
  pip install wget 
```

  google-cloud-vision(v.0.30.0)
```
  pip install google-cloud-vision
```

```
  pip install google-cloud-bigquery
```

Then set up a Cloud Platform Console project and **download a private key as JSON**

```
  export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
```

Warm NOTE: If Google Cloud does not running on your compter successfully, you may try this command,
```
  source ~/.bashrc
```
Hope this helps.

**Remember to Enable Google Cloud Vision API** in Google Cloud Console

</br>

## Instruction :grinning:
You could use this file **as a Library** or **a Program**.

#### Use as a LIBRARY
There are three functions you could call:

* 1. **get_tweets_imgs_url(screen_name)**

   input: screen_name
   output: urls of all images
   description: utilize Twitter API to access the twitter content

* 2. **conv_imgs2video(media_names)**

   input: images
   
   output: a video
   
   description: utilize FFMPEG to convert images to video
   
* 3. **describe_imgs(media_names)**

   input: images
   
   output: description of each image
   
   description: utilize Google Vision analysis to describe the content


#### Use as a Program

   Just type "**python HW1_API [screen_name]**" in terminal to run
   
   e.g. python HW1_API @helpanimals
   
#### Additionally note
   To use this library, use 'import HW1_API' in your code.
   
   Additionally, you need to set up a Cloud Platform Console project and Download a private key as JSON.

   Then, run export GOOGLE_APPLICATION_CREDENTIALS="[PATH]" in terminal.

#### Enjoy the code and have fun!:wink::wink:

:beers::beers::beers:

<br/>

## Error Handling :satisfied:
```Python
    # Error handler
    if len(new_tweets) == 0:
        print("The account doesn't exist or Has no tweets.\n")
        return 1
```

</br>

## Demo :grin:

:sun_with_face: **Finally, thank you for watching :D)**:exclamation:

:trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface:
