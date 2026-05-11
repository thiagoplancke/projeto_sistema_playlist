from estrutura import Biblioteca, Fila
from musica import Musica


biblioteca = Biblioteca()

fila_relaxar = Fila()
fila_focar = Fila()
fila_animar = Fila()
fila_treinar = Fila()

historico = Fila()

proximo_id = 1


def montar_filas():

    fila_relaxar.limpar()
    fila_focar.limpar()
    fila_animar.limpar()
    fila_treinar.limpar()

    atual = biblioteca.lista

    while atual:
        musica = atual.musica

        if musica.bpm <= 80:
            fila_relaxar.enqueue(musica)

        elif 81 <= musica.bpm <= 120:
            fila_focar.enqueue(musica)

        elif 121 <= musica.bpm <= 160:
            fila_animar.enqueue(musica)

        else:
            fila_treinar.enqueue(musica)

        atual = atual.prox


while True:

    print("\n===== SISTEMA PLAYLIST =====")
    print("1 - Adicionar música")
    print("2 - Remover música")
    print("3 - Buscar música")
    print("4 - Listar biblioteca")
    print("5 - Montar filas por humor")
    print("6 - Reproduzir próxima")
    print("7 - Exibir fila")
    print("8 - Histórico")
    print("9 - Estatísticas")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")

  
    if opcao == "0":
        print("Saindo...")
        break

   
    elif opcao == "1":

        titulo = input("Título: ")
        artista = input("Artista: ")
        genero = input("Gênero: ")

        try:
            bpm = int(input("BPM: "))

            if bpm <= 0:
                print("BPM deve ser maior que 0.")
                continue

        except:
            print("BPM inválido.")
            continue

        musica = Musica(
            proximo_id,
            titulo,
            artista,
            genero,
            bpm
        )

        biblioteca.adicionar_musica(musica)

        print("Música adicionada com sucesso.")

        proximo_id += 1

   

    elif opcao == "2":

        try:
            id_musica = int(input("Digite o ID: "))

        except:
            print("ID inválido.")
            continue

        removida = biblioteca.remover_musica(id_musica)

        if removida:
            print("Música removida.")
        else:
            print("Música não encontrada.")

   
    elif opcao == "3":

        tipo = input("Buscar por (id/titulo): ").lower()

        if tipo == "id":

            try:
                id_musica = int(input("Digite o ID: "))

            except:
                print("ID inválido.")
                continue

            musica = biblioteca.buscar_musica_por_id(id_musica)

        elif tipo == "titulo":

            titulo = input("Digite o título: ")

            musica = biblioteca.buscar_musica_por_titulo(titulo)

        else:
            print("Tipo inválido.")
            continue

        if musica:
            print(
                f"{musica.id} - "
                f"{musica.titulo} - "
                f"{musica.artista} - "
                f"{musica.genero} - "
                f"{musica.bpm} BPM"
            )

        else:
            print("Música não encontrada.")

   
   

    elif opcao == "4":

        print("\n===== BIBLIOTECA =====")
        biblioteca.listar_musicas()

  

    elif opcao == "5":

        montar_filas()

        print("Filas montadas com sucesso.")



    elif opcao == "6":

        nome_fila = input(
            "Escolha a fila "
            "(relaxar/focar/animar/treinar): "
        ).lower()

        if nome_fila == "relaxar":
            fila = fila_relaxar

        elif nome_fila == "focar":
            fila = fila_focar

        elif nome_fila == "animar":
            fila = fila_animar

        elif nome_fila == "treinar":
            fila = fila_treinar

        else:
            print("Fila inválida.")
            continue

        musica = fila.dequeue()

        if not musica:
            print("Fila vazia.")
            continue

        historico.enqueue(musica)

        print("\nTocando agora:")
        print(
            f"{musica.id} - "
            f"{musica.titulo} - "
            f"{musica.artista} - "
            f"{musica.genero} - "
            f"{musica.bpm} BPM"
        )

    # =========================
    # EXIBIR FILA
    # =========================

    elif opcao == "7":

        nome_fila = input(
            "Escolha a fila "
            "(relaxar/focar/animar/treinar): "
        ).lower()

        if nome_fila == "relaxar":
            fila = fila_relaxar

        elif nome_fila == "focar":
            fila = fila_focar

        elif nome_fila == "animar":
            fila = fila_animar

        elif nome_fila == "treinar":
            fila = fila_treinar

        else:
            print("Fila inválida.")
            continue

        print(f"\n===== FILA {nome_fila.upper()} =====")

        fila.listar()

    # =========================
    # HISTÓRICO
    # =========================

    elif opcao == "8":

        print("\n===== HISTÓRICO =====")

        historico.listar()

    # =========================
    # ESTATÍSTICAS
    # =========================

    elif opcao == "9":

        print("\n===== ESTATÍSTICAS =====")

        print(
            f"Total músicas biblioteca: "
            f"{biblioteca.total_musicas()}"
        )

        print(
            f"Relaxar: {fila_relaxar.tamanho()}"
        )

        print(
            f"Focar: {fila_focar.tamanho()}"
        )

        print(
            f"Animar: {fila_animar.tamanho()}"
        )

        print(
            f"Treinar: {fila_treinar.tamanho()}"
        )

        print(
            f"Histórico: {historico.tamanho()}"
        )

    else:
        print("Opção inválida.")