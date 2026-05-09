class NodoLista:
    def __init__(self, musica):
        self.musica = musica
        self.prox = None

class Biblioteca:
    def __init__(self):
        self.lista = None

    def adicionar_musica(self, musica):
        novo_nodo = NodoLista(musica)
        if not self.lista:
            self.lista = novo_nodo
        else:
            atual = self.lista
            while atual.prox:
                atual = atual.prox
            atual.prox = novo_nodo

    def remover_musica(self, id):
        atual = self.lista
        anterior = None
        while atual:
            if atual.musica.id == id:
                if anterior:
                    anterior.prox = atual.prox
                else:
                    self.lista = atual.prox
                return
            anterior = atual
            atual = atual.prox
            
    def buscar_musica(self, id):
        atual = self.lista
        while atual:
            if atual.musica.id == id:
                return atual.musica
            atual = atual.prox
        return None

    def listar_musicas(self):
        atual = self.lista
        while atual:
            print(f"ID: {atual.musica.id}, Título: {atual.musica.titulo}, Artista: {atual.musica.artista}, Gênero: {atual.musica.genero}, BPM: {atual.musica.bpm}")
            atual = atual.prox
