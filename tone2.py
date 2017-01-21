#!/usr/bin/python

import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
   username='1de7eb5b-0ec9-4df7-b886-28871372850c',
   password='Aptofapeo3kh',
   version='2016-05-19')

import sys, getopt

def runscript(s1, s2):
   inputfile = ''
   outputfile = ''
   
   if s1 != '':
      inputfile = s1
   if s2 != '':
      outputfile = s2

   input = open(inputfile, "r")
   firstline = input.readline().rstrip()
   firstline = firstline.split(",")
   songtitle = '\t"songtitle": "' + firstline[0][:-1] + '",\n'
   artist = '\t"artist": "' + firstline[1][1:] + '",\n'
   parsetext = input.read()
   
   if outputfile != '':
      output = open(outputfile, "w")
      output.write("{\n")
      output.write(songtitle)
      output.write(artist)
      output.write(json.dumps(tone_analyzer.tone(text=parsetext)['document_tone'], indent=2)[2:])
      output.close()
   else:
      print(json.dumps(tone_analyzer.tone(text=parsetext)['document_tone'], indent=2))

   input.close()
