# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 12:10:23 2020

@author: aleortega
"""


import pandas as pd
from googletrans import Translator
from google.cloud import translate_v2 as translate
import time


# %%

def auto_truncate(val):
    return val[:9999]

class NewsTranslated():
    def __init__(self, news_file):
        self.articulos = pd.read_csv(r"Data/ML_1.csv",sep = ';')
        self.articulos = self.articulos[:50]
        self.articulos = self.articulos.drop_duplicates(subset='titulo', keep="first")
        self.articulos = self.articulos.dropna(subset=['titulo', 'cuerpo'])
        self.articulos['cuerpo'] = self.articulos['cuerpo'].apply(auto_truncate)
        self.translate_client = translate.Client()
        
       
    def translate_articles_df(self):
        print("==============================================================")
        print("              TRANSLATING NEWS WITH GOOGLE API                ")
        print("==============================================================")
        self.df_traducidos = pd.DataFrame(columns=["periodico","url","fecha","titulo","cuerpo","titulo_traducido","cuerpo_traducido"])
        
        for index, row in self.articulos.iterrows():
            try:
                tr_titulo= row['titulo']
                tr_cuerpo= row['cuerpo']
                time.sleep(0.5)
                target = 'es'
                translation = self.translate_client.translate(tr_titulo,target_language=target)
                tr_titulo = format(translation['translatedText'])
                
                translation = self.translate_client.translate(tr_cuerpo,target_language=target)
                tr_cuerpo = format(translation['translatedText'])
    
                self.df_traducidos = self.df_traducidos.append({"periodico": row['periodico'], 
                                                      "url":row['url'], 
                                                      "fecha":row['fecha'], 
                                                      "titulo": row['titulo'],
                                                      "cuerpo":row['cuerpo'],
                                                      "titulo_traducido" : tr_titulo, 
                                                      "cuerpo_traducido": tr_cuerpo}, ignore_index = True)
                
                if index % 10 == 1:
                    print("Noticia Nº: " + str(index) + " Traducida")

            except Exception as err:
                time.sleep(10)
                print("Error al traducir noticia Nº: " + str(index))
                
        return self.df_traducidos
        
    def save_df(self):
        print("==============================================================")
        print("                      SAVING EXCEL AND CSV                    ")
        print("==============================================================")
        self.df_traducidos.to_excel(r'DATA/ML1_translated'+".xlsx", encoding="utf-8")
        self.df_traducidos.to_csv(r'DATA/ML1_translated'+".csv", encoding="utf-8", sep = ';')


    















