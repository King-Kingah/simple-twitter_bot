# simple-twitter_bot

This is a simple Tweeter bot developed using Python and Tweepy module.

The bot retweets and favorites tweets based in specified keywords.

## Twitter Bot Challenge (#BuildWhat'sNext)
The Twitter Bot Challenge aims to support the tech ecosystem in Kenya to build using the Twitter API.
We will be using the API to build for fun by creating bots. This is a summary of my experience participating, the good, the bad and the ugly, and most of all what you learned.

The goal is to create a twitter bot which tweets Dev, Linux, and other Coding content. Primarily, I decided to develop the bot using Python as it has several handy libraries and tools. As always, it is safer to code new python projects within virtual environments.


## Requirements
- Twitter developer account
- Python3.8
- Python virtual environment
  - Tweepy: install using the command: 'pip install tweepy'
  - ConfigParser: install using: 'pip install configparser'

## Twitter Developer Account

Search for Twitter Developer Account on any search engine of your choice and choose the first option (should be). This will redirect you to a Developer Portal. Create a new application under the **Projects & Apps** section.

Request for a Twitter Developer Account and provide a few answers:
![First page you'll be greeted with](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mgw3sb6fd05jnjeydjwc.png)

Create an application:
![Projects and Applications](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ljyunblbr296sc0bg7xr.png)

Request for privileged permissions under the User Authentication Settings. I decided to use OAuth 1.0a:
![User Authentication settings](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xh4kmjmfxmh00ha0jeua.png)

Select the Read and write and Direct message App permissions:
![Permissions](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zxrye3rzh7z9d4e71jkk.png)

Generate API Key, API Key Secret, Access Token and Access Token Secret:
![Generate and copy keys](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ufh8pz07p102shovnbgt.png)

## Python Virtual Environment
For this project, we will use Python3.8, and primarily the Tweepy Python package to develop a simple Twitter bot that retweets, and favorites tweets with certain keywords.

Create a virtual environment to install all the necessary modules using pip, separate and without interfering with the system(global) packages. This can be done by running the command:

```
python3 -m venv yourvirtualenv
```
Activate the virtual environment to install the libraries:

```
source yourvirtualenv/bin/activate
```
Install the following packages/libraries:

tweepy - this is the primary python package the bot uses to communicate or interface with the Twitter API. It has a rich module and function libraries in addition to a supportive community. This makes it the most popular package for automating Twitter.

Install using:

```
pip install tweepy

```
configparser - used to hide important credentials such as api key, api key secret, access token and access token secret. Therefore, it is safer when sharing the code with others as one does not have to share these credentials.

Install using:

```
pip install configparser
```

time - a Python module that is used to represent time in different ways including objects, numbers and strings as well as offering various functionality such as waiting during code execution.

NOTE: If you have cloned this repository, install all pip packages using the requirements.txt file.
This is done by running:
```
pip install -r requirements.txt
```

## Contribution
Any contributions are welcome. Create a pull request or open an issue.