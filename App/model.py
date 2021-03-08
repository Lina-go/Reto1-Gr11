﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as it
from DISClib.Algorithms.Sorting import selectionsort as sr
from DISClib.Algorithms.Sorting import quicksort as qt
from DISClib.Algorithms.Sorting import mergesort as mt
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog(tipo):
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y videos. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'category': None
               }

    catalog['videos'] = lt.newList(tipo)
    catalog['category'] = lt.newList(tipo,
                                     cmpfunction=cmpVideosById),

    return catalog

# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)
    # Se obtiene el autor del video


def addVideoYoutuber(catalog, authorname, videos):
    """
    Adiciona un youtuber a lista de youtubers, la cual guarda referencias
    a los videos de dicho youtuber
    """
    channel_title = catalog['channel_title']
    poschannel_title = lt.isPresent(channel_title, authorname)
    if poschannel_title > 0:
        channel_titlee = lt.getElement(channel_title, poschannel_title)
    else:
        channel_titlee = newAuthor(authorname)
        lt.addLast(channel_title, channel_titlee)
    lt.addLast(channel_titlee['videos'], videos)


def addCategory(catalog, video_ctg):
    """
    Adiciona un tag a la lista de tags
    """
    c = newCategory(video_ctg['name'], video_ctg['id'])
    lt.addLast(catalog['category'], c)


# Funciones para la creación de Datos

def newAuthor(name):
    """
    Crea una nueva estructura para modelar los videos de
    un autor y su promedio de ratings
    """
    channel_titlee = {'name': "", "videos": None,  "likes": 0}
    channel_titlee['name'] = name
    channel_titlee['videos'] = lt.newList('ARRAY_LIST')
    return channel_titlee


def newCategory(c_name, c_id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    video_ctg = {'name': '', 'id': ''}
    video_ctg['name'] = c_name
    video_ctg['id'] = int(c_id)
    return video_ctg

# Funciones de comparación


def cmpVideosByViews(video1, video2):
    return (float(video1['views']) < float(video2['views']))


def cmpVideosById(video_1, video_2):
    if video_1 < video_2:
        return -1
    elif video_1 == video_2:
        return 0
    else:
        return 1


def comparecountry(country_1, country):
    if (country_1.lower() in country['country'].lower()):
        return 0
    return -1

#category_id, videos_id


# Funciones para sort


def sortvideos(catalog, size):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = sa.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list


def sort_type(catalog, size, type):

    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if type == "insertionsort":
        sorted_list = it.sort(sub_list, cmpVideosByViews)
    elif type == "selectionsort":
        sorted_list = sr.sort(sub_list, cmpVideosByViews)
    elif type == "mergesort":
        sorted_list = mt.sort(sub_list, cmpVideosByViews)
    elif type == "quicksort":
        sorted_list = qt.sort(sub_list, cmpVideosByViews)
    else:
        sorted_list = sa.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

# Funciones de Consulta


def getVideosByViews(catalog, category_name, country, size_lt):
    """
    Retorna el trending_date, title, channel_title, publish_time, views, likes, dislikes
    de acuerdo a un category_name, country, número de videos que se quieren listar.
    Este es el requerimiento 1
    """
    pass


def getVideosbyDays(catalog, country):
    """
    Retorna title, cannel_title, country, número de días
    Este es el req 2
    """
    pass
