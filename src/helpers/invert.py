# invert.py
#
# Copyright 2026 mBilG
#
# This is a python helper file to invert images

import numpy as np
from gi.repository import Gdk, GdkPixbuf, GLib

def get_texture(file_path, invert=False):
    # Gdk.Texture.new_from_file is thread-safe and faster than Pixbuf for basic loads
    if not invert:
        from gi.repository import Gio
        return Gdk.Texture.new_from_file(Gio.File.new_for_path(file_path))

    pixbuf = GdkPixbuf.Pixbuf.new_from_file(file_path)
    width, height = pixbuf.get_width(), pixbuf.get_height()
    stride = pixbuf.get_rowstride()
    has_alpha = pixbuf.get_has_alpha()

    # NumPy's '255 - arr' is already near-peak performance for this operation
    arr = np.frombuffer(pixbuf.get_pixels(), dtype=np.uint8).copy()

    if has_alpha:
        view = arr.reshape((height, stride))[:, :width * 4].reshape((height, width, 4))
        view[:, :, :3] = 255 - view[:, :, :3]
    else:
        view = arr.reshape((height, stride))[:, :width * 3].reshape((height, width, 3))
        view[:] = 255 - view

    return Gdk.MemoryTexture.new(
        width, height,
        Gdk.MemoryFormat.R8G8B8A8 if has_alpha else Gdk.MemoryFormat.R8G8B8,
        GLib.Bytes.new(arr.tobytes()),
        stride
    )

