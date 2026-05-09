# Sistema de Playlist 🎵

Projeto desenvolvido para a disciplina de Estrutura de Dados com foco na implementação manual de estruturas encadeadas em Python.

## 📌 Objetivo

O projeto simula o backend de um aplicativo de músicas, permitindo:

* Gerenciar uma biblioteca de músicas
* Criar filas de reprodução baseadas em humor
* Reproduzir músicas
* Registrar histórico de reprodução
* Consultar estatísticas do sistema

O principal objetivo acadêmico é praticar:

* Lista encadeada simples
* Filas FIFO
* Encapsulamento
* Separação de responsabilidades
* Manipulação de nós encadeados sem estruturas prontas do Python

---

## 🧠 Estruturas de Dados Utilizadas

### Lista Encadeada

Utilizada para armazenar toda a biblioteca musical.

Permite:

* Inserção de músicas
* Remoção por ID
* Busca
* Percurso completo

### Filas FIFO

Utilizadas para:

* Filas de humor
* Histórico de reprodução

Operações principais:

* `enqueue`
* `dequeue`

---

## 📂 Estrutura do Projeto

```bash
📁 sistema-playlist/
│
├── musica.py
├── nodo_lista.py
├── biblioteca.py
├── nodo_fila.py
├── fila.py
├── main.py
└── README.md
```

---

## 🏗️ Classes do Sistema

### `Musica`

Representa uma música da biblioteca.

Atributos:

* `id`
* `titulo`
* `artista`
* `genero`
* `bpm`

---

### `NodoLista`

Nó utilizado na lista encadeada da biblioteca.

Contém:

* Uma instância de `Musica`
* Referência para o próximo nó

---

### `Biblioteca`

Lista encadeada responsável por armazenar todas as músicas cadastradas.

Operações:

* Inserção
* Remoção
* Busca
* Listagem

---

### `NodoFila`

Nó utilizado internamente pela fila.

---

### `Fila`

Implementação própria de fila FIFO.

Usada para:

* Filas de humor
* Histórico

Operações:

* `enqueue`
* `dequeue`
* Exibição
* Verificação de fila vazia

---

## 🎶 Filas de Humor

As músicas são organizadas automaticamente conforme o BPM.

| Humor   | BPM          |
| ------- | ------------ |
| Relaxar | até 80       |
| Focar   | 81 a 120     |
| Animar  | 121 a 160    |
| Treinar | acima de 160 |

---

## 📋 Funcionalidades

### 1. Adicionar música

* Cadastro de músicas
* Geração automática de ID sequencial

### 2. Remover música

* Remoção por ID

### 3. Buscar música

* Busca por:

  * ID
  * Título

### 4. Listar biblioteca

* Exibe todas as músicas cadastradas

### 5. Montar filas de humor

* Percorre toda a biblioteca
* Reconstrói as filas do zero

### 6. Reproduzir próxima música

* Remove da fila escolhida
* Adiciona ao histórico

### 7. Exibir fila de humor

* Mostra músicas sem removê-las

### 8. Exibir histórico

* Lista músicas já reproduzidas

### 9. Estatísticas

Exibe:

* Total de músicas
* Tamanho de cada fila
* Total reproduzido

---

## ⚠️ Regras do Projeto

* Não utilizar:

  * `list`
  * `deque`
  * Estruturas prontas para lista/fila

* Toda estrutura deve ser implementada manualmente com nós encadeados.

* IDs:

  * São automáticos
  * Não podem ser reutilizados

* Entradas inválidas devem ser tratadas:

  * BPM inválido
  * BPM ≤ 0
  * ID inexistente
  * Reprodução em fila vazia

---

## ▶️ Como Executar

Clone o repositório:

```bash
git clone <url-do-repositorio>
```

Entre na pasta:

```bash
cd sistema-playlist
```

Execute o programa:

```bash
python main.py
```

---

## 🎯 Conceitos Trabalhados

Este projeto reforça conceitos importantes de Estrutura de Dados:

* Encadeamento de nós
* Manipulação de ponteiros/referências
* Filas FIFO
* Percurso de listas
* Organização orientada a objetos
* Separação de responsabilidades
* Validação de entrada

---

## 🚀 Possíveis Melhorias Futuras

Ideias interessantes para evoluir o projeto:

* Persistência em arquivo
* Interface gráfica
* Sistema de playlists personalizadas
* Ordenação por artista/gênero
* Reprodução aleatória
* Busca parcial por nome
* Relatórios estatísticos mais avançados

---

## 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos na disciplina de Estrutura de Dados.
