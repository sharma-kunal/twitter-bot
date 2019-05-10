# twitter-bot
Automated reply to tweets 

This is a automated script for twitter to reply to your tweets. The script is made using `Selenium`. I choose `Selenium` over
`Tweepy` because using Tweepy would restrict me to using only one account. But in this script I have asked the user for the 
Twitter account details. 

The example of script running is shown in the below video,

[![Watch the video](https://img.youtube.com/vi/fdLvY6ek1QY/maxresdefault.jpg)](https://youtu.be/fdLvY6ek1QY)

In this example video I did not ask the user for Twitter account details because I am using a temporary account for this purpose.

If you want to add your account just uncomment the lines `39 and 40`. 

To run the script just follow the below steps, 

1. Clone the project and then navigate to the project folder.

2. Run the command in the project folder

```
pip3 install -r requirements.txt
```

3. Download geckodriver for Firefox for your OS from the link https://github.com/mozilla/geckodriver/releases

4. After downloading geckodriver, navigate to the folder where the geckodriver is installed and run the commands,

```
tar -xvzf <full-name-of-the-downloaded-file>
```

```
chmod +x geckodriver.
```

```
sudo mv geckodriver /usr/local/bin/
```

Now you are good to go. Just go and run the script. 

Happy Coding :)
