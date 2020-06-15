from typing import Dict
import engine.constants as constants


class Game28Settings:
    settings: Dict[str,object] = { constants.MIN_BID_VALUE: 14,
                                   constants.FIRST_ROUND_HONORS_MIN: 20,
                                   constants.SECOND_ROUND_HONORS_MIN: 22,
                                   constants.VALIDATE_GAME_PLAY: True}

    def set_setting_value(self, key: str, value):
        self.settings[key] = value

    def get_setting_value(self, key):
        return self.settings[key]