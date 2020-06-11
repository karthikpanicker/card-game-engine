from typing import Dict
import engine.constants as constants


class Game28Settings:
    settings: Dict[str,object] = { constants.MIN_BID_VALUE: 14}

    def set_setting_value(self, key: str, value):
        self.settings[key] = value

    def get_setting_value(self, key):
        return self.settings[key]