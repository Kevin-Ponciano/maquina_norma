# README - Máquina de Norma

## Descrição

Este é um código Python que implementa uma simulação de uma máquina fictícia chamada "Máquina de Norma". A máquina possui registradores e pode executar programas que consistem em uma série de instruções. As instruções disponíveis incluem adição, subtração e verificação se um registrador está zerado.

## Funções

O código inclui as seguintes funções e classes:

### Classe `MaquinaNorma`

- `__init__(self, A=0, B=0, C=0, D=0)`: Inicializa a máquina com quatro registradores (A, B, C e D) com valores iniciais opcionais.
- `add(self, reg)`: Incrementa o valor do registrador especificado em 1.
- `sub(self, reg)`: Decrementa o valor do registrador especificado em 1, desde que seja maior que 0.
- `zer(self, reg)`: Verifica se o valor do registrador especificado é igual a 0.
- `execute_instruction(self, instruction)`: Executa uma instrução fornecida como uma string e retorna o próximo índice de instrução a ser executado.
- `get_register_values(self)`: Retorna uma tupla com os valores atuais dos registradores.
- `execute_program(self, program)`: Executa um programa fornecido como uma lista de instruções, exibindo o estado dos registradores durante a execução.

### Função `read_program(file_path)`

- Lê um programa a partir de um arquivo de texto especificado por `file_path` e retorna as instruções como uma lista de strings.

### Função `main()`

- Exibe um menu interativo para o usuário, permitindo escolher entre três programas diferentes: soma, multiplicação e cálculo de fatorial.
- Solicita valores iniciais para os registradores A e B.
- Cria uma instância da classe `MaquinaNorma` com os valores iniciais e executa o programa escolhido.

## Como Usar

1. Certifique-se de ter o Python instalado em seu sistema.

2. Baixe o código fonte deste projeto.

3. Crie arquivos de programa para as operações desejadas (soma, multiplicação e fatorial) no formato de texto, como `soma.txt`, `multiplicacao.txt` e `fatorial.txt`. Cada arquivo deve conter uma série de instruções, uma por linha.

4. Execute o código Python através do terminal ou do ambiente de desenvolvimento. Certifique-se de que o script e os arquivos de programa estão na mesma pasta.

5. Siga as instruções do menu interativo para escolher a operação desejada, fornecer valores iniciais para os registradores A e B, e executar o programa correspondente.

## Autor

- Kevin Ponciano - [kevin-ponciano](https://github.com/kevin-ponciano)

## Co-autores

- Daniel Batista Zoppi - [DanielBZoppi](https://github.com/DanielBZoppi)
- Edgar Gama de Souza

## Ferramentas

- [Python](https://www.python.org/) - Linguagem de programação.
- [PyCharm](https://www.jetbrains.com/pt-br/pycharm/) - Ambiente de desenvolvimento integrado (IDE).
- [ChatGPT-4](https://chat.openai.com/) - Ferramenta de geração de texto baseada em inteligência artificial.