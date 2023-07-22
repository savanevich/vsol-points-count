import logging

from controllers.get_statistic_for_all import print_statistic_all

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    filename='logs.txt')

logger = logging.getLogger('scraping')

USER_CHOICE = '''Enter one of the following:

- 'a' to print statistic for all tournaments
- 'q' to exit

Enter your choice: '''


user_choices = {
    'a': print_statistic_all,
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in 'a':
            user_choices[user_input]()
        else:
            print('Invalid command. Please try again.')

        user_input = input(USER_CHOICE)


menu()
