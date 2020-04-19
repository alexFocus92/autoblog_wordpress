# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 12:10:23 2020

@author: aleortega
"""


import pandas as pd
from googletrans import Translator

# %%

def auto_truncate(val):
    return val[:4999]

class NewsTranslated():
    def __init__(self, news_file):
        self.articulos = pd.read_csv(r"Data/ML_1.csv",sep = ';')
        #self.articulos = self.articulos[10:11]
        self.articulos = self.articulos.dropna(subset=['titulo', 'cuerpo'])
        self.articulos['cuerpo'] = self.articulos['cuerpo'].apply(auto_truncate)
    
    def translate(self):
        translator = Translator()
        self.articulos['titulo_traducido'] = self.articulos['titulo'].apply(translator.translate, src='en', dest='es').apply(getattr, args=('text',))
        
        self.articulos['cuerpo_traducido'] = self.articulos['cuerpo'].apply(translator.translate, src='en', dest='es').apply(getattr, args=('text',))
        return self.articulos
        
        
        
    def save_df(self):
        self.articulos.to_excel(r'DATA/ML1_translated'+".xlsx", encoding="utf-8")
        
        

   