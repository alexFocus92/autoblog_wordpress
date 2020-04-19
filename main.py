#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:16:28 2020

@author: alejandroortega
"""
from scraping import News
from news_translator import NewsTranslated
import pandas as pd

#%%              EXTRACTION OF ARTICLES

urls_generales = ['https://www.elmundo.es/']

urls_especificas = ['https://towardsdatascience.com','https://machinelearningmastery.com','http://news.mit.edu/topic/machine-learning']

Extraccion = News()
Extraccion.get_url_news(lista_especifica=urls_especificas, lista_general=urls_generales, termino_filtrado='machine_lerning')
Extraccion.get_texts()
Extraccion.save_as_csv("ML_1")
Extraccion.save_as_xlsx("ML_1")


# %%===========================================================================
#     TRANSLATE ARTICLES
# =============================================================================
noticias_ml = NewsTranslated(news_file = 'DATA/ML_1.csv')
a = noticias_ml.translate()

# %%
articulos = []
articulos = pd.read_csv(r"Data/ML_1.csv",sep = ';')
#articulos = articulos[2:3]
articulos = articulos.dropna(subset=['titulo', 'cuerpo'])

articulos['cuerpo'] = articulos['cuerpo'].apply(auto_truncate)


translator = Translator()
articulos['titulo_traducido'] = articulos['titulo'].apply(translator.translate, src='en', dest='es').apply(getattr, args=('text',))

#articulos['cuerpo_traducido'] = articulos['cuerpo'].apply(translator.translate, src='en', dest='es').apply(getattr, args=('text',))

articulos.to_excel(r'DATA/ML1_translated'+".xlsx", encoding="utf-8")
articulos.to_csv(r'DATA/ML1_translated'+".csv", encoding="utf-8", sep = ';')
