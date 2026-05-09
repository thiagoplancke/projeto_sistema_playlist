class Musica():
    def __init__(self,id,titulo,artista,genero,bpm):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

    def __str__(self):
        return f"Musica(id={self.id}, titulo={self.titulo}, artista={self.artista}, genero={self.genero}, bpm={self.bpm})"