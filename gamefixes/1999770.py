""" Atelier Ryza 3: Alchemist of the End & the Secret Key
Missing voices/sounds in cutscenes
Requires disabling the gstreamer protonaudioconverterbin plugin to get full audio in cutscenes
"""

#pylint: disable=C0103

from protonfixes import util

def main():
    util.set_environment('GST_PLUGIN_FEATURE_RANK', 'protonaudioconverterbin:NONE')
