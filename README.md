# Test_task
## О проекте
Данный проект создан в качестве тестового задания на должность 
**junior backend(Django) developer**. Здесь реализован простейший функционал 
с помощью базовых возможностей фреймворка *Django*, который отражает в себе пример 
работы будущего *junior developer'а*. Проект представляет собой небольшой сайт 
с возможностью регистрации и аутентификации с помощью *GitHub*. Пользователи могут 
добавлять, изменять, удалять информацию о своем профиле. Пользователям разрешается переход
к своему профилю и списку всех пользователей только после заполнения личной информации 
в форме, на которую перенаправляется пользователь после первого входа(регистрации) 
на сайте. Также есть возможность выхода из аккаунта на сайте с помощью соответствующей кнопки.


## Функциональность
В проекте реализованы такие возможности и функции:
* Регистрация и авторизация с помощью учетной записи GitHub. <br/>
На главной странице все гости(неавторизованные пользователи) имеют возможность войти 
в систему или зарегистрироваться в ней(в случае отсутствия аккаунта на сайте) с помощью
учетной записи GitHub. Пользователь, который не вошел в систему, не может получить доступ 
к остальным страницам сервиса, и при попытках перейти на них перенаправляется на начальную 
страницу для авторизации.

* Выход из системы. <br>
Авторизированные пользователи имеют возможность в любой момент выйти из своего аккаунта
с помощью специальной кнопки в верху станицы.

* Просмотр своего профиля. <br/>
Любой авторизированный пользователь, который ввел личную информацию в специальной форме
после регистрации, может просматривать информацию своего профиля на соответствующей странице.
Эта страница содержит аватар пользователя, ФИО и email в сециальной карточке Bootstrap, 
а также дополнительную информацию.

* Добавление/изменение личных данных. <br/>
С помощью кнопки *"Изменить профиль"* пользователь может перейти к специальной форме для 
изменения информации о профиле. Кроме того, эта форма обязательна к заполнения после 
регистрации(первого входа в систему), так как без ее заполнения пользователь не сможет 
посещать остальные страницы сайта 

* Просмотр всех пользователей. <br/>
С помощью кнопки *"Смотреть всех пользователей"* авторизованному пользователю 
предоставляется возможность посмотреть всех зарегистрированных в системе пользователей,
информация о которых представляется в виде карточек Bootstrap


## Технологии
В *backend-части* данного проекта задействован фреймворк *Django* языка 
*python*.<br/>
Для представления данных на web-страницах используется язык разметки *web-страниц*
*HTML*, а также был задействован фреймворк *Bootstrap* для дизайна сайта. <br/>
База данных реализована с помощью встроенной *db.sqlite*.