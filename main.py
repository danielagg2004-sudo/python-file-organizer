from pathlib import Path
import constantes

folder = Path("test-folder")
organizador = {}
categorias_usuario = {}

def mover_archivos(folder,organizador):
    for key in organizador.keys():
        if isinstance(organizador[key],dict):
            mover_archivos(folder / key , organizador[key])
        elif isinstance(organizador[key],list):
            for file in organizador[key]:
                file.rename(folder / key / file.name)

def crear_carpetas(folder, organizador):
    for key in organizador.keys():
        if not (folder / key).exists() and not (folder / key).is_dir():
            (folder / key).mkdir()
        if isinstance(organizador[key],dict):
            crear_carpetas(folder / key ,organizador[key])
while True:
    cat = input("Ingresa el nombre de tu categoria o deja en blanco para terminar: ")
    if cat== "":
        break
    categorias_usuario.setdefault(cat,[])
    ext = []
    while True:
        ext.append(input("Ingresa la extension que admite tu categoia o pulsa enter para terminar:"))
        if ext[-1] == "":
            del ext[-1]
            break
    categorias_usuario[cat]= ext



for file in folder.iterdir():
    switchVar=False
    for key in categorias_usuario:
        if str(file).endswith(tuple(categorias_usuario[key])):
            organizador.setdefault(key,[]).append(file)
            switchVar=True
            break
    if switchVar:
        continue
    if file.is_dir():
        continue
    elif str(file).endswith(constantes.IMAGEEXT):
        organizador.setdefault("Imagenes",[]).append(file)
    elif str(file).endswith(constantes.EJECUTABLEEXT):
        organizador.setdefault("Ejecutables",[]).append(file)
    elif str(file).endswith(constantes.DOCUMENTEXT):
        organizador.setdefault("Documentos",{})
        if str(file).endswith(constantes.PDFEXT):
            organizador["Documentos"].setdefault("PDF",[]).append(file)
        elif str(file).endswith(constantes.TEXTEXT):
            organizador["Documentos"].setdefault("Documentos de texto",[]).append(file)
    elif str(file).endswith(constantes.OFFICEEXT):
        organizador.setdefault("Office",{})
        if str(file).endswith(constantes.WORDEXT):
            organizador["Office"].setdefault("Word",[]).append(file)
        elif str(file).endswith(constantes.EXCELEXT):
            organizador["Office"].setdefault("Excel",[]).append(file)
        elif str(file).endswith(constantes.PPOINTEXT):
            organizador["Office"].setdefault("Power point",[]).append(file)
        elif str(file).endswith(constantes.ACCESSEXT):
            organizador["Office"].setdefault("Access",[]).append(file)
    elif str(file).endswith(constantes.COMPREXT):
        organizador.setdefault("Archivos comprimidos",[]).append(file)
    else:
        organizador.setdefault("Otros",[]).append(file)



crear_carpetas(folder,organizador)
mover_archivos(folder,organizador)




    
