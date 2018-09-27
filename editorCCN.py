#! python 3
# searchAndReplace.py Simple automated find and replace program.

import pyperclip, re, sys

#To Do:
#Figure out how to capitalize the first letter of a paragraph




searchAndReplace = {
#Hardcoded Search and Replace Dictionary
	"Bitcoin Cash" : "bitcoin cash",
	"Ethereum Classic" : "ethereum classic",
	"Bitcoin" : "bitcoin",
	"Ethereum" : "ethereum",
	"Ether" : "ether",
	"Litecoin" : "litecoin",
	"Ripple price" : "ripple price",
	"Dash" : "dash",
	"Monero" : "monero",
	"Stellar price" : "stellar price",
	"Tezos" : "tezos",
	"Tron" : "tron",
	"TRON" : "tron",
	"Cardano" : "cardano",
	"VeChain" : "vechain",
	"Zcash" : "zcash",
	"Blockchain" : "blockchain"
	}

#Functions

def search_and_replace(text, edits, attribution):
	#Edits the article
	for item in edits.keys():
		text = re.sub(item, edits[item], text)

	text = re.sub("<div>", "", text)
	text = re.sub("</div>", "", text)
	text = re.sub("</span>", "", text)
	text = re.sub("<span style=\"font-weight: 400;\">", "", text)
	text = re.sub("<b>", "<strong>", text)
	text = re.sub("</b>", "</strong>", text)
	text = re.sub("<i>", "<em>", text)
	text = re.sub("</i>", "</em>", text)
	text = re.sub("\&nbsp\;", "", text)
	text = re.sub("<h2><strong>", "<h2>", text)
	text = re.sub("</h2></strong>", "</h2>", text)
	text = re.sub(r'(\. )([a-z])', capitalize, text)
	text = re.sub(r'([A-Z]\.[A-Z]\. )([A-Z])', fix_acronyms, text)
	text = re.sub(r'(<h*>)([a-z])', fix_headings, text)
	text = re.sub("%", " percent", text)

	if attribution == 1:
		text = text + ('\n\n<em>Featured Image from Shutterstock. Charts from <a href="https://www.tradingview.com/ideas/cryptocurrency/" target="blank" rel="nofollow">TradingView</a>.</em>')
	return text

def capitalize(m):
	#Capitalizes the first word of every sentence that follows a period.
	#Does not currently work for the first word of a paragraph
    return m.groups()[0] + m.groups()[1].upper()

def fix_acronyms(m):
	# Ensures that the first letter after "U.S." and "U.K." is lowercase.
	return m.groups()[0] + m.groups()[1].lower()

def fix_headings(m):
	#Ensures the first word of headings are capitalized
	return m.groups()[0] + m.groups()[1].upper()

#Variables

imageAttribution = 0

print(r'Instructions: Copy the raw text of the article to your clipboard.')
print(r'Press ENTER to run the program without an image attribution.')
print(r'''Enter 'C' to run the program and add an 'Images from Shutterstock and Charts from TradingView' attribution.
''')

while True:
	while True:
		answer = input()
		if answer == '':
			imageAttribution = 0
			break
		elif answer == 'c' or answer == 'C':
			imageAttribution = 1
			break
		elif answer == 'x' or answer == 'X':
			sys.exit()
		else:
			print('\nInvalid entry.')
			print(r'Press ENTER to run again without an attribution.')
			print(r'''Enter 'C' to run the program and add an 'Images from Shutterstock and Charts from TradingView' attribution.''')
			print(r'''Enter 'X' to Quit: ''')

	draft = str(pyperclip.paste())
	pyperclip.copy(search_and_replace(draft, searchAndReplace, imageAttribution))

	print(r'Edited text copied to clipboard.')
	print(r'Press ENTER to run again without an attribution.')
	print(r'''Enter 'C' to run the program and add an 'Images from Shutterstock and Charts from TradingView' attribution.''')
	print(r'''Enter 'X' to Quit: ''')
