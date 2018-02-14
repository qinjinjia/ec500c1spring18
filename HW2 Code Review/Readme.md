# EC500_C1_HW2 Code Review Exercise
## Brief Introduction :sunglasses:

  Hello Everyone! :trollface::trollface::trollface::trollface:
  
  This is the page for **EC500_C1(Spring 2018) HW2 Code Review** [@github/qinjinjia/ec500c1spring18/HW2_Code_Review](https://github.com/qinjinjia/ec500c1spring18/tree/master/HW2%20Code%20Review)
  
  The Author: :boy: **Qinjin Jia** qjia@bu.edu   :point_right:[@github/qinjinjia](https://github.com/qinjinjia)
   
  :mailbox_closed:Please feel free to contact me, if you have any suggestions or concerns.
  
</br>

## Project Description :bowtie:
:new_moon: The aim :golf: of the project：
* :sun_with_face: Comprehensive **Code Review**
* :full_moon_with_face: Develop **Test** scenarios and scripts
* :new_moon_with_face: Build a **local home page**


## Comprehensive Code Review :neckbeard:
### Overall

  |The project reviewed| **[@github.com/abbottn3/EC500](https://github.com/abbottn3/EC500)**
  |--|--
  |**The Reviewer**| :boy: **Qinjin Jia** qjia@bu.edu   :point_right:[@github/qinjinjia](https://github.com/qinjinjia)
  |**Criteria Followed**| [MIT 6.005 fall 15 - Reading 4 Code Review](http://web.mit.edu/6.005/www/fa15/classes/04-code-review/) 
  ||[Code Review Checklist](http://www.evoketechnologies.com/blog/code-review-checklist-perform-effective-code-reviews/)

  :sun_with_face: Summary of the Code Review Criteria :link: [Code Review Criteria.pdf](https://github.com/qinjinjia/ec601_Code-Review/blob/master/Code%20Review%20Criteria.pdf) 
 
 :full_moon_with_face: Code Review auxiliary tool: [pep8](https://www.python.org/dev/peps/pep-0008/), [pylint](https://www.pylint.org)
 
#### Some bugs in the code were fixed before conducing code review.
**********************************************************
**In myTweep.py**

**parentheses missed for call to 'print'**

File "myTweep.py", line 75
    print media_files
                    ^
SyntaxError: Missing parentheses in call to 'print'

**Solution**:
Change
```Python
print media_files
```
to
```Python
print (media_files)
```

**********************************************************
**In TwitterSummarization.py**

This is an **cross-platform problem**, and I **CANNOT** solve this problem :boom::boom::boom:

As Osama said that if people are having **too much trouble** making the programs **work cross platform**, you can just do the **test
cases for your own program** and only do the **text peer review on peer's project**.

:exclamation::exclamation::exclamation: Therefore, I would do the **test cases for my own program** and **only do the text peer review on peer's API assignment**

```
Traceback (most recent call last):
  File "TwitterSummarization.py", line 209, in <module>
    main()
  File "TwitterSummarization.py", line 201, in main
    description_dict = gVision_and_FFMPEG(pic_urls)
  File "TwitterSummarization.py", line 143, in gVision_and_FFMPEG
    if webnotes.web_entities[0] > escore:
TypeError: '>' not supported between instances of 'WebEntity' and 'int

```

**********************************************************


## Develop Test scenarios and scripts


## Build a local home page
