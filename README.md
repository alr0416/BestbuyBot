# Bestbuy-Bot
### This is a script that uses a modified ChromeDriver to automate buying a product from Bestbuy.


## 1. Install Dependencies
### Install [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads)
```commandline
pipenv install python-dotenv
pipenv install undetected_chromedriver
pipenv install selenium               
```


## 2. Set Variables in .env file
```python
EMAIL=youremail@email.com
PASSWORD=yourpassword
CVV=123
```

### NOTE
As Bestbuy updates their website periodically, this script could go out of date where changes may need to be made to keep the script working correctly. 

