import json
import sys

class TuringMachine:
    def __init__(self, config):
        """
        Inicializa a Máquina de Turing com a configuração JSON
        """
        self.states = config['states']
        self.input_symbols = config['input_symbols']
        self.tape_symbols = config['tape_symbols']
        self.transitions = self._build_transition_dict(config['transiction'])
        self.current_state = config['initial_state']
        self.blank_symbol = config['white']
        self.final_states = config['end_state']
        self.tape = []
        self.head_position = 0
        self.step_count = 0
        
    def _build_transition_dict(self, transitions_list):
        """
        Constrói um dicionário de transições para acesso O(1)
        Formato: {(estado_atual, símbolo_lido): (novo_estado, símbolo_escrito, direção)}
        """
        trans_dict = {}
        for trans in transitions_list:
            key = (trans['initial'], trans['read'])
            value = (trans['end'], trans['write'], trans['action'])
            trans_dict[key] = value
        return trans_dict
    
    def load_tape(self, input_string):
        """
        Carrega a fita com a entrada, adicionando marcadores de borda
        """
        self.tape = [self.blank_symbol] + list(input_string) + [self.blank_symbol]
        self.head_position = 1
        self.current_state = self.transitions[(self.current_state, self.tape[self.head_position])][0] if (self.current_state, self.tape[self.head_position]) in self.transitions else self.current_state
        
    def get_tape_content(self):
        """
        Retorna o conteúdo atual da fita sem os marcadores de borda
        """
        content = ''.join(self.tape)
        return content.strip(self.blank_symbol)
    
    def print_configuration(self):
        """
        Exibe a configuração atual da máquina
        """
        tape_display = ''.join(self.tape)
        pointer = ' ' * self.head_position + '^'
        print(f"Passo {self.step_count}:")
        print(f"Fita:   {tape_display}")
        print(f"Cabeça: {pointer}")
        print(f"Estado: {self.current_state}")
        print(f"Lendo:  '{self.tape[self.head_position]}'")
        print("-" * 50)
    
    def step(self):
        """
        Executa um passo da Máquina de Turing
        Retorna True se continuou, False se parou (estado final ou sem transição)
        """
        if self.current_state in self.final_states:
            return False
        
        current_symbol = self.tape[self.head_position]
        transition_key = (self.current_state, current_symbol)
        
        if transition_key not in self.transitions:
            print(f"ERRO: Transição não definida para ({self.current_state}, '{current_symbol}')")
            return False
        
        new_state, write_symbol, direction = self.transitions[transition_key]
        
        # Escreve na fita
        self.tape[self.head_position] = write_symbol
        
        # Move a cabeça
        if direction == 'R':
            self.head_position += 1
            if self.head_position >= len(self.tape):
                self.tape.append(self.blank_symbol)
        elif direction == 'L':
            self.head_position -= 1
            if self.head_position < 0:
                self.tape.insert(0, self.blank_symbol)
                self.head_position = 0
        # 'S' significa ficar parado (Stay)
        
        # Atualiza o estado
        self.current_state = new_state
        self.step_count += 1
        
        return True
    
    def run(self, max_steps=10000, verbose=False):
        """
        Executa a Máquina de Turing até parar
        """
        if verbose:
            self.print_configuration()
        
        while self.step_count < max_steps:
            if not self.step():
                break
            if verbose:
                self.print_configuration()
        
        if self.step_count >= max_steps:
            print(f"AVISO: Máquina atingiu o limite de {max_steps} passos")
        
        return self.get_tape_content()


def load_config_from_file(file_path):
    """
    Carrega a configuração da Máquina de Turing de um arquivo JSON
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
        print(f"✓ Configuração carregada de: {file_path}")
        return config
    except FileNotFoundError:
        print(f"✗ ERRO: Arquivo não encontrado: {file_path}")
        print(f"  Verifique se o caminho está correto e o arquivo existe.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"✗ ERRO: JSON inválido no arquivo {file_path}")
        print(f"  Detalhes: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ ERRO ao carregar arquivo: {e}")
        sys.exit(1)


# Exemplo de uso
if __name__ == "__main__":
    print("=" * 60)
    print("SIMULADOR DE MÁQUINA DE TURING - REGRA 30")
    print("=" * 60)
    print()
    
    # Define o caminho do arquivo JSON
    json_path = "../input/modelo.json"
    
    # Carrega a configuração do arquivo
    config_json = load_config_from_file(json_path)
    print()
    
    # Solicita a entrada do usuário
    print("Digite a sequência de células (use apenas 0 e 1)")
    print("Exemplo: 000100")
    test_input = input("Entrada: ").strip()
    
    # Valida a entrada
    if not test_input:
        print("✗ Entrada vazia! Usando exemplo padrão: 000100")
        test_input = "000100"
    elif not all(c in '01' for c in test_input):
        print("✗ Entrada inválida! Use apenas 0 e 1. Usando exemplo padrão: 000100")
        test_input = "000100"
    
    print()
    
    # Cria e executa a máquina
    tm = TuringMachine(config_json)
    tm.load_tape(test_input)
    
    result = tm.run(verbose=True)
    
    print("=" * 60)
    print(f"RESULTADO FINAL")
    print("=" * 60)
    print(f"Entrada:  {test_input}")
    print(f"Saída:    {result}")
    print(f"Passos:   {tm.step_count}")
    print(f"Estado:   {tm.current_state}")
    print()
    
    # Perguntar se deseja fazer outro teste
    print("\n" + "=" * 60)
    print("DESEJA FAZER OUTRO TESTE?")
    print("=" * 60)
    resposta = input("Digite 's' para sim ou Enter para sair: ").strip().lower()
    
    if resposta == 's':
        test_input2 = input("Digite a nova sequência: ").strip()
        
        # Valida a nova entrada
        if test_input2 and all(c in '01' for c in test_input2):
            print(f"\nProcessando: {test_input2}")
            
            tm2 = TuringMachine(config_json)
            tm2.load_tape(test_input2)
            result2 = tm2.run(verbose=False)
            
            print(f"Saída:   {result2}")
            print(f"Passos:  {tm2.step_count}")
        else:
            print("Entrada inválida! Encerrando programa.")
    else:
        print("Programa finalizado.")