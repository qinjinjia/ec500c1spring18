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

</br>

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
**In [TwitterSumarization.py](https://github.com/abbottn3/EC500/blob/master/TwitterSummarization.py)**

This is an **cross-platform problem**, and I **CANNOT** solve this problem :boom::boom::boom:

As Osama said that if people are having **too much trouble** making the programs **work cross platform**, you can just do the **test
cases for your own program** and only do the **text peer review on peer's project**.

:exclamation::exclamation::exclamation: Therefore, I would do the **test cases for my own program** and **only do the text peer review on peer's API assignment** :exclamation::exclamation::exclamation:

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

### 1. Code Formatting :sun_with_face:
The python file is assessed by the Code Review auxiliary tool: [pep8](https://www.python.org/dev/peps/pep-0008/) and [pylint](https://www.pylint.org) for an overview of the code quality.

 |Python File Name |Link |pep8 check |pylint check |
 |--|--|--|--
 |TwitterSummarization.py|:link: [TwitterSumarization.py](https://github.com/abbottn3/EC500/blob/master/TwitterSummarization.py)|217 Problems|-5.81/10 |

**PEP8 check for TwitterSummarization.py**
```
TwitterSummarization.py:25:1: E302 expected 2 blank lines, found 1
TwitterSummarization.py:26:1: W191 indentation contains tabs
TwitterSummarization.py:27:1: W191 indentation contains tabs
TwitterSummarization.py:28:1: W191 indentation contains tabs
TwitterSummarization.py:29:1: W191 indentation contains tabs
TwitterSummarization.py:30:1: W191 indentation contains tabs
TwitterSummarization.py:32:1: W191 indentation contains tabs
TwitterSummarization.py:33:1: W191 indentation contains tabs
TwitterSummarization.py:33:6: W291 trailing whitespace
TwitterSummarization.py:34:1: W191 indentation contains tabs
TwitterSummarization.py:34:2: E101 indentation contains mixed spaces and tabs
TwitterSummarization.py:35:1: W191 indentation contains tabs
TwitterSummarization.py:35:2: E101 indentation contains mixed spaces and tabs
TwitterSummarization.py:36:1: W191 indentation contains tabs
TwitterSummarization.py:36:2: E101 indentation contains mixed spaces and tabs
and so on...
```


**Pylint check for TwitterSummarization.py**
```
************* Module TwitterSummarization
W: 27, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 28, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 29, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 30, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 33, 0: Trailing whitespace (trailing-whitespace)
W: 33, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 34, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 35, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 36, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 37, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 38, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 38, 0: No space allowed before bracket
      print ("Error -- keys/secrets are incompatible")
           ^ (bad-whitespace)
and so on...

Your code has been rated at -5.81/10 (previous run: -5.81/10, +0.00)
```

According to the **Code Review auxiliary tool Pep8 and Pylint, Overall Code Quality(Formatting) still can be improved.**

#### 1.1 Alignments
The uses of alignments are perfect. The code block starting point and ending point are **easily identifiable**.

#### 1.2 Naming Conventions
The **‘camelCode’** nameing convention is used in the project. The developer utilizes capital letters to indicate the start of a word, which makes name of variables be **meaningful**. However, the developer also uses "underline" naming conventions (e.g. 'pic_urls') in few places of the code. It would be better if the developer could follow the same naming convention for the whole file. 

#### 1.3 Code Layout
:thumbsup:Perfect! The code can fit in the standard 14-inch laptop screen.

#### 1.4 Commented Code
There is no commented code found in the file, which is good. :thumbsup:

</br>

### 2. Architecture :full_moon_with_face:
Not applicable for such a mini project.

</br>

### 3. Coding best practices :first_quarter_moon:
#### 3.1 Hard Coding
:thumbsup: Good!. There is no [hard coding](https://en.wikipedia.org/wiki/Hard_coding) in the project.

#### 3.2 Enumeration
The python file :link: [TwitterSummarization.py](https://github.com/abbottn3/EC500/blob/master/TwitterSummarization.py) contains **[magic number](https://en.wikipedia.org/wiki/Magic_number_(programming))**. It is difficult to understand what is the meaning of 0, 1, 3 etc here.
This might be solved by utilizing the enumeration.
```python
  if pictype > 0:
      escore = 1
    else:
      escore = 3
```

#### 3.3 Comments
The developer utilzes meaningful comments, which helps other to understand the code.
However, this kind of comments(i.e. comments to help developer understand the tutorial) should be deleted (or removed from the master branch).
```python
  # Grabs pic URLs
  pic_urls = twitterDL(t_handle)
```


#### 3.4 Mul if/else blocks
:thumbsup: Good, there is no multiple if/else block in the project.

#### 3.5 Framework features
N/A

</br>

### 4. Non Functional requirements :waning_gibbous_moon:
#### 4.1 Maintainability(Supportability) 
The **Readability** of the code is good. The developer uses **‘camelCode’ nameing convention**, which makes name of variables be meaningful.
The **"Testability", "Debuggability", "Configurability"** are problems, but it's mainly because the cross-platform issue.

**In TwitterSummarization.py**

This is an **cross-platform problem**, and I **CANNOT** solve this problem :boom::boom::boom:

As Osama said that if people are having **too much trouble** making the programs **work cross platform**, you can just do the **test
cases for your own program** and only do the **text peer review on peer's project**.

:exclamation::exclamation::exclamation: Therefore, I would do the **test cases for my own program** and **only do the text peer review on peer's API assignment** :exclamation::exclamation::exclamation:

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


#### 4.2 Reusability
Some places in the code violate [DRY (Do not Repeat Yourself) principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).Duplicated code is a risk to safety. If you have identical or very similar code in two places, then the fundamental risk is that there’s a bug in both copies, and some maintainer fixes the bug in one place but not the other.
```Python
    if pictype > 0:
        d_dict['Image_{}'.format(filecnt)].append(logos[0].description)
        picdescripts.write(logos[0].description)
      else:
        d_dict['Image_{}'.format(filecnt)].append(logos[0].description)
        picdescripts.write('Logo Description: {}, '.format(logos[0].description))
```

However, the project utilizes **generic functions**, which increase reusability of the project. 

#### 4.3 Reliability:
Exception handling is considered in the code.
```Python
  # Verifying Twitter Handle
  try:
      user = api.get_user(user_handle)
  except tweepy.TweepError:
      print ("Error -- invalid Twitter handle")
      sys.exit()
```

#### 4.4 Extensibility
The developer could use this code to increase the "Extensibility".
```Python
# for using this file as a Library
if __name__ == '__main__':
    main()
```
Thus, the file could be used as an library and then the functions in the file could be called in other files.

</br>

### 5. Synchronous or Asynchronous :last_quarter_moon:
Synchronous/asynchronous APIs are application programming interfaces(API) that return data for requests either immediately or at a later time, respectively. The synchronous and asynchronous nature of an API is a function of the time frame from the request to the return of data.:link: [**link**](http://whatis.techtarget.com/definition/synchronous-asynchronous-API)
For the code reviewed, [**TwitterSumarization.py**](https://github.com/abbottn3/EC500/blob/master/TwitterSummarization.py), **the code is Synchronous** :bouquet: as the code returns data for requests immediately. We need to wait until all images are downloaded to continue next step.

</br>

### Develop Test scenarios and scripts :guardsman:

Note: There are **too much trouble** making the peer's programs **work cross platform**, so I just do the **test
cases for my own programs**.

|Data of Test Run|Feb. 16th, 2018|
|---|---
|Environment Description|Macbook(macOS V10.13.1)|
|SW Version||

|ID|Test Scenario|Involved|Test Steps|Results|Pass/Fail|Priority|
|---|---|---|---|---|---|---
|1||||||
|2||||||
|3||||||
|4||||||
|5||||||
|6||||||
|7||||||


</br>

## Build a local home page :hear_no_evil:

### Instruction for using local home page

:one: Download webpage floder :open_file_folder: [here](https://github.com/qinjinjia/ec500c1spring18/tree/master/HW2%20Code%20Review)

:two: cd to the floder, use the command
```
    python main.py
```
Then, the url for local home web would be displayed,
URL for Local home page: http://127.0.0.1:8080
```
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 226-064-645
```

:three: Enter the screen name on the page. (N.B. Remember to include @)

:four: Results(video and description) would be displayed on another page. 

Enjoy and have fun :beers:

### Demo

<img src="https://github.com/qinjinjia/ec500c1spring18/blob/master/HW2%20Code%20Review/images_for_readme/form_page.png" width="650" height="350">
