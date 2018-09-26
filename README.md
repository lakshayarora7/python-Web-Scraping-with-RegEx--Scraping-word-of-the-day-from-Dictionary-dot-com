# python-Web-Scraping-with-RegEx--Scraping-word-of-the-day-from-Dictionary-dot-com


Python script to fetch word of the day from Dictionary.com and print it to the console.

![Alt text](screenshot1.PNG?raw=true "python-Web-Scraping-with-RegEx--Scraping-word-of-the-day-from-Dictionary-dot-com")

Package requirements:
$ pip install requests
For more information on how to install packages with pip, refer to https://www.djangospin.com/python-installing-external-modules-using-pip/.


Script flow:
1. get page source of page http://dictionary.reference.com/wordoftheday/.
2. match word and meaning with regex; for more information on how to use regex in Python, refer to http://www.djangospin.com/regular-expression-in-python/.
3. clean the word-meaning to remove unicode characters, non breakable spaces and html tags.
4. output the word-meaning in unformatted form, and HTML formatted form.
