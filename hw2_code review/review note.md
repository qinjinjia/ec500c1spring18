# Code review

## Comprehensice Code Review
1.Data path review: 

2.API calls: Tweepy,ffmpeg,Google Vision

3.Code convention:
-Have a main function
-Every step has a funciton
-pylint score: 3.03/10

4.Readablity:
The code has a lot of useful comments to make it easy to read.

5.Error handling:
-Gives notification if no posts in twitter acount
-Gives notification if an error occurs while obtaining image URL
-Gives notification if an error occurs while using FFMPEG

Summary: Awesome performance in error handling.

6.Is the main call Synchronous or Asynchronous:
Synchronous.Deesn't need additional inputs.

## Develop Test scenarios and scripts
The code can perfectly get image URL, download them, and convert them to a vedio/vedioes.
However, It appears credential problem when calling Google Vision.

Before I ran the code, in terminal, I exported Google applicaiton Credential of my own json file:
```
export GOOGLE_APPLICATION_CREDENTIALS="/Users/rzhan/Desktop/Alzheimer\'s-683341b411e6.json"
```
Then I ran the code, after converting images into vedio, there came error shows that:
```
google.auth.exceptions.DefaultCredentialsError: File /Users/rzhan/Desktop/Alzheimer\'s-683341b411e6.json was not found.
```
So I just designed test for the first two steps.

I tried to give a wrong twitter ID in command line, and it returned error message like this
![alt text](https://github.com/qinjinjia/ec500c1spring18/blob/master/hw2_code%20review/Screen%20Shot%202018-02-21%20at%208.13.11%20PM.png)
Then I gave an empty screen page, it showed the same message 

