# app_logic.py
#
# Copyright 2026 mBilG
#
# This is a python helper file to run some of the logic functions for the app
# '/app/share/pyquran/mushaf/old/dark_mode/1.png'

import os

import json
from gi.repository import GLib

class PageInfo:
    def __init__(self):
        pass

    def double_path_from_page(self, page=1, page_style="old", mode="dark_mode"):
        if page % 2 == 0: #even
            path_even = "/app/share/pyquran/mushaf/" + page_style + '/' + mode + '/' + f"{page:03}"+ '.png'
            path_odd = "/app/share/pyquran/mushaf/" + page_style + '/' + mode + '/' + f"{page-1:03}"+ '.png'
        else: #odd
            path_even = "/app/share/pyquran/mushaf/" + page_style + '/' + mode + '/' + f"{page+1:03}"+ '.png'
            path_odd = "/app/share/pyquran/mushaf/" + page_style + '/' + mode + '/' + f"{page:03}"+ '.png'
        page_path = (path_even, path_odd)
        return page_path

    def single_path_from_page(self, page=1, page_style="old", mode="dark_mode"):
        page_path = "/app/share/pyquran/mushaf/" + page_style + '/' + mode + '/' + f"{page:03}"+ '.png'
        return page_path

    def page_from_surah_index(self, surah_index):
        self.i = surah_index

class SaveState:
    def __init__(self, app_name="com.thinqrlab.pyQuran"):
        # Set up the private path for Flatpak/Linux
        self.data_dir = os.path.join(GLib.get_user_data_dir(), app_name)
        self.file_path = os.path.join(self.data_dir, "state.json")

    def load_page(self):
        """Returns the saved page number, or 1 if nothing is found."""
        if not os.path.exists(self.file_path):
            return 1

        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                return data.get("page", 1)
        except (IOError, json.JSONDecodeError):
            return 1

    def save_page(self, page_num):
        """Saves the page number to the private data folder."""
        os.makedirs(self.data_dir, exist_ok=True)
        with open(self.file_path, "w") as f:
            json.dump({"page": page_num}, f)


class GetIndex:
    @staticmethod
    def get_first_index(p, q):
        for i in range(len(p)):
            if p[i] > q:
                return i-1
        return len(p)
