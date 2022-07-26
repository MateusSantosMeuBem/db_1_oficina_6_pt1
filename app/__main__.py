# Pip imports
from main.model import connector

# Local imports
from main.services.database import (
    create_student,
    change_student_by_code,
    delete_student_by_code,
    show_students,
    show_students_with
)

from main.utils import (
    draw_menu,
    options
)

if __name__ == '__main__':
    manager = [
        change_student_by_code,
        create_student,
        delete_student_by_code,
        show_students,
        show_students_with
    ]

    try:
        print('Trying conecting...')
        connection = connector()
        print('Conected!')

        while True:
            choice = draw_menu()
            if choice in [str(option) for option in range(1, len(manager) + 2)]:
                if choice == str(len(options)):
                    break
                else:
                    manager[int(choice) - 1](connection)
            else:
                print('\n -- DIGITE UMA OPÇÃO VÁLIDA -- \n')

        connection.close()
        print('Connection closed!')

    except Exception as exception:
        print(exception)


