import sys
import os.path
from os import path
import argparse
import analysis
import calculateHealthIndicators as chi
import numpy

def dir_path(pathName):
    if os.path.isfile(pathName):
        return pathName
    else:
        raise IsADirectoryError(pathName)

parser = argparse.ArgumentParser(
    description='COR AL PIT is a program that given images determine if your heart is healthy or not.',
    epilog="Example of use: python .\main.py -pl '<path_to_PSLA>' -ps '<path_to_SAX>'")

parser.add_argument('-pl','--pathpsla', type=dir_path, help= "the path to the dicom file of PSLA", required=True)
parser.add_argument('-ps','--pathsax', type=dir_path, help= "the path to the dicom file of SAX", required=True)

def parse():
    return parser.parse_args()

def usage_help():
    return parser.print_help()

def main(path):
    print(path)


if __name__ == '__main__':
    args = parser.parse_args()

    print('Analyzing PSLA ......')
    psla = analysis.analyze_video(args.pathpsla)
    print('Analysis done.')

    print('Analyzing SAX ......')
    sax = analysis.analyze_video(args.pathsax, psla=False)
    print('Analysis done.')

    
    chi.calculateAll(psla.top_d, 
                    psla.top_s ,
                    numpy.mean([psla.mid_d]),
                    numpy.mean([psla.mid_s]), 
                    numpy.mean([psla.bot_d]),
                    numpy.mean([psla.bot_s]),
                    1,
                    1,numpy.mean([psla.hr,sax.hr]))