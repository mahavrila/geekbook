#!/usr/bin/python
# -*- coding: utf-8 -*-
# I'm working on this.Trying to cope with the pre processing of the MD file.

import codecs
from engine.conf import PATH_TO_MD, SCREENSHOT_INBOX, PATH_TO_IMG, IMG_PREFIX
from engine.preprocessing import right_link_from_dropbox_screenshot, get_ss
from engine.plugins.insert_image import insert_image_in_md
from os import sep


import logging
logger = logging.getLogger('geekbook')


class Md_update(object):
    """Md_update class

    Attributes:

      fn
      md
    This class is responsible for the changes operated directly on the MD file.
    For example replacing some patterns with MarkDown language.
    """

    def __init__(self, fn):
        """Init a Page and load the content of MD file into self.md"""
        self.fn = fn
        with codecs.open(PATH_TO_MD + sep + fn, "r", "utf-8") as f:
            self.md = f.read()

    def compile(self):
        """Preprocess, compile, postprocess.
        """
        self.md = get_ss(self.md)
        if SCREENSHOT_INBOX:
            self.md = insert_image_in_md(self.md, SCREENSHOT_INBOX, PATH_TO_IMG, IMG_PREFIX)
        self.md = right_link_from_dropbox_screenshot(self.md)

    def save(self):
        with codecs.open(PATH_TO_MD + sep + self.fn, "w", "utf-8") as outfn:
            outfn.write(self.md)

if __name__ == '__main__':
    fin = 'test.md'

    m = Md_update(fin)
    m.compile()
    m.save()
