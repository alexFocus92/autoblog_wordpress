#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:56:44 2019

@author: alejandroortega
"""

#https://parzibyte.me/blog/2018/01/22/gestionando-sitio-blog-api-wordpress-python/



#%%

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts,media
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.compat import xmlrpc_client
import os
import re
import pandas as pd
import config

#LAST_PUBLICED = 14

comando_para_limpiar_pantalla = "clear" #Si estás en otro sistema cámbialo al comando correcto (en Linux es clear, en Windows es cls)

#%%

def pagina_wordpres_old(site = '***************'):
    if site == '************':
        usuario = "*************"
        contraseña = "*************"
        sitio = "**************/xmlrpc.php"
    else:
        usuario = '**************'
        contraseña = '************'
        sitio = '************/xmlrpc.php'
    cliente = Client(sitio, usuario, contraseña)
    return cliente

def pagina_wordpres(site = 'Aprende Data Science'):
    if site == 'd************':
        usuario = "************"
        contraseña = "************"
        sitio = "************/xmlrpc.php"
    else:
        usuario = '************'
        contraseña = '************'
        sitio = '************//xmlrpc.php'
    cliente = Client(sitio, usuario, contraseña)
    return cliente

def limpiar_pantalla():
    os.system(comando_para_limpiar_pantalla)

def limpiar_html(html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', html).strip()
    return cleantext

def pedir_datos_nueva_entrada():
    limpiar_pantalla()
    nueva_entrada = WordPressPost()
    nueva_entrada.title = input("Ingresa el título de la entrada: ")
    nueva_entrada.content = input("Ingresa todo el contenido de la entrada: ")
    etiquetas = []
    categorias = []
    eleccion = input("¿Deseas agregar etiquetas? [S/N] ")
    if eleccion.lower() == "s":
        etiquetas = input("Ingresa las etiquetas separadas con comas: ").split(",")
    eleccion = input("¿Deseas agregar categorías? [S/N] ")
    if eleccion.lower() == "s":
        categorias = input("Ingresa las categorías separadas con comas: ").split(",")
    nueva_entrada.terms_names = {
            'post_tag': etiquetas,
            'category': categorias,
    }
    print("Publicando entrada...")
    id_entrada_publicada = cliente.call(posts.NewPost(nueva_entrada))
    limpiar_pantalla()
    print("Correcto! Se guardó la entrada como borrador, y su id es {}".format(id_entrada_publicada))
    eleccion = input("¿Publicar inmediatamente? [S/N] ")
    if eleccion.lower() == "s":
        print("Publicando entrada...")
        nueva_entrada.post_status = 'publish'
        resultado = cliente.call(posts.EditPost(id_entrada_publicada, nueva_entrada))
        if resultado is True:
            input("Entrada publicada")
        else:
            input("Algo salió mal")
    imprimir_menu_opciones()

def crear_nueva_entrada_automatica():

    limpiar_pantalla()
    nueva_entrada = WordPressPost()
    num = int(input("Introduce el ID del post que quieres publicar: "))
    articulos = []
    articulos = pd.read_csv('travel_translated.csv',sep = ';')
    nueva_entrada.title = articulos.titulo_traducido[num]
    nueva_entrada.content = articulos.cuerpo_traducido[num]

    ############       AUTOMATIZAR LA SUBIDA DE IMAGENES      ############
    filename = 'downloads/travel_images_2/travel_' + str(num) + '.jpg'
    # prepare metadata
    data = {'name': 'picture.jpg', 'type': 'image/jpeg',}
    # read the binary file and let the XMLRPC library encode it into base64
    with open(filename, 'rb') as img:
        data['bits'] = xmlrpc_client.Binary(img.read())
    response = cliente.call(media.UploadFile(data))
    attachment_id = response['id']
    nueva_entrada.thumbnail = attachment_id
    ####################### ####################### #######################

    etiquetas = []
    categorias = []
    eleccion = input("¿Deseas agregar etiquetas? [S/N] ")
    if eleccion.lower() == "s":
        #etiquetas = input("Ingresa las etiquetas separadas con comas: ").split(",")
        etiquetas = ["viajar,carrefour,baratos,viajeros piratas,halcon,viaje al cuarto de una madre,barcelo,viaje al centro de la tierra,sorpresa,viaje sorpresa,viaje a cuba,viaje a nueva york,viaje a egipto,viajera del tiempo,viajem,todo incluido,viajera soledad,viajera,agencia,viaje en el tiempo,corte ingles,viaje largo,viaje barato,viaje budapest,viaje bali,viaje berlin,viaje barcelona,viaje bora bora,viaje bruselas brujas gante,viaje barato a roma,viaje bahamas,viaje barato semana santa,the travel brand pamplona,viajeras b,viajeras con b,viaje b alfa romeo,mundo,the travel brand valladolid,viajeros b travel brand,viaje canarias,viaje costa oeste eeuu,viaje cuba,viaje costa rica,viaje corte ingles,viaje croacia,viaje cerdeña,viaje caribe,viaje con niños,viaje con nosotros,viajeros c,m&c  turismo quilmes,jota c ,d.c.  y turismo s.a,at&c  mar del plata,viaje de chihiro,viaje de novios,viaje disney,viaje del heroe,viaje disneyland,viaje de magallanes,viaje disney paris,viaje de arlo,viaje destino sorpresa,viaje dubai,viaje destinos,san juan,viaje club,gaitan,san juan estafa,de viaje destinos san juan,turismo,tour.com,d-viaje vitoria,viaje egipto,viaje en el tiempo,viaje en globo madrid,viaje eurodisney,viaje en ingles,viaje en globo segovia,viaje en tren,viaje express,viajero,viaje de chihiro,viaje mas largo,viaje del heroe,viaje de arlo,operadora sa de cv veracruz,ideas,el tiempo,viaje fin desemana,playa,montaña"]
    eleccion = input("¿Deseas agregar categorías? [S/N] ")
    if eleccion.lower() == "s":
        categorias = input("Ingresa las categorías separadas con comas: ").split(",")
    nueva_entrada.terms_names = {
            'post_tag': etiquetas,
            'category': categorias,
    }
    print("Publicando entrada...")
    id_entrada_publicada = cliente.call(posts.NewPost(nueva_entrada))
    limpiar_pantalla()
    print("Correcto! Se guardó la entrada como borrador, y su id es {}".format(id_entrada_publicada))
    eleccion = input("¿Publicar inmediatamente? [S/N] ")
    if eleccion.lower() == "s":
        print("Publicando entrada...")
        nueva_entrada.post_status = 'publish'
        resultado = cliente.call(posts.EditPost(id_entrada_publicada, nueva_entrada))
        if resultado is True:
            input("Entrada publicada")
        else:
            input("Algo salió mal")
    imprimir_menu_opciones()


def mostrar_todas_las_entradas():
    offset = 0
    increment = 20
    while True:
        limpiar_pantalla()
        print("Mostrando entradas desde {} hasta {}".format(offset + 1, increment))
        entradas = cliente.call(posts.GetPosts({'number': increment, 'offset': offset}))
        if len(entradas) == 0:
                break  # no more posts returned
        mostrar_tabla_posts(entradas)
        eleccion = input("¿Ver más? [S/N] ")
        if eleccion.lower() != "s":
            break
        offset = offset + increment
    imprimir_menu_opciones()


def mostrar_tabla_posts(entradas):
    print("+{:-<20}+{:-<30}+{:-<50}+".format("", "", "", "", ""))
    print("|{:<20}|{:<30}|{:<50}|".format("ID", "Título", "Contenido"))
    print("+{:-<20}+{:-<30}+{:-<50}+".format("", "", "", "", ""))
    for entrada in entradas:
        print("|{:<20}|{:<30}|{:<50}|".format(entrada.id, entrada.title[0:30], limpiar_html(entrada.content)[0:50]))
    print("+{:-<20}+{:-<30}+{:-<50}+".format("", "", "", "", ""))


def pedir_id_para_eliminar():
    limpiar_pantalla()
    id_entrada_eliminar = int(input("Introduce el ID de la entrada que deseas eliminar [-1 para salir] "))
    if id_entrada_eliminar != -1:
        print("Eliminando entrada con el id {}".format(id_entrada_eliminar))
        resultado = cliente.call(posts.DeletePost(id_entrada_eliminar))
        if resultado is True:
            input("Eliminado correctamente")
        else:
            input("Algo salió mal")
    imprimir_menu_opciones()


def pedir_id_para_editar():
    limpiar_pantalla()
    id_entrada_editar = int(input("Introduce el ID de la entrada que deseas editar [-1 para salir] "))
    if id_entrada_editar != -1:
        entrada_para_editar = cliente.call(posts.GetPost(id_entrada_editar))
        entrada_original = entrada_para_editar
        entrada_para_editar.title = input("Introduce el nuevo título: [vacío si no quieres cambiarlo] ") or entrada_original.title
        entrada_para_editar.content = input("Introduce el nuevo contenido: [vacío si no quieres cambiarlo] ") or entrada_original.content
        print("Guardando cambios...")
        resultado = cliente.call(posts.EditPost(id_entrada_editar, entrada_para_editar))
        if resultado is True:
            input("Cambios guardados")
        else:
            input("Algo salió mal")
    imprimir_menu_opciones()


def imprimir_menu_opciones():
    limpiar_pantalla()
    eleccion = int(input("""Elige una opción:
    [ 1 ] - Agregar nueva entrada
    [ 2 ] - Ver todas las entradas
    [ 3 ] - Eliminar entrada
    [ 4 ] - Editar entrada
    [ 5 ] - Agregar entrada automaticamente
    [ -1 ] - Salir
"""))
    if eleccion == 1:
        pedir_datos_nueva_entrada()
    elif eleccion == 2:
        mostrar_todas_las_entradas()
    elif eleccion == 3:
        pedir_id_para_eliminar()
    elif eleccion == 4:
        pedir_id_para_editar()
    elif eleccion == 5:
        crear_nueva_entrada_automatica()
    else:
        exit()
#%%
# =============================================================================
# DATOS PARA VIAJEROAZUL
# =============================================================================


os.chdir('YOUR/PATH')

cliente = pagina_wordpres()

#Obtener la información del usuario para lanzar una excepción si la autenticación falla
cliente.call(GetUserInfo())
imprimir_menu_opciones()

#%%
from gensim.models import LdaModel
from gensim.corpora.dictionary import Dictionary


def get_topics(model, model_type = 'lda'):
  if model_type == 'lda':
      b = model.print_topics(num_topics=-1,num_words = 20)
  b = [i[1] for i in b]
  b = [i.split("+") for i in b]
  for pos,value in enumerate(b):
        b[pos] = [re.findall(r'"([^"]*)"', i)[0] for i in b[pos]]
  b =pd.DataFrame(b)
  return b

dataset = pd.read_csv('travel_translated.csv',sep=';')
#dataset_bolsa = pd.read_csv('06.ALTORO/DATASET/DATASET_PRENSA_ALTORO.csv',sep=';', encoding = 'latin-1')
#dataset_bolsa = dataset_bolsa.dropna(how='any')
dataset_cuerpo = dataset['cuerpo_traducido']

#dataset_bolsa_cuerpo = dataset_bolsa_cuerpo[0:500]

documents = list(dataset_cuerpo)


# Stopwords generation
STOP_WORDS_SET = set()
stopwordsfile = open("stopwords-es.txt", "r", encoding = 'utf-8')

for word in stopwordsfile: # a stop word in each line
    word = word.replace("\n", '')
    word = word.replace("\r\n", '')
    STOP_WORDS_SET.add(word)

# Punctuation symbols generation
PUNCTUATION = ['(', ')', ':', ';', ',', '-', '–', '!', '.', '?', '/', '"', '*',"`","’", "_", "“", '”','…','%','[',']','*']
# Carriage returns symbols generation
CARRIAGE_RETURNS = ['\n', '\r\n']
#Numeric characters
NUMERIC = ['0','1','2','3','4','5','6','7','8','9']

# Define stemming process
#stemmer = PorterStemmer()
# Other stemmer

#stemmer_spanish = SnowballStemmer('spanish')

for index,document in enumerate(documents): #run over each document
    for p in PUNCTUATION + CARRIAGE_RETURNS + NUMERIC:
        document = document.replace(p,' ') #quit punctuations from the document

    words = document.split(' ') #tokenize by words
    aux = list()
    for word in words:
        if (word not in STOP_WORDS_SET and len(word) > 2):
          word_stemm =word
          if (word_stemm not in STOP_WORDS_SET and len(word) > 2):
            aux.append(word_stemm)
            #aux.append(word)
          documents[index] = aux

topics = 3
dictionary = Dictionary(documents) #create a dictionary from the documents
dictionary.filter_extremes(no_below=2, no_above=0.7) # Filter the extrems of de dictionary
corpus = [dictionary.doc2bow(document) for document in documents] #transform documents in a BoW, Bag of Words (id2word)

lda = LdaModel(corpus, num_topics=topics, id2word= dictionary,update_every=1, chunksize=100, passes=5, distributed=False, iterations=10, per_word_topics=True, gamma_threshold=1e-3, minimum_probability=0.0, random_state=2019, alpha=0.01)

topics_lda = get_topics(lda)



















