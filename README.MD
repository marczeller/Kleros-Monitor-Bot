# Kleros-Monitor-Bot
Simple Kleros case monitor bot


# Setup
```
git clone https://github.com/marczeller/Kleros-Monitor-Bot.git
cd Kleros-Monitor-Bot/
export ETH_NODE_URL="https://mainnet.infura.io/v3/31c378f901bf46c08674e655e6640287"
./monitor.py CASENUMBER
```
Just input your [Kleros.io](https://kleros.io) case number and the bot will do the fun part.

your monitor window should look like this during the installation process exemple with CASENUMBER = 17:

![setup_exemple_last.JPG](https://github.com/marczeller/Kleros-Monitor-Bot/blob/master/setup_exemple_last.JPG)

### How to get the case ID?

1. Visit the token you want to check: https://tokens.kleros.io/token/0xabe49ddffcac5ab14ca0fad9dc865beae1f1cde898e89a927c9bb4493e024adc

2. Get the long name from URL: `0xabe49ddffcac5ab14ca0fad9dc865beae1f1cde898e89a927c9bb4493e024adc`


3. Read contract on Etherscan: https://etherscan.io/address/0xebcf3bca271b26ae4b162ba560e243055af0e679#readContract

![](etherscan_dispute_id.png?raw=true)


# common bug fix

*You don't have web3 :*

![Bug exemple.JPG](https://github.com/marczeller/Kleros-Monitor-Bot/blob/master/Bug%20exemple.JPG)

we gonna assume that you don't have anything required, let's do that.
it's a bit longer but don't worry you only need to do that once

```
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
pip3 install web3
```
*I'm on windows OS i can't do stuff like this ! :*

Yes you do, Windows10 has a fancy ubuntu emulator.
just check the windows store, type "Ubuntu" and select Ubuntu 18.04 LTS.
you'll just need to follow the *You don't have web3 :* process then follow the regular setup steps.

# what is Kleros ?

Kleros is a Decentralized Dispute Resolution System to learn more about it, [read their blog posts](https://blog.kleros.io/)

# Donations
the best kind of support is opening up issues and proposing PRs this is a prototype MVP, we can do much better!!

For the other kind of support : marczeller.eth (0x010afb8548a5D1a3a3D62f58CA0a5A1329974206)
