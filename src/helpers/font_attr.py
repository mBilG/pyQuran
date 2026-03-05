# font_attr.py
#
# Copyright 2026 mBilG
#
# This is a python helper file to generate font attributes

from gi.repository import Pango

class FontAttr:
    @staticmethod
    def make_font_attrs(self, family: str, size_pt: int) -> Pango.AttrList:
        attrs = Pango.AttrList()
        # Font family
        family_attr = Pango.attr_family_new(family)
        attrs.insert(family_attr)
        # Font size is in Pango units (points * Pango.SCALE)
        size_attr = Pango.attr_size_new(int(size_pt * Pango.SCALE))
        attrs.insert(size_attr)
         # Bold
        attrs.insert(Pango.attr_weight_new(Pango.Weight.BOLD))
        return attrs


    def font_list(self):
        font_list = (
            "(A) Arslan Wessam A",
            "(A) Arslan Wessam B",
            "Amiri Quran",
            "Amiri",
            "Aref Ruqaa Ink",
            "Aref Ruqaa",
            "KFGQPC Uthmanic Script HAFS",
            "Qahiri",
            "Rakkas",
            "Reem Kufi Ink",
            "Scheherazade"
            )
        return font_list


font_attr = FontAttr()
