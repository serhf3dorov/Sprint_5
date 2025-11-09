# UI tests for Stellar Burgers

## Фикстуры - ***conftest.py***
* `driver` - настройки webdriver

## Данные пользователя и список URL - ***data.py***
* `class Data` - валидные данные пользователя
* `class Url` - список URL страниц

## Сценарии, покрытые тестами

### Регистрация пользователя - ***test_registration.py***
* `test_registration_success` - успешная регистрация пользователя
* `test_registration_without_name` - регистрация без имени
* `test_registration_without_email` - регистрация без email
* `test_registration_without_password` - регистрация без пароля
* `test_registration_password_less_6_symbols` - регистрация с невалидным паролем
* `test_registration_with_incorrect_email` - регистрация с некорректным email
* `test_registration_with_exist_user` - регистрация уже существующего пользователя


### Вход в аккаунт - ***test_login.py***
* `test_login_from_main_page` - вход по кнопке "Войти в аккаунт" на главной странице
* `test_login_via_account_button` - вход через кнопку «Личный кабинет»
* `test_login_via_registration_page` - вход через кнопку в форме регистрации
* `test_login_via_password_recovery` - вход через кнопку в форме восстановления пароля


### Переход в личный кабинет - ***test_go_to_personal_account***
* `test_go_to_personal_account` - переход по клику на «Личный кабинет»


### Переход из личного кабинета в конструктор - ***test_go_to_constructor_from_personal_account.py***
* `test_go_to_constructor_from_account_by_click_on_constructor` - переход по клику на "Конструктор"
* `test_go_to_constructor_from_account_by_click_on_logo` - переход по клику на лого "Stellar Burgers"


### Выход из аккаунта - ***test_logout.py***
* `test_logout` - выход по кнопке «Выйти» в личном кабинете


### Раздел "Конструктор" - ***test_constructor.py***
* `test_go_to_buns` - переход к разделу "Булки"
* `test_go_to_sauces` - переход к разделу "Соусы"
* `test_go_to_fil` - переход к разделу "Начинки"
