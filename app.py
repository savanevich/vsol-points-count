import logging

from controllers.get_teams_statistic import print_statistic_cubanas, print_statistic_ciego, print_statistic_trinidad
from controllers.get_players_statistic import print_statistic_olivares
from controllers.get_teams_history_statistic import print_teams_history_statistic
from controllers.get_teams_perspectives_statistic import print_teams_perspective_statistic

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    filename='logs.txt')

USER_CHOICE = '''Enter one of the following:

- 'a' to print statistic for Cubanas Royal Trophy
- 'b' to print statistic for Ciego de Avila Trophy
- 'c' to print statistic for Trinidad Trophy
- 'd' to print statistic for Olivares Trophy
- 'e' to print statistic for Teams History
- 'f' to print statistic for Teams Perspective
- 'q' to exit

Enter your choice: '''


user_choices = {
    'a': print_statistic_cubanas,
    'b': print_statistic_ciego,
    'c': print_statistic_trinidad,
    'd': print_statistic_olivares,
    'e': print_teams_history_statistic,
    'f': print_teams_perspective_statistic
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ['a', 'b', 'c', 'd', 'e', 'f']:
            user_choices[user_input]()
        else:
            print('Invalid command. Please try again.')

        user_input = input(USER_CHOICE)


menu()
