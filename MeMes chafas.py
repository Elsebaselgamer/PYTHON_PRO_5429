meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'OMG': 'Expresion de asombro',
            'NASHE': 'Algo del pintor',
            'WTF': 'Que carajos?',
            'AESTHETIC': 'Expresion usada para definir cierto estilo',
            'GRWM': 'Expresion usada para: Alistate conmigo',
            'NEA': 'Persona con corte de cabello el 7',
            'BRUH': 'Expresion usada para cualquier cosa',
            'GG': 'Great Game',
            'SHIPPEAR': 'Juntar a dos personas o personajes en un romance en mi imaginacion',
            'PRIME': 'Persona que se encuentra en el mejor punto de su carrera o existencia',
               }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print("este el el significado de una palabra", meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
  print('no lo tengo')
