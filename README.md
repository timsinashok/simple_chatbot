# Quickstart

* To get a quick response, join our [Discord channel](https://discord.com/invite/YfrVwBtYWb).
* Visit the [Chai Docs](https://chai.ml/docs) for more information.


## Installation
`pip install chaipy`

## Getting Started
1. Visit [Chai](https://chai.ml/links/share-app/) - download the Chai app on your iPhone or Android device. 
2. Visit [Chai Developer Platform](https://chai.ml/dev).
3. Sign in.
4. Scroll to the bottom to see your "Developer Unique ID" (referred to as `developer_uid` in this tutorial) and your "Developer Key".
5. Git clone this starter repo. `git clone https://github.com/chai-nexus/chai_quickstart.git`

## Setting your DEVELOPER_KEY and DEVELOPER_UID
1. `cd chai_quickstart`
2. Open the file `uploader.py` using your text editor.

```python

DEVELOPER_UID = None # SET THIS VALUE
DEVELOPER_KEY = None # SET THIS VALUE

if DEVELOPER_KEY is None or DEVELOPER_UID is None:
    raise RuntimeError("Please fetch your UID and KEY from the bottom of the Chai Developer Platform. https://chai.ml/dev")

```

3. You must set your `DEVELOPER_UID` and `DEVELOPER_KEY`. Save and exit this file.
4. Let’s take a look at our starter bot in the file `starter_bot.py` and set our first message. Change "Hi I’m an ExampleBot" to "I love AI" then save and exit the file.
```python
from chai_py import ChaiBot, Update

class Bot(ChaiBot):
    def setup(self):
        self.logger.info("Setting up...")

    async def on_message(self, update: Update) -> str:
        return "Hi, I'm ExampleBot." # EDIT THIS MESSAGE
```

5. Now lets upload our bot! Simply run `python uploader.py`.
6. Press Y when prompted, as this is a new bot. Next time we will press N.
7. You’ll get a QR code. First install the Chai app, and then scan the QR code. This will allow you to open the app so you can speak to your chat AI.
8. Chat with your bot! 

# Learn More
Visit the [Chai Docs](https://chai.ml/docs) for more information.

Join our [Discord channel](https://discord.com/invite/YfrVwBtYWb).

Have fun building!
