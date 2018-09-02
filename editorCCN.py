#! python 3
# searchAndReplace.py Simple automated find and replace program.

import pyperclip, re, sys

searchAndReplace = {
	"Bitcoin" : "bitcoin",
	"Ethereum" : "ethereum",
	"Ether" : "ether",
	"Litecoin" : "litecoin",
	"Bitcoin Cash" : "bitcoin cash",
	"Ripple price" : "ripple price",
	"Dash" : "dash",
	"Monero" : "monero",
	"Ethereum Classic" : "ethereum classic",
	"Stellar price" : "stellar price",
	"Tezos" : "tezos",
	"Tron" : "tron",
	"TRON" : "tron",
	"Cardano" : "cardano",
	"VeChain" : "vechain",
	"Zcash" : "zcash"
	}

def search_and_replace(text, edits):
    for item in edits.keys():
        text = re.sub(item, edits[item], text)
        text = re.sub("<div>", "", text)
        text = re.sub("</div>", "", text)
        text = re.sub("</span>", "", text)
        text = re.sub("<span style=\"font-weight: 400;\">", "", text)
        text = re.sub("<strong>", "<b>", text)
        text = re.sub("</strong>", "</b>", text)
    return text

while True:
    draft = str(pyperclip.paste())
    pyperclip.copy(search_and_replace(draft, searchAndReplace))
    
    print('Edited text copied to clipboard.\nPress ENTER to Run Again or \'X\' to Quit.')
    while True:
        answer = input()
        if answer == '':
            break
        elif answer == 'x' or answer == 'X':
            sys.exit()
        else:
            print('Invalid entry. Press ENTER to continue or \'X\' to quit.')

