## Máquina de Turing - Regra 30

### Descrição
# 🤖 Projeto Final: Máquina de Turing - Regra 30

![Curso](https://img.shields.io/badge/Curso-Engenharia_de_Computação-blue)
![Disciplina](https://img.shields.io/badge/Disciplina-Linguagens_Formais_e_Autômatos-orange)

O objetivo é desenvolver uma **Máquina de Turing** capaz de simular o comportamento do autômato celular unidimensional conhecido como **Regra 30**.

---

## 📚 Sobre o Projeto

A **Regra 30** é uma regra elementar de autômatos celulares introduzida por Stephen Wolfram em 1983. Ela especifica o estado (cor) de uma célula na próxima iteração baseando-se no seu estado atual e no de seus vizinhos imediatos (esquerda e direita).

O comportamento desta regra é complexo e caótico, sendo utilizada em:
* 🎲 Geração de números pseudoaleatórios;
* 🔐 Criação de criptografia;
* 🌿 Modelagem de sistemas naturais;
* 🗺️ Implementação de mapas procedurais em jogos.

### Objetivo
### 🎯 O Desafio
Desenvolver uma Máquina de Turing que, a partir de uma fita de entrada representando uma linha de células (geração $t$), processe e escreva na fita a próxima linha de células (geração $t+1$).

---

## ⚙️ Lógica de Transição (Regra 30)

Para determinar o estado da célula na próxima geração, a Máquina de Turing analisa a vizinhança (Esquerda, Centro, Direita). Existem 8 combinações possíveis:

| Vizinhança (E-C-D) | Novo Estado (t+1) | Binário |
| :---: | :---: | :---: |
| ⬛⬛⬛ (000) | ⬜ (0) | 0 |
| ⬛⬛⬜ (001) | ⬛ (1) | 1 |
| ⬛⬜⬛ (010) | ⬛ (1) | 1 |
| ⬛⬜⬜ (011) | ⬛ (1) | 1 |
| ⬜⬛⬛ (100) | ⬛ (1) | 1 |
| ⬜⬛⬜ (101) | ⬜ (0) | 0 |
| ⬜⬜⬛ (110) | ⬜ (0) | 0 |
| ⬜⬜⬜ (111) | ⬜ (0) | 0 |

---

## 📐 Descrição Formal da Máquina

Abaixo encontra-se a definição formal da Máquina de Turing projetada, composta pela tupla $M = (Q, \Sigma, \Gamma, \delta, q_0, B, F)$.

M = ({q0,q_ant0, q_ant1, q_check00, q_check01, q_check10, q_check11, q_fazA, q_fazB, q_fazC, 
q_fazD, q_limpa, q_fim}, {0,1}, {0, 1, A, B, C, D, #}, &, q0, #, {q_fim}) 

<img width="696" height="255" alt="Tabela Diagrama" src="https://github.com/user-attachments/assets/ee133fe8-2397-46d9-a541-70250aeb1e7a" />

---

A Máquina de Turing utiliza um conjunto de estados para memorizar a vizinhança (célula anterior e atual) e decidir o próximo valor com base na **Regra 30**. Como a máquina lê e escreve na mesma fita, são utilizados símbolos auxiliares (A, B, C, D) para marcar a transformação antes da passagem final de limpeza.

* **`q0` (Estado Inicial):**
    * Responsável por ler o primeiro símbolo da fita e iniciar o processamento, transitando para os estados de memória.

* **`q_ant0` e `q_ant1` (Memória do Anterior):**
    * Estes estados armazenam o valor da célula **anterior** (vizinho da esquerda) lida.
    * `q_ant0`: O vizinho da esquerda era **0**.
    * `q_ant1`: O vizinho da esquerda era **1**.
    * Eles movem o cabeçote para a direita para ler a célula central.

* **`q_checkXX` (Verificação de Padrão):**
    * Este conjunto de estados representa o conhecimento da sequência formada pelo vizinho da esquerda e a célula central. Ao ler o próximo símbolo (vizinho da direita), a máquina completa a trinca necessária para aplicar a Regra 30.
    * `q_check00`: Sequência identificada até agora: **0-0-?**
    * `q_check01`: Sequência identificada até agora: **0-1-?**
    * `q_check10`: Sequência identificada até agora: **1-0-?**
    * `q_check11`: Sequência identificada até agora: **1-1-?**

* **`q_fazA`, `q_fazB`, `q_fazC`, `q_fazD` (Escrita Temporária):**
    * Estados responsáveis por escrever um símbolo auxiliar na fita, representando o novo estado da célula $(t+1)$ sem perder a referência de posição.
    * **`q_fazA` e `q_fazC`**: Preparam a escrita do valor **0**.
    * **`q_fazB` e `q_fazD`**: Preparam a escrita do valor **1**.
    * Após marcar a célula, retornam o controle para os estados de memória (`q_ant`) para continuar o processamento da linha.

* **`q_limpa` (Limpeza e Conversão):**
    * Ativado quando a máquina chega ao fim da linha (lê um espaço em branco `#`).
    * O cabeçote varre a fita da direita para a esquerda, convertendo os símbolos temporários nos valores binários finais:
        * **A, C** $\rightarrow$ **0**
        * **B, D** $\rightarrow$ **1**

* **`q_fim` (Estado Final):**
    * Indica que a geração da nova linha foi concluída com sucesso e a máquina para sua execução.
---
Diagrama da máquina de turing:

<img width="595" height="574" alt="Diagrama Linguagens Trabalho" src="https://github.com/user-attachments/assets/286be569-7c8b-40a4-8d84-d06e645d067a" />

### Autores
* Palloma Barros
* Gabriel Rodrigues
* Tássio Moraes
