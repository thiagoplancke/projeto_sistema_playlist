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

                return True

            anterior = atual
            atual = atual.prox

        return False

    def buscar_musica_por_id(self, id):
        atual = self.lista

        while atual:
            if atual.musica.id == id:
                return atual.musica

            atual = atual.prox

        return None

    def buscar_musica_por_titulo(self, titulo):
        atual = self.lista

        while atual:
            if atual.musica.titulo.lower() == titulo.lower():
                return atual.musica

            atual = atual.prox

        return None

    def listar_musicas(self):
        atual = self.lista

        while atual:
            musica = atual.musica

            print(
                f"ID: {musica.id}, "
                f"Título: {musica.titulo}, "
                f"Artista: {musica.artista}, "
                f"Gênero: {musica.genero}, "
                f"BPM: {musica.bpm}"
            )

            atual = atual.prox

    def total_musicas(self):
        atual = self.lista
        total = 0

        while atual:
            total += 1
            atual = atual.prox

        return total


class NodoFila:
    def __init__(self, musica):
        self.musica = musica
        self.prox = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enqueue(self, musica):
        novo_nodo = NodoFila(musica)

        if not self.inicio:
            self.inicio = novo_nodo
            self.fim = novo_nodo
        else:
            self.fim.prox = novo_nodo
            self.fim = novo_nodo

    def dequeue(self):
        if not self.inicio:
            return None

        musica = self.inicio.musica

        self.inicio = self.inicio.prox

        if not self.inicio:
            self.fim = None

        return musica

    def listar(self):
        atual = self.inicio

        while atual:
            musica = atual.musica

            print(
                f"ID: {musica.id}, "
                f"Título: {musica.titulo}, "
                f"Artista: {musica.artista}, "
                f"Gênero: {musica.genero}, "
                f"BPM: {musica.bpm}"
            )

            atual = atual.prox

    def tamanho(self):
        atual = self.inicio
        total = 0

        while atual:
            total += 1
            atual = atual.prox

        return total