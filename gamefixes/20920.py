""" Witcher 2
"""
#pylint: disable=C0103

from protonfixes import util
import multiprocessing


def main():
    """ Witcher 2 chokes on more than 31 cores
    """

    if multiprocessing.cpu_count() > 24:
        util.set_environment('WINE_CPU_TOPOLOGY', '31:0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30')

