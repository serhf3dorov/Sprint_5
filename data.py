from random import randint


class Data:
    name = 'Сергей'
    email = 'sergeyfedorov35292@yandex.ru.'
    password = '25256182'


class Url:
    main_page = "https://stellarburgers.education-services.ru" #URL главной страницы
    login_page = f"{main_page}/login" #URL страницы авторизации
    registration_page = f"{main_page}/register" #URL страницы регистрации
    profile_page = f"{main_page}/account/profile" #URL страницы профиля


class RandomUser:
    name = f"Random{randint(0, 999)}Name"
    email = f"random{randint(000, 999)}mail@gmail.com"
    password = f"rnd{randint(000, 999)}"

