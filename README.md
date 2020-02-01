# ShurBot_LinkedIn
El ShurBot que te permite aplicar a todas las ofertas con EasyApply en LinkedIn

### Aviso

Si durante la instalacion del bot tenemos cualquier problema que no aparezca en las instrucciones, buscar un tutorial en YouTube sobre como instalar X nos deberia resolver ese problema. El ordenador de cada uno es un mundo(distintos Sistemas Operativos que existen, programas instalados que puedan dar problemas, etc.).

## Instrucciones de uso:

1. Instalamos Visual Studio Code https://code.visualstudio.com/

2. Instalamos Python https://www.python.org/downloads/ Click en el boton amarillo que pone 3.8.0

3. Creamos una carpeta donde queramos, y ahi copiamos lo que hemos extraido del .zip

4. Abrimos Visual Studio y le damos a Open Folder, abrimos la carpeta que acabamos de crear

5. En la parte izquierda apareceran los archivos, sino, hacemos click en el icono de los 2 documentos solapados y aparece el menu de documentos

6. Doble click para ver el codigo del archivo easyapplybot.py

7. Ahora volvemos otra vez a donde clickamos para ver el archivo, pero le damos click derecho, y le damos a Run Python File in Terminal

8. En la parte de abajo aparecera la terminal, igual se inicia automaticamente el bot o igual no. Si lo hace dara error. Pulsamos Control + C varias veces y luego Enter, hasta que aparezca todo el rato la misma linea una y otra vez, eso es que no hay nada funcionando

9. Instalamos los paquetes que hacen falta. Para ello ejecutamos en la terminal `pip install -r requirements.txt` desde ShurtBot_linkdln/

10. Ahora en el codigo del archivo easyapplybot.py, en las ultimas lineas 272=277, donde pone username, password, position, etc. Ahi ponemos lo que nos interesa, nuestro usuario de LinkedIn y contraseña, el lenguaje lo dejamos en español, y de position ponemos el trabajo que queremos y de location pues la ciudad o pais que queramos. Guardamos el archivo con Control + S

11. Con todo listo ejecutamos el programa, dandole a Run Python File in Terminal

12. Ya deberia de estar funcionando. Como aclaracion, decir que el CV y todo ese rollo no tiene nada que ver con el bot, eso lo configuramos nosotros previamente en nuestra cuenta de LinkedIn para que cuando hacemos EasyApply salga el CV por defecto.


Varios shurs ya lo preguntaron. Este bot vale para todos los trabajos y todas los lugares del mundo. Que queremos buscar trabajo en Madrid como Android Developer, pues hacemos lo dicho en el paso 10 y listo. Que queremos buscar en otro sitio u otro puesto. Pues paramos el bot, si es que esta funcionando, nos vamos al codigo y volvemos a cambiar *position* y *location*. Guardamos de nuevo el archivo y volvemos a iniciar el bot de nuevo.
