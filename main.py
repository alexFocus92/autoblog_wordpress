#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:16:28 2020

@author: alejandroortega
"""
from scraping import News
from news_translator import NewsTranslated
import pandas as pd
             
# %%==========================================================================
#                               EXTRACTION OF ARTICLES
# =============================================================================
urls_generales = ['https://www.elmundo.es/']

urls_especificas = ['https://towardsdatascience.com','https://machinelearningmastery.com','http://news.mit.edu/topic/machine-learning']

Extraccion = News()
Extraccion.get_url_news(lista_especifica=urls_especificas, lista_general=urls_generales, termino_filtrado='machine_lerning')
Extraccion.get_texts()
Extraccion.save_as_csv("ML_1")
Extraccion.save_as_xlsx("ML_1")


# %% ==========================================================================
#                              TRANSLATE ARTICLES
# =============================================================================
noticias_ml = NewsTranslated(news_file = 'DATA/ML_1.csv')
df_traducidos = noticias_ml.translate_articles_df()
noticias_ml.save_df()
