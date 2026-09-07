
#  Organizador de archivos en Python

## Descripción 

La idea de este programa es automatizar la organización de los archivos de una carpeta especifica, el programa recorrerá todos los archivos y los reposicionará en la carpeta correspondiente según su extensión. De igual manera el programa permite al usuario crear su propia categoría para guardar archivos específicos en una carpeta con nombre indicado por el usuario.

## Características

- Organizado automático de archivos según su extensión.
- Creación automática de carpetas para cada categoría.
- Permite al usuario crear categorías personalizadas.
- Permite asignar múltiples extensiones a una categoría personalizada.
- Organización de archivos en categorías y subcategorías.
- Mueve los archivos automáticamente a la carpeta correspondiente.
- Previene errores por carpetas ya existentes.
- Ignora carpetas ya creadas.

## Tecnologías empleadas

- Python 3.13.15
- Modulo Pathlib
- Módulos Python

## Como utilizarlo 

1.  El programa viene por defecto con una ruta relativa por defecto, la carpeta de prueba.
```Python
 folder = Path(" test-folder ")
```
aquí se puede sustituir por la ubicación de la carpeta que se quiere ordenar, (en Windows es importante utilizar \\ ya que \ altera la cadena) para no afectar la cadena, por ejemplo:
> folder = Path(" C:\\Users\\User\\Documents ")

2. Una vez especificado la carpeta se puede ejecutar el programa y se obtendrá esto en terminal:
> Ingresa el nombre de tu categoría o deja en blanco para terminar: 

aquí el usuario puede agregar el nombre de su carpeta para su categoría personalizada, también puede pulsar *Enter* para cancelar este procedimiento y proseguir con el acomodo por defecto de los archivos.
> *Ejemplo*:
>
> Ingresa el nombre de tu categoría o deja en blanco para terminar:  **Arduino**

3. Si presionamos Enter sin escribir un nombre de categoría, el programa procederá directamente con la organización predeterminada. Si escribimos el nombre de una categoría, el programa nos preguntará qué extensiones queremos asignarle.
>Ingresa la extensión que admite tu categoría o pulsa enter para terminar: **.ino**
>Ingresa la extensión que admite tu categoría o pulsa enter para terminar:
>
>**Nota**: Es importante utilizar el punto (.) en el texto que ingresemos ya que el programa compara el texto que entregamos con la terminación de la ruta del archivo, sin el punto el programa puede funcionar de manera errónea.

Una vez terminado este procedimiento correctamente la carpeta deseada habrá sido reorganizada priorizando las categorías dadas por el usuario, en este caso si se encuentra un documento con extensión .ino , este será enviado a la carpeta Arduino, si no se le asigna esta extensión a esta carpeta el programa .ino será enviado a la carpeta *Otros*
>**Nota**: Una vez asignadas las extensiones el programa volverá a preguntar si deseamos agregar otra categoría, de ser así podemos repetir el procedimiento, si no podemos pulsar enter.

##  Ejemplo

Para este ejemplo en mi folder de prueba organizaré un conjunto de archivos. Para esto quiero que los documentos PDF no queden dentro de la carpeta documentos>>PDF , quiero que queden en la carpeta Tareas para esto primero asignare la carpeta que quiero organizar, en este caso es test-folder por lo cual no hare ningún cambio en el código.
``` python
folder = Path("test-folder")
```
![Carpeta desorganizada](Imagenes%20de%20ejemplo/Carpeta%20desorganizada.png)

Para poder crear las categorías debo de asignarle a la carpeta Tarea la extensión .pdf para esto al ejecutar el programa haré lo siguiente

>Ingresa el nombre de tu categoría o deja en blanco para terminar: Tareas
>Ingresa la extensión que admite tu categoría o pulsa enter para terminar:.pdf
>Ingresa la extensión que admite tu categoría o pulsa enter para terminar:
>Ingresa el nombre de tu categoría o deja en blanco para terminar: 

Este es el resultado de la carpeta
![Carpeta organizada](Imagenes%20de%20ejemplo/Carpeta%20organizada.png)

Normalmente, al organizar los archivos por extensión, los documentos PDF serían colocados dentro de una carpeta llamada Documentos, que a su vez contendría una subcarpeta llamada PDF. Sin embargo, en este caso esta estructura no fue creada debido a que se especificó que los archivos con extensión .pdf fueran almacenados directamente en la carpeta *Tareas*..






