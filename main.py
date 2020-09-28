import praw
import random
import time

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="<CONSOLE:SAD-BOT:1.0>",
    username="",
    password=""
)
#Extra Subreddits = ,"aww","television","dankmemes","amongus","wholesomememes"
subreddit = reddit.subreddit("memes")
quotes_jokes = [
    "Dont be sad here is a quote for you : Never let to know the reason of your sadness to others, they won’t get it. Beep Bop I am a bot.",
    "Dont be sad here is a quote for you : If you get a reason to be happy, take it. Life is small. Beep Bop I am a bot ",
    "Dont be sad here is a quote for you : True love takes time to find, but once it's found, the rest is eternal. Beep Bop I am a bot ",
    "Dont be sad here is a quote for you : very corner and room of a house will carry memories, make these the most pleasurable times you shared with your family. Beep Bop I am a bot ",
    "Dont Be Sad, Here is a joke : When your only tool is a hammer, all problems start looking like nails. Beep Bop I am a bot ",
    "Dont Be Sad , Here is a joke : If you’re too open-minded; your brains will fall out. Beep Bop I am a bot.",
    "Dont Be Sad , Here is a joke : If your diet soda has zero calories, zero sugar and zero fat, what the hell are you drinking"
]


for submission in subreddit.hot(limit=100):
     #print(submission.title)

     for comment in submission.comment:
         if hasattr (comment,"body"):
            comment_lower = comment.body.lower()
            if " sad " in comment_lower:
                print(comment)
                random_index = random.randint(0,len(quotes_jokes))
                comment.reply(quotes_jokes[random_index])
                time.sleep(589)

