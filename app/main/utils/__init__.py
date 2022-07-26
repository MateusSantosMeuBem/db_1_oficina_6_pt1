options = [
    'Atualizar estudante pelo código',
    'Criar estudante',
    'Apagar estudante pelo código',
    'Mostrar estudantes',
    'Mostrar estudantes com [...]',
    'Sair'
]

def draw_menu():
    print('--------- MENU ---------')
    for key, option in enumerate(options):
        print(f'[{key + 1}] - {option}')
    print()

    return input('Opção: ')

