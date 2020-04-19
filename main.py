#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:16:28 2020

@author: alejandroortega
"""
from scraping import News


#%%              EXTRACTION OF ARTICLES

urls_generales = ['https://www.elmundo.es/']

urls_especificas = ['https://towardsdatascience.com','https://machinelearningmastery.com','http://news.mit.edu/topic/machine-learning']

Extraccion = News()
Extraccion.get_url_news(lista_especifica=urls_especificas, lista_general=urls_generales, termino_filtrado='machine_lerning')
Extraccion.get_texts()
Extraccion.save_as_csv(r"DATA/ML_1")
Extraccion.save_as_xlsx(r"DATA/ML_1")

#%%   READ AND TRANSLATE FILE
articulos = []
articulos = pd.read_csv(r"DataScience_downloads/ML_1.csv",sep = ';')
#articulos = articulos[2:3]

articulos['cuerpo'] = articulos['cuerpo'].apply(auto_truncate)
# =============================================================================
#     TRANSLATE ARTICLES
# =============================================================================

translator = Translator()
articulos['titulo_traducido'] = articulos['titulo'].apply(translator.translate, src='en', dest='es').apply(getattr, args=('text',))

articulos['cuerpo_traducido'] = articulos['cuerpo'].apply(translator.translate, src='en', dest='es').apply(getattr, args=('text',))

articulos.to_excel(r'DataScience_downloads/ML1_translated'+".xlsx", encoding="utf-8")
articulos.to_csv(r'DataScience_downloads/ML1_translated'+".csv", encoding="utf-8", sep = ';')

# %%
for translation in articulos.cuerpo:
    print(translation.translator.translate)

a = translator.translate(articulos.titulo[10],src='en', dest='es')

#fin