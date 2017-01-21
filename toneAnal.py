#!/usr/bin/python

import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
   username='1de7eb5b-0ec9-4df7-b886-28871372850c',
   password='Aptofapeo3kh',
   version='2016-05-19')

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   
   input = open(inputfile, "r")
   parsetext = input.read();
   
   if outputfile != '':
      output = open(outputfile, "w")
      output.write(json.dumps(tone_analyzer.tone(text=parsetext)['document_tone'], indent=2))
      output.close()
   else:
      print(json.dumps(tone_analyzer.tone(text=parsetext), indent=2))

   input.close()

if __name__ == "__main__":
   main(sys.argv[1:])
