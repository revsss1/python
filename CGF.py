from collections import deque

class CFG:
    def __init__(self, non_terminals, terminals, productions, start_symbol):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol

    def generate(self, target):
        queue = deque([[self.start_symbol]])

        while queue:
            current = queue.popleft()
            current_string = ''.join(current)

            if current_string == target:
                print(f'Target string "{target}" generated.')
                return True

            for i in range(len(current)):
                symbol = current[i]
                if symbol in self.non_terminals:
                    prods = self.productions.get(symbol, [])
                    for prod in prods:
                        new_current = current[:]
                        new_current[i:i+1] = list(prod)
                        queue.append(new_current)

                        print(f'{current_string} -> {" ".join(new_current)}')

        print(f'Target string "{target}" cannot be generated.')
        return False

def main():
    # Input non-terminals
    non_terminals = input('Enter non-terminals (comma separated): ').strip().split(',')

    # Input terminals
    terminals = input('Enter terminals (comma separated): ').strip().split(',')

    # Input productions
    productions = {}
    print('Enter productions (format: A -> aA|b, enter "end" to finish): ')
    while True:
        production_input = input().strip()
        if production_input.lower() == 'end':
            break
        parts = production_input.split('->')
        non_terminal = parts[0].strip()
        prod_array = parts[1].split('|')
        prod_list = [prod.strip() for prod in prod_array]
        productions[non_terminal] = prod_list

    # Input start symbol
    start_symbol = input('Enter start symbol: ').strip()

    # Input target string
    target = input('Enter the target string: ').strip()

    cfg = CFG(non_terminals, terminals, productions, start_symbol)
    result = cfg.generate(target)

    print(f'Can the CFG generate the string "{target}"? {result}')

if __name__ == '__main__':
    main()
