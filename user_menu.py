import sys
from enum import Enum
# import database


class ChoiceEnum(Enum):
    ADD_POSITION = 1
    ADD_RECRUITING = 2
    ADD_CANDIDATE = 3
    CHANGE_CANDIDATE_STATUS = 4
    CHANGE_RECRUITMENT_STATUS = 5
    LOG_OUT = 6


def add_position():
    pass


def add_recruiting():
    pass


def add_candidate():
    pass


def change_candidate_status():
    pass


def change_recruitment_status():
    pass


def log_out():
    print('Koniec programu.')
    sys.exit(0)


def run_calculation(choice):
    functions[choice]()


functions = {
    ChoiceEnum.ADD_POSITION.value: add_position,
    ChoiceEnum.ADD_RECRUITING.value: add_recruiting,
    ChoiceEnum.ADD_CANDIDATE.value: add_candidate,
    ChoiceEnum.CHANGE_CANDIDATE_STATUS.value: change_candidate_status,
    ChoiceEnum.CHANGE_RECRUITMENT_STATUS.value: change_recruitment_status,
    ChoiceEnum.LOG_OUT.value: log_out,

}


def print_options():
    print('1. Dodaj nowe stanowisko')
    print('2. Dodaj nową rekrutację')
    print('3. Dodaj nowego kandydata')
    print('4. Zmień ststus kandydata')
    print('5. Zmień status rekrutacji')
    print('6. Wyjście z programu')


def validate_decision(decision):
    allowed_decisions = [e.value for e in ChoiceEnum]
    if decision not in allowed_decisions:
        raise Exception(f"Liczba {decision} jest niedozwolona!")


while True:
    print_options()
    decision = int(input('Wybierz dzialanie: '))
    validate_decision(decision)
    run_calculation(decision)
