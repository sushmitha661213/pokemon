# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 23:21:08 2017

@author: Suchi
"""


import requests
import webbrowser as wb
import json
import speech_recognition as sr
R = sr.Recognizer()
#speech input
with sr.Microphone() as voice:
   print "Say Pokemon name"
   audio = R.listen(voice)
try:
    img = (R.recognize_google(audio))
except:
    pass

print img
img=img.replace(" ","-")

#PokeAPI
site = "http://pokeapi.co/api/v2/pokemon/"+img.lower()+"/"
print site
hdr = {'User-Agent':'Mozilla/5.0'}

sreq = requests.get(site , headers=hdr)
#Displaying in webbrowser
if(sreq.status_code==200):
    #print sreq.headers['content-type']
    #print sreq.text
    
    ImageUrl = json.loads(sreq.text)['sprites']['back_default']
    wb.open(ImageUrl)
else:
    print "ERROR:Image doen't exist"

