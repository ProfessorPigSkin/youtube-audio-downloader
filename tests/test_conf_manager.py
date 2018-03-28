import os
import unittest

from sound_downloader.conf_manager import ConfManager


class TestConfManager(unittest.TestCase):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CONF_FILE_PATH = os.path.join(BASE_DIR, os.pardir, "examples", "conf.yml")
    EXPECTES_RESULTS = {
        "links": [
            "https://www.youtube.com/watch?v=hTWKbfoikeg",
            "https://www.youtube.com/watch?v=ygYYOeVoVgk"
        ],
        "audio_formats": ['mp4', 'mp3', 'webm', 'm4a', 'ogg', 'wma']
    }

    def test_get_conf(self):
        conf = ConfManager.get_conf(self.CONF_FILE_PATH)
        self.assertEquals(
            conf.links, self.EXPECTES_RESULTS.get('links'))
        self.assertEquals(
            conf.audio_formats,
            self.EXPECTES_RESULTS.get('audio_formats')
        )
