## Máquina de Turing - Regra 30

### Descrição
# 🤖 Projeto Final: Máquina de Turing - Regra 30

![Curso](https://img.shields.io/badge/Curso-Engenharia_de_Computação-blue)
![Disciplina](https://img.shields.io/badge/Disciplina-Linguagens_Formais_e_Autômatos-orange)

Este repositório contém a implementação e documentação do projeto final da disciplina de **Linguagens Formais e Autômatos** do **Instituto Federal Goiano - Campus Trindade**.

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
(Tabela baseada na referência)

---

## 📐 Descrição Formal da Máquina

Abaixo encontra-se a definição formal da Máquina de Turing projetada, composta pela tupla $M = (Q, \Sigma, \Gamma, \delta, q_0, q_{aceita}, q_{rejeita})$.

M = ({q0,q_ant0, q_ant1, q_check00, q_check01, q_check10, q_check11, q_fazA, q_fazB, q_fazC, 
q_fazD, q_limpa, q_fim}, {0,1}, {0, 1, A, B, C, D, #}, &, q0, #, {q_fim}) 

<img width="696" height="255" alt="Tabela Diagrama" src="https://github.com/user-attachments/assets/ee133fe8-2397-46d9-a541-70250aeb1e7a" />

Diagrama da máquina de turing:

<img width="595" height="574" alt="Diagrama Linguagens Trabalho" src="https://github.com/user-attachments/assets/286be569-7c8b-40a4-8d84-d06e645d067a" />

### Autores
* Palloma Barros
* Gabriel Rodrigues
* Tássio Moraes
