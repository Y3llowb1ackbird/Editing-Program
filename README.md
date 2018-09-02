# Editing-Program
A program that edits and corrects a specific set of common style guide errors from the raw text of WordPress articles.

<h2>Running the Program: </h2>

It's pretty simple. Just copy the raw text of the file and then press ENTER to run the program. It will then copy the edited text to your clipboard, which you can then paste back into the raw text field.

Copy text from the next article and then press ENTER to run again, etc.

<h2>What it Does:</h2>

-Changes cryptocurrency names to lowercase: Bitcoin, Ethereum, Ether, Litecoin, Bitcoin Cash, Ripple price, Dash, Monero, Ethereum Classic, Stellar price, Tezos, Tron, TRON, Cardano, VeChain, Zcash.

- Removes < div > and < /div >
- Removes < span... > and < /span >
- Changes < strong > and < /strong > to < b > and < /b >

<h2>Known Issues: </h2>

- Obviously the program cannot tell when the cryptocurrency name is capitalized correctly (ex. when referring to the "Bitcoin protocol"), so this will require some discretion.

- The program does not currently recognize when a word is the first word of a sentence or paragraph, so you will need to read through and fix any of these errors that the program causes (don't forget about section headers).
