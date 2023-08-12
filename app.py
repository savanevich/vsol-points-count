import logging

from controllers.get_statistic_for_cubanas import print_statistic_cubanas
from controllers.get_statistic_for_ciego import print_statistic_ciego
from controllers.get_statistic_for_trinidad import print_statistic_trinidad

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    filename='logs.txt')

USER_CHOICE = '''Enter one of the following:

- 'a' to print statistic for Cubanas Royal Trophy
- 'b' to print statistic for Ciego de Avila Trophy
- 'c' to print statistic for Trinidad Trophy
- 'q' to exit

Enter your choice: '''


user_choices = {
    'a': print_statistic_cubanas,
    'b': print_statistic_ciego,
    'c': print_statistic_trinidad,
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ['a', 'b', 'c']:
            user_choices[user_input]()
        else:
            print('Invalid command. Please try again.')

        user_input = input(USER_CHOICE)


menu()
