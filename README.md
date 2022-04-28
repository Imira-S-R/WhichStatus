## WhichStatus
Free program to check your website status and alert you when it is down.
## How to use
1. Download the repo.
2. Install rhe requirements
```js
pip install -r requirements.txt
```
3. Fill the config.py with your information
```js
FROM_EMAIL = ''
FROM_EMAIL_PASSWORD = ''
TO_EMAIL = ''

URL = ''
CHECK_EVERY = 0 # In seconds, the script will check every <seconds you gave> whether your website is down.

SMTP_HOST = '' # For gmail use smtp.gmail.com
PORT = 0 # For Gmail use 465
```
4. Run the file
```js
python main.py
```
## How it works
This program will check if your website is down and alert you through email if it is down. And it will send you an email when it comes back up again.
