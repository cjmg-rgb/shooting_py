from settings import *
from config import Config

class Game:
    def __init__(self):
        self.config = Config(os.path.join("./settings.json"))
        print(self.config.get("WIDTH"))
        print(self.config.get("TEST")["YEAH"])