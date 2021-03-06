# twitter-bot
Automated reply to tweets 

This is a automated script for twitter to reply to your tweets. The script is made using `Selenium`. I choose `Selenium` over
`Tweepy` because using Tweepy would restrict me to using only one account. But in this script I have asked the user for the 
Twitter account details. 

The example of script running is shown in the below video,

[![Watch the video](https://img.youtube.com/vi/M4wTYVx2cqI/maxresdefault.jpg)](https://youtu.be/M4wTYVx2cqI)

In this example video I did not ask the user for Twitter account details because I am using a temporary account for this purpose.

If you want to add your account just uncomment the lines `39 and 40`. 

To run the script just follow the below steps, 

1. Clone the project and then navigate to the project folder.

2. Run the command in the project folder

```
pip3 install -r requirements.txt
```

3. Download geckodriver for Firefox for your OS from the link https://github.com/mozilla/geckodriver/releases

4. After downloading geckodriver, navigate to the folder where the geckodriver is downloaded and run the commands,

```
tar -xvzf <full-name-of-the-downloaded-file>
```

```
chmod +x geckodriver.
```

```
sudo mv geckodriver /usr/local/bin/
```

Now you are good to go.

Now write the reply to the tweet in the `tweet_reply.txt` file and run the script using the command

```
python3 twitter_bot.py
```

Happy Coding :)
