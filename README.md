# autodepart
A bot that plays Shipping Manager for you by automatically departing your ships.

# Requirements
1. Windows (Sorry Linux/SteamOS users, port coming eventually?)
2. Python - [Download here](https://www.python.org/downloads/) (make sure you install to PATH)
3. Steam - [Download here](https://store.steampowered.com/about/)
4. Shipping Manager installed via Steam - [Steam store page](https://store.steampowered.com/app/2445660/Shipping_Manager/)
5. A Shipping Manager account and game set up and running (obviously)

# How to use

1. Download this repo (green button that says code + download zip. Extract the zip)
2. Open a terminal in the folder you downloaded and extracted (right click + open terminal in file explorer)
3. Install dependencies: `pip install -r requirements.txt`
4. Make sure steam is open and running on your computer. (Don't have shipping manager running, however.)
5. run the bot: `python bot.py`

# Notes

* This bot isn't perfect, for example it isn't currently able to buy CO2 or fuel, so you will have to open the game manually and refill those from time to time (might add this feature in the future)
* This is useful if you want to maximize your profits while asleep IRL (fill up your fuel and CO2 before bed and then leave it running overnight)
* The bot will quit the game after departing ships and re-launch it when it needs to depart again. I did this for two reasons - 1. It allows you to do other things on your computer during the delay, and 2. So you won't get like 200 hours on Steam after leaving the bot running overnight lmao
* Everything the bot does is stored in a handy log file, so you can see if anything went wrong while you were asleep.

# Disclaimer

Using this bot may go against Shipping Manager's rules. Please use responsibly. I am not responsible for your use or misuse of this bot.
