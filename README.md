## About
This is a reddit bot to search for the word "sad" and reply with jokes or quotes. 


## Requirementes
- Python 3.6 Or Higher
- PRAW Module


```bash
pip install praw
```



## Preperations
Create and app at https://reddit.com/prefs/apps

Enter some stuff like this:

Name : (Anything)
<br>
Type : Script
<br>
Description : (Anything)
<br>
About : http://localhost:8080
<br>
Redirect URI : http://localhost:8080

// IMGS COMING

Now you have done that go to the Python Script and edit:
<br>
client_id = "(THE ID SPECIFIED UNDER YOUR APP NAME IN reddit.com/prefs/apps)"
<br>
like this:
```
client_id="SI8pN3DSbt0zor"
```
now fill the secret
<br>
client_secret="(Go To Edit App , Then In The Description , there will be secret. Copy and Paste it here)"
<br>
like this:
```
client_secret= "xaxkj7HNh8kwg8e5t4m6KvSrbTI"
```
now fill password of your reddit account like:
```
password="1guiwevlfo00esyy"
```
fill your user_agent like this if appname is testscript and username is fakebot3:
```
user_agent="testscript by u/fakebot3
```
fill your reddit username like:
```
username="fakebot3"
```
all of this will look like:
```
reddit = praw.Reddit(client_id="SI8pN3DSbt0zor",
                     client_secret="xaxkj7HNh8kwg8e5t4m6KvSrbTI",
                     password="1guiwevlfo00esyy",
                     user_agent="testscript by u/fakebot3",
                     username="fakebot3")

```
with this info replace [this](https://github.com/fast-and-curious-1910/happy-bot-reddit/blob/9cec2b2cabfb7cbc60734c3c59c6998ef06c5081/main.py#L5-L11) with this :point_up: info


And that is it !

#### Disclaimer
I am not responsible if your reddit account gets banned or you get banned from a subreddit  . This is made for fun only . Do not run this bot in r/deppresion or anything such as that
