# page_info.py
#
# Copyright 2026 mBilG
#
# This is a python helper file to get info for selected pages and other info manipulation for pages

from .quran_data import mushafVariant

import os
from pathlib import Path
from typing import Tuple, List


class GetPath:
    @staticmethod
    def single(self, page=1, variant=0):
        if variant == 0:
            data_path = "/app/share/pyquran/mushaf/"
        else:
            data_path = os.path.expanduser(f"~/.var/app/{os.environ.get('FLATPAK_ID')}/data/mushaf/")

        var = mushafVariant[variant]

        page_path = data_path + var +  f"/{page:03}"+ '.png'
        return page_path

get_path = GetPath()



class GetIndex:
    @staticmethod
    def get_first_index(p, q):
        for i in range(len(p)):
            if p[i] > q:
                return i-1
        return len(p)

get_index = GetIndex()



class CheckPath:
    @staticmethod
    def is_valid(self, variant_id):
        var = mushafVariant[variant_id]
        if variant_id == 0:
            data_path = "/app/share/pyquran/mushaf/"
        else:
            data_path = os.path.expanduser(f"~/.var/app/{os.environ.get('FLATPAK_ID')}/data/mushaf/")
        target = Path(data_path) / var

        if not target.is_dir():
            return False
        return True

check_path = CheckPath()


class CheckFolder:
    @staticmethod
    def is_valid(base_path: str) -> Tuple[bool, List[str]]:
        REQUIRED_SUBFOLDERS = mushafVariant
        REQUIRED_FILE_COUNT = 604

        issues = []
        top_dir = Path(base_path).resolve()

        if not top_dir.is_dir():
            top_dir.mkdir(parents=True, exist_ok=True)

        try:
            for folder_name in REQUIRED_SUBFOLDERS:
                target_subfolder = top_dir / folder_name
                if not target_subfolder.is_dir():
                    issues.append(f"{folder_name}")
                    continue
                actual_count = sum(1 for item in target_subfolder.iterdir()
                                   if item.is_file() and not item.name.startswith('.'))
                if actual_count != REQUIRED_FILE_COUNT:
                    issues.append(f"{folder_name} ({actual_count}/{REQUIRED_FILE_COUNT} files)")

        except (PermissionError, OSError) as e:
            return False, [f"Access error: {str(e)}"]

        is_valid = len(issues) == 0
        return is_valid, issues

check_folder = CheckFolder()
