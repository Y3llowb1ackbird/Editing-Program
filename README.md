# Editing-Program
A program that edits and corrects a specific set of common style guide errors from the raw text of WordPress articles.

<h2>Running the Program: </h2>

It's pretty simple. Just copy the raw text of the file and then press ENTER to run the program or 'C' to run the program and add an 'Images from Shutterstock. Charts from TradingView' attribution. It will then copy the edited text to your clipboard, which you can then paste back into the raw text field.

Copy text from the next article and then press ENTER/'C' to run again, etc.

<h2>What it Does:</h2>

-Changes cryptocurrency names to lowercase: Bitcoin, Ethereum, Ether, Litecoin, Bitcoin Cash, Ripple price, Dash, Monero, Ethereum Classic, Stellar price, Tezos, Tron, TRON, Cardano, VeChain, Zcash, Blockchain.

- Removes < div > and < /div >
- Removes < span... > and < /span >
- Removes "&nbsp"
- Changes < b > and < /b > to < strong > and < /strong >
- Changes "%" to "percent"
- Changes < i > and < /i > to < em > and < /em >

<h2>Known Issues: </h2>

- Obviously the program cannot tell when the cryptocurrency name is capitalized correctly (ex. when referring to the "Bitcoin protocol"), so this will require some discretion.

- The program does not currently recognize when a word is the first word of a paragraph.
