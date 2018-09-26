# Python script to fetch word of the day from Dictionary.com and print it to the console

from requests import get as requestsGet
from re import search as reSearch
from re import sub as reSub

def wordOfTheDay(URL):
	print("Fetching word of the day from {}...".format(URL))

	# GET PAGE SOURCE
	source = requestsGet(URL)

	# MATCH REGEX TO OBTAIN HTML SNIPPET FROM PAGE SOURCE THAT CONTAINS WORD AND MEANING
	matchedObject = reSearch(r'Definitions for <strong>(.+?)</strong>[\S\s\n]*?<li class="first"><span>(.+?)</span></li>', source.text)

	# TO SEE EXACTLY HOW THE REGEX IS MATCHING THE PAGE SOURCE, GO TO https://regex101.com/r/vI9lEA/1/, AND PASTE THE PAGE SOURCE FROM http://dictionary.reference.com/wordoftheday/ IN TEST STRING SECTION. THEN CLICK ON 'FULL MATCH' IN MATCH INFORMATION PANE, YOU WILL BE ABLE TO SEE A BLUE AND RED HIGHLIGHTED SECTION. THE BLUE HIGHLIGHTED TEXT IS THE NON-CAPTURE MATCH AND RED HIGHLIGHTED TEXT IS OUR CAPTURE MATCH.

	try:
		word = matchedObject.group(1)
		meaning = matchedObject.group(2)

		# CLEANING THE WORD-MEANING TO REMOVE ANY HTML TAGS, UNICODE DECIMAL CODES, NON BREAKABLE SPACES.
		cleanedWord = reSub('<.*?>', '', word)
		cleanedWord = reSub('&#\d{2,4};', '', cleanedWord)
		cleanedWord = reSub('&nbsp;', ' ', cleanedWord)

		cleanedMeaning = reSub('<.*?>', '', meaning)
		cleanedMeaning = reSub('&#\d{2,4};', '', cleanedMeaning)
		cleanedMeaning = reSub('&nbsp;', ' ', cleanedMeaning)

		entryWithoutHTML = "Entry Without HTML\n:{}: {}".format(cleanedWord, cleanedMeaning)
		entryWithHTML = "Entry with HTML:\n<strong>{}</strong>: {}".format(cleanedWord, cleanedMeaning)

		print("{}\n".format(entryWithoutHTML))

		print("<li>{}</li>\n".format(entryWithHTML))

	except:
		print("Error in retrieving information from {}".format(URL), file = sys.stderr)


if __name__ == '__main__':
	wordOfTheDay('http://dictionary.reference.com/wordoftheday/')
