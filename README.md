# Завдання: Розробка веб-додатку для управління завданнями ("Task Manager")
## Опис проекту:
Створіть веб-застосунок для керування завданнями, який дозволяє користувачам створювати, редагувати, видаляти та 
переглядати завдання. Застосунок має підтримувати реєстрацію та автентифікацію користувачів, а також мати зручний інтерфейс для взаємодії із завданнями.

## Основні вимоги:
1. Реєстрація та автентифікація користувачів:

* Користувачі повинні мати можливість зареєструватися, увійти в систему та вийти з неї.
* Реалізуйте захист маршрутів для автентифікованих користувачів.

2. Профіль користувача:
* Кожен користувач повинен мати профіль, де він може редагувати свої дані (ім'я, email, тощо).

3. Управління завданнями:
* Користувачі можуть створювати завдання з зазначенням заголовка, опису, терміну виконання та пріоритету.
* Можливість редагування та видалення завдань.
* Можливість перегляду списку завдань з фільтрацією за статусом (виконано/не виконано), пріоритетом та терміном виконання.

4. API:
* Використовуйте Django REST Framework для створення API для управління завданнями.
* API має включати ендпоінти для CRUD (створення, читання, оновлення, видалення) операцій із завданнями.
* Реалізуйте автентифікацію для API (наприклад, з використанням токенів).

5. Фронтенд:
* Використовуйте Bootstrap для створення адаптивного та зручного інтерфейсу.
* Створіть сторінки для реєстрації, входу, профілю користувача, списку завдань і форми створення/редагування завдань.

6. Тестування:
* Напишіть тести для перевірки функціональності бекенду (моделі, серіалізатори, представлення) та API.
* Перевірте, що основні сценарії роботи додатку працюють коректно.

7. Документація:
* Підготуйте документацію щодо встановлення та запуску проекту.
* Опис основних функцій додатку та API.

8. Додаткові вимоги (за бажанням):
* Інтернаціоналізація (i18n): підтримка кількох мов інтерфейсу.
* Сповіщення: сповіщення користувачів електронною поштою про створення, зміну та наближення терміну виконання завдань.
* Інтеграція з зовнішніми сервісами: наприклад, інтеграція з календарем Google для відображення завдань.
* Використання Docker: створення Docker-контейнерів для простого розгортання застосунку.

## Організація роботи:
1. Розподіл завдань:
* Розділіть проект на підзадачі та розподіліть їх між членами команди.
* Визначте ролі: хто буде відповідати за бекенд, фронтенд, тестування та документацію.
2. Спільна робота:
* Використовуйте систему контролю версій (наприклад, Git) для управління кодом.
* Проводьте регулярні зустрічі для обговорення прогресу та проблем.
3. Код-рев'ю:
* Проводьте код-рев'ю для підтримки якості коду та обміну знаннями всередині команди.