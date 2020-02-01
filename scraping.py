#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 22:39:47 2019

@author: alejandroortega
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:23:58 2019

@author: alejandro.ortega.or1
"""

#%% Libreries
import newspaper
from newspaper import Article
import pandas as pd
from datetime import datetime
from time import time
from googletrans import Translator

#%% Functions definitions

def extraction(url, no_valid_url):
    try:
        article = Article(url, fetch_images=False)
        article.download()
        article.parse()
    except Exception as err:
        no_valid_url += 1
        print("{} no valid urls until now".format(no_valid_url))
    return article

def auto_truncate(val):
    return val[:4999]

#%% Class definition

class News(object):

    def __init__(self):
        self.url_news = list()
        self.texts = pd.DataFrame(columns=["periodico","url","fecha","titulo","cuerpo"])

    def get_url_news(self, lista_general=None, lista_especifica=None, termino_filtrado=None):

        self.url_news = list()
        list_aux = list()

        #Extraccion para periodicos genericos

        for webpage in lista_general:
            web_page = newspaper.build(webpage,memoize_articles=False, language = 'es')
            aux = web_page.article_urls()
            list_aux += [i for i in aux if termino_filtrado in i] #extract only by "economia"

        #Extraccion para periodicos especificos (no hay filtrado)

        for webpage in lista_especifica:
           web_page = newspaper.build(webpage,memoize_articles=False, language = 'es')
           aux = web_page.article_urls()
           list_aux += [i for i in aux]

        #divide webpages by containing 'html' or not to delete comments or other stuff
        list_aux1 = [i for i in list_aux if 'html' in i]
        list_aux2 = [i for i in list_aux if 'html' not in i]
        list_aux1 = [i[0:(i.index('html')+4)] for i in list_aux1] #remove comments or stuff
        self.url_news = list(set(list_aux1+list_aux2)) #combine again the two
        print("\nProceso finalizado. \n{} urls han sido extraidas".format(len(self.url_news)))


    def get_texts(self):
        self.texts = pd.DataFrame(columns=["periodico","url","fecha","titulo","cuerpo"])
        no_valid_url = 0


        for pos,url in enumerate(self.url_news):
            try:
                article = Article(url, fetch_images=False, language = 'es')
                article.download()
                article.parse()

                date = article.publish_date
                if date is not None:
                    date = article.publish_date.strftime("%Y-%m-%d")
                else:
                    date = ''

                if (len(article.text) > 500):
                    self.texts = self.texts.append({"periodico": article.url.split("//")[1].split("/")[0], "url":article.url, "fecha":date, "titulo": article.title, "cuerpo":article.text}, ignore_index = True)

            except Exception as err:
                no_valid_url += 1


        print("\nProceso finalizado\n{} urls no han podido ser procesadas".format(no_valid_url))
        print("\n{} noticias han sido descargadas".format(self.texts.shape[0]))

    def save_as_csv(self,filename):
        #date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.texts.to_csv(filename+".csv", encoding="utf-8", sep = ';')

    def save_as_pkl(self,filename):
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.texts.to_pickle(date+"_"+filename+".pkl", encoding="utf-8")

    def save_as_xlsx(self,filename):
        #date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.texts.to_excel(filename+".xlsx", encoding="utf-8")

#%%              EXTRACTION OF ARTICLES

urls_generales = ['https://www.elmundo.es/']

urls_especificas = ['https://towardsdatascience.com','https://machinelearningmastery.com','http://news.mit.edu/topic/machine-learning']

Extraccion = News()
Extraccion.get_url_news(lista_especifica=urls_especificas, lista_general=urls_generales, termino_filtrado='machine_lerning')
Extraccion.get_texts()
Extraccion.save_as_csv(r"DataScience_downloads/ML_1")
Extraccion.save_as_xlsx(r"DataScience_downloads/ML_1")

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

