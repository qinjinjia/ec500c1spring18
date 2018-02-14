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


## Comprehensive Code Review
#### Some bugs in the code were fixed before conducing code review.
In myTweep.py

parentheses missed for call to 'print'

File "myTweep.py", line 75
    print media_files
                    ^
SyntaxError: Missing parentheses in call to 'print'

Solution:
Change
```Python
print media_files
```
to
```Python
print (media_files)
```

## Develop Test scenarios and scripts


## Build a local home page
