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
Hope this helps. :neckbeard:

**Remember to Enable Google Cloud Vision API** in Google Cloud Console

</br>

## Instruction :grinning:
You could use this file **as a Library** or **a Program**.

#### Use as a LIBRARY :file_folder:
There are three functions you could call:

##### 1. **get_tweets_imgs_url(screen_name)**
* input: screen_name

* output: urls of all images

* description: utilize Twitter API to access the twitter content

##### 2. **conv_imgs2video(media_names)**
* input: images
   
* output: a video
   
* description: utilize FFMPEG to convert images to video
   
##### 3. **describe_imgs(media_names)**
* input: images
   
* output: description of each image
   
* description: utilize Google Vision analysis to describe the content


#### Use as a Program :scroll:

   Just type "**python HW1_API [screen_name]**" in terminal to run
   
   e.g. python HW1_API @helpanimals
   
#### Additionally note :pushpin:
   To use this library, use '**import HW1_API**' in your code. :page_with_curl:
   
   Additionally, you need to **set up a Cloud Platform Console project** and **Download a private key as JSON.**

   Then, run export GOOGLE_APPLICATION_CREDENTIALS="[PATH]" in terminal. :pill:

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

```Python
      try:
          media = status.entities.get('media', [])
          if(len(media) > 0):
              media_files.add(media[0]['media_url'])
      except:
          print("An error occurs wilie obtaining image URL.\n")
          return 2
```

```Python
    # convert image to video
    try:
        # names for concatenating
        names = open('filenames.txt', 'w')
        for filename in media_names:
            output = filename.replace(".jpg",".mp4")
            names.write("file " + output + "\n")
            cmd = "ffmpeg -loop 1 -i " + filename + " -c:a libfdk_aac -ar 44100 -ac 2 -vf \"scale='if(gt(a,16/9),1280,-1)\':\'if(gt(a,16/9),-1,720)\', pad=1280:720:(ow-iw)/2:(oh-ih)/2\" -c:v libx264 -b:v 10M -pix_fmt yuv420p -r 30 -shortest -avoid_negative_ts make_zero -fflags +genpts -t 1 " + output
            os.system(cmd)
        names.close()
        
        # concate all videos to a video
        concat_cmd = "ffmpeg -f concat -i filenames.txt output.mp4"
        os.system(concat_cmd)
    except:
        print("An error occurs while using FFMPEG.\n")
        return 3
```

Also, some other error would be raised by API.

In Summary,
|Error Code|Error Description|
|---|---
|1|The account doesn't exist or Has no tweets.|
|2|An error occurs wilie obtaining image URL.|
|3|An error occurs while using FFMPEG.|
|Other|Raised by API|

</br>

## Demo :grin:

<img src="https://github.com/qinjinjia/ec500c1spring18/blob/master/HW1%20API/Images%20for%20Readme/terminal%20screenshot.png" width="400" height="200">


:sun_with_face: **Finally, thank you for watching :D)**:exclamation:

:trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface:
