1. Клонируем проект
git clone https://github.com/didoogan/attractgroup-test.git

2. Переходим внутрь
cd attractgroup-test/

3. Создаем базу
sudo -u postgres psql
CREATE DATABASE test_db;
CREATE USER test WITH password 'test';
GRANT ALL ON DATABASE test_db TO test;

4. Создать виртуальное окружение
pip install virtualenv
virtualenv -p python3 .env

5. Активируем его
.env/bin/activate

6. Устанавливаем зависимости
pip3 install -r requirements/local.txt

7. Создаем таблицы в базе
./manage.py migrate

8. Запускаем Celery
celery -A config worker -l info

9. Создаем супер юзера
./manage.py createsuperuser

10. Запускаем сервер
./manage.py createsuperuser

11. Заходим в админку (http://127.0.0.1:8000/admin/)

12. Переходим в приложение Authenticator

13. Создаем новый объект Authenticator, выбираем csv файл с юзерами (в той же
директории, что и manage.py

14. Переходим в приложение Product, создаем несколько инстансов

15. Переходим по http://127.0.0.1:8000/

16. Играемя с заказами, тестируем админа и обычных юзеров (подсматриваем в
консольку с celery, чтобы увидеть креденшилы созданных юзеров), в общем,
убеждаемся, что все замечательно.

17. Перезваниваем мне, хвалим, предлагаем офер и ЗП в 3 раза больше, от
запрашиваемой [шутка :)