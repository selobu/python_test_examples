# https://gestionhseq.com
# @servicioslatam
from json import loads, dumps
from pprint import pprint

bulk_json1 = '{"glossary1": {"title": "example glossary", "GlossDiv": {"title": "S", "GlossList": {"GlossEntry": {"ID": "SGML1", "SortAs": "SGML", "GlossTerm": "Standard Generalized Markup Language1", "Acronym": "SGML", "Abbrev": "ISO 8879:1986", "GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.", "GlossSeeAlso": ["GML", "XML"]}, "GlossSee": "markup"}}}}, "glossary2": {"title": "example glossary", "GlossDiv": {"title": "S", "GlossList": {"GlossEntry1": {"ID": "SGML1", "SortAs": "SGML", "GlossTerm": "Standard Generalized Markup Language 3", "Acronym": "SGML", "Abbrev": "ISO 8879:1986", "GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.", "GlossSeeAlso": ["GML", "XML"]}, "GlossSee": "markup"}, "GlossEntry2": {"ID": "SGML2", "SortAs": "SGML", "GlossTerm": "Standard Generalized Markup Language 2", "Acronym": "SGML", "Abbrev": "ISO 8879:1986", "GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.", "GlossSeeAlso": ["GML", "XML"]}, "GlossSee": "markup"}}}}}'
bulk_json2 = '{"glossary1": {"title": "example glossary", "GlossDiv": {"title": "S", "GlossList": {"GlossEntry": {"ID": "2SGML1", "SortAs": "SGML", "GlossTerm": "Standard Generalized Markup Language1", "Acronym": "SGML", "Abbrev": "ISO 8879:1986", "GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.", "GlossSeeAlso": ["GML", "XML"]}, "GlossSee": "markup"}}}}, "glossary2": {"title": "example glossary", "GlossDiv": {"title": "S", "GlossList": {"GlossEntry1": {"ID": "2SGML3", "SortAs": "SGML", "GlossTerm": "Standard Generalized Markup Language 3", "Acronym": "SGML", "Abbrev": "ISO 8879:1986", "GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.", "GlossSeeAlso": ["GML", "XML"]}, "GlossSee": "markup"}, "GlossEntry2": {"ID": "2SGML2", "SortAs": "SGML", "GlossTerm": "Standard Generalized Markup Language 2", "Acronym": "SGML", "Abbrev": "ISO 8879:1986", "GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.", "GlossSeeAlso": ["GML", "XML"]}, "GlossSee": "markup"}}}}}'

# 1.  Se interpretan los contenidos de los string json y se convierten a diccionarios
json1 = loads(bulk_json1)
json2 = loads(bulk_json2)

def func(struct, val_2_search: str, curr_path=[]):
    """funcion recursiva para encontrar valores en string de tipo json

    Args:
        struct (_type_): diccionario con la estructura a buscar
        val_2_search (str): _description_
        curr_path (list, optional): variable privada. Defaults to [].

    Yields:
        _type_: generador contiene las rutas encontradas
    """
    for key, value in struct.items():
        newpath= curr_path[:]
        newpath.append(key)
        if isinstance(value, dict):
             v = list(func(value, val_2_search, newpath))
             if len(v)>0:
                 yield v[0]
        elif isinstance(value, str):
            if value == val_2_search:
                yield ('/'.join(newpath), True)

# encontrar id especificado en el arbol
print(list(func(json1, "SGML1")))
print('//---//')
print(list(func(json2, "2SGML3")))
a=1