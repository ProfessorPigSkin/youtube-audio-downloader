 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import pafy

from arguments_parser import get_arguments
from file_manager import FileManager


class YoutubeAudioDownloader(object):
    PATH_TO_SAVE = "."

    def __init__(self, path_file, path_to_save=None):
        self.path_file = path_file
        self.path_to_save = path_to_save or self.PATH_TO_SAVE

    @staticmethod
    def _get_links(path_file):
        return FileManager.get_links(path_file)

    def download_audios(self):
        links = self._get_links(self.path_file)
        for link in links:
            print(link)
            # video = pafy.new(link)
            # bestaudio = video.getbestaudio()
            # bestaudio.download(quiet=False, filepath=self.path_to_save)


if __name__ == "__main__":
    args = get_arguments()
    path_file = args.path_file
    path_to_save = args.path_to_save
    downloader = YoutubeAudioDownloader(path_file, path_to_save=path_to_save)
    downloader.download_audios()
