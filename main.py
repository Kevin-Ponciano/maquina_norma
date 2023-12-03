class MaquinaNorma:
    # Inicializa os registradores com os valores fornecidos ou 0 por padrão
    def __init__(self, A=0, B=0, C=0, D=0):
        self.registradores = {'A': A, 'B': B, 'C': C, 'D': D}

    # Incrementa o valor do registrador especificado em 1
    def add(self, reg):
        self.registradores[reg] += 1

    # Decrementa o valor do registrador especificado em 1, se for maior que 0
    def sub(self, reg):
        if self.registradores[reg] > 0:
            self.registradores[reg] -= 1

    # Verifica se o valor do registrador especificado é igual a 0
    def zer(self, reg):
        return self.registradores[reg] == 0

    def execute_instruction(self, instruction):
        # Divide a instrução em partes
        parts = instruction.split()
        if len(parts) < 2:
            return None

        label, cmd, reg, *jumps = parts

        # Se o comando for 'ADD', chama o método add() e retorna o índice de salto
        if cmd == 'ADD':
            self.add(reg)
            return int(jumps[0])

        # Se o comando for 'SUB', chama o método sub() e retorna o índice de salto
        elif cmd == 'SUB':
            self.sub(reg)
            return int(jumps[0])

        elif cmd == 'ZER':
            # Se o comando for 'ZER' e o registrador for zero, retorna o primeiro índice de salto
            if self.zer(reg):
                return int(jumps[0])
            # Se o comando for 'ZER' e o registrador não for zero, retorna o segundo índice de salto
            else:
                return int(jumps[1])
        else:
            return None

    def get_register_values(self):
        # Retorna uma tupla com os valores dos registradores
        return tuple(self.registradores.values())

    def execute_program(self, program):
        i = 0
        while i < len(program):
            current_state = self.get_register_values()
            # Exibe o estado atual dos registradores e a instrução sendo executada
            print(f"{current_state} , {i + 1}) {program[i]}")
            # Executa a instrução e atualiza o índice da próxima instrução
            i = self.execute_instruction(program[i]) - 1


# Lê as linhas do programa a partir de um arquivo e remove espaços em branco
def read_program(file_path):
    with open(file_path, 'r') as file:
        program = file.readlines()
    return [line.strip() for line in program]

def main():
    print("Máquina de Norma")
    while True:
        print("Menu:")
        print("1 - Somar")
        print("2 - Multiplicar")
        print("3 - Fatorial")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            print("Soma")
            program = read_program('soma.txt')
            A = int(input("Valor inicial de A: "))
            B = int(input("Valor inicial de B: "))
            C = 0
            D = 0
            maquina = MaquinaNorma(A, B, C, D)
            maquina.execute_program(program)
        elif opcao == 2:
            print("Multiplicação")
            program = read_program('multiplicacao.txt')
            A = int(input("Valor inicial de A: "))
            B = int(input("Valor inicial de B: "))
            C = 0
            D = 0
            maquina = MaquinaNorma(A, B, C, D)
            maquina.execute_program(program)
        elif opcao == 3:
            print("Fatorial")
            program = read_program('fatorial.txt')
            A = int(input("Valor inicial de A: "))
            B = 0
            C = 0
            D = 0
            maquina = MaquinaNorma(A, B, C, D)
            maquina.execute_program(program)
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()
