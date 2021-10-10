import json


def add_user():
    with open("database/users.json", "r+") as file:
        data = json.load(file)
        new_user = {}
        user = input('Podaj nazwę użytkownika: ')
        if user not in data:
            password = input('Podaj hasło uzytkownika: ')
        else:
            print('Nazwa użytkownika już jest zajęta, podaj inną.')
            return
        new_user[user] = password
        data.update(new_user)
        file.seek(0)
        json.dump(data, file)


add_user()
