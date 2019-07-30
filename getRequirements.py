from os import system 
req=open('requirements.txt','w')

# input("Cole aqui todas as linhas de código com imports")
libs = """from flask import Flask,request, render_template,redirect,url_for
import pandas as pd
import requests
from watson_developer_cloud import VisualRecognitionV3 
import json
import ast"""

libraries=[]
imps = libs.split('import')
imps = ' '.join(imps)
imps = imps.split('from')
for imp in imps:
    if imp != '' or imp != '\n':
        
        libs= imp.split(' ')
        
        for lib in libs:
            if lib != 'as' and lib != '' and lib != '\n' :
                if lib[len(lib)-1] == '\n' or lib[len(lib)-1] == ',':
                    lib = lib[:len(lib)-1]
                libraries.append(lib)
for lib in libraries:
    system('pip freeze | findstr '+lib)