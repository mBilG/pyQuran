# downloader.py
#
# Copyright 2026 mBilG
#
# This handles the download and extraction of files


import os
import shutil
import zipfile
import urllib.request
from gi.repository import GLib

class FileDownloader:
    def __init__(self, url, zipname, cache_dir, status_widget):
        self.url = url
        self.cache_dir = cache_dir
        self.status_widget = status_widget
        self.zip_path = os.path.join(cache_dir, f"{zipname}.zip")
        self._is_cancelled = False

    def cancel(self):
        self._is_cancelled = True
        if os.path.exists(self.cache_dir):
            shutil.rmtree(self.cache_dir)

    def _update_ui(self, text):
        self.status_widget.set_subtitle(text)
        return False

    def run(self):
        os.makedirs(self.cache_dir, exist_ok=True)
        try:
            # Using urllib instead of requests
            req = urllib.request.Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                total = int(response.headers.get('Content-Length', 0))
                downloaded = 0

                with open(self.zip_path, 'wb') as f:
                    while True:
                        if self._is_cancelled: return False
                        chunk = response.read(1024 * 1024) # 1MB chunk
                        if not chunk: break

                        f.write(chunk)
                        downloaded += len(chunk)

                        percent = int(100 * downloaded / total) if total else 0
                        mb = downloaded / (1024 * 1024)
                        GLib.idle_add(self._update_ui, f"Downloading: {mb:.1f} MB")
            return True
        except Exception as e:
            GLib.idle_add(self._update_ui, f"Download Error: {str(e)}")
            return False

class FileExtractor:
    def __init__(self, cache_dir, data_dir, zipname, status_widget):
        self.zip_path = os.path.join(cache_dir, f"{zipname}.zip")
        self.data_dir = data_dir
        self.status_widget = status_widget
        self._is_cancelled = False

    def _update_ui(self, text):
        self.status_widget.set_subtitle(text)
        return False

    def cancel(self):
        self._is_cancelled = True
        if os.path.exists(self.data_dir):
            shutil.rmtree(self.data_dir)

    def run(self):
        if not os.path.exists(self.zip_path): return False
        os.makedirs(self.data_dir, exist_ok=True)
        try:
            with zipfile.ZipFile(self.zip_path, 'r') as z:
                members = z.infolist()
                total = len(members)
                zip_size_mb = os.path.getsize(self.zip_path) / (1024 * 1024)

                for i, member in enumerate(members):
                    if self._is_cancelled: return False

                    # Split the path (githubname-branch/actual_folder/file)
                    parts = member.filename.split('/', 1)

                    # If there's a sub-path after the GitHub root folder
                    if len(parts) > 1 and parts[1]:
                        # Reconstruct path without the first part (githubname-branch)
                        member.filename = parts[1]
                        z.extract(member, self.data_dir)

                    percent = int(100 * (i + 1) / total)
                    GLib.idle_add(self._update_ui, f"Extracting: {percent}% ({zip_size_mb:.1f} MB)")
            return True
        except Exception as e:
            GLib.idle_add(self._update_ui, f"Extraction Error: {str(e)}")
            return False
