# EC500_C1_HW3 Database
## Brief Introduction :sunglasses:

  Hello Everyone! :trollface::trollface::trollface::trollface:
  
  This is the page for **EC500_C1(Spring 2018) HW3 Database** 
  [@github/qinjinjia/ec500c1spring18/HW3_Database](https://github.com/qinjinjia/ec500c1spring18/tree/master/HW3%20Database)
  
  The Author: :boy: **Qinjin Jia** qjia@bu.edu   :point_right:[@github/qinjinjia](https://github.com/qinjinjia)
   
  :mailbox_closed:Please feel free to contact me, if you have any suggestions or concerns.
  
</br>


## Configure Enivronment :smirk:
  For running the code, you need to download and install following packages:
  
  My Environment is **macOS High Sierra Version 10.13.3** and **Python 3.5**.
  
  MongoDB
  https://api.mongodb.com/python/current/installation.html
```
  brew install mongodb
```
  
  pymongo-3.6.1
  https://api.mongodb.com/python/current/installation.html
```
  python -m pip install pymongo
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

Warm NOTE2: You may encounter the following issue, 

When you attemp to execute these commands

```
sudo mkdir -p /data/db
```
```
sudo chown -R $USER /data/db
```
Issue:
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
2018-03-28T16:48:49.108-0400 W NETWORK  [thread1] Failed to connect to 127.0.0.1:27017, in(checking socket for error after poll), reason: Connection refused
2018-03-28T16:48:49.109-0400 E QUERY    [thread1] Error: couldn't connect to server 127.0.0.1:27017, connection attempt failed :
connect@src/mongo/shell/mongo.js:251:13
@(connect):1:6
exception: connect failed

Try to solve this bug with this command
$ brew services start mongodb

Good Luck!

:trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface::trollface:
