#### Запуск в docker
Собираем необходимые образы для запуска:
```shell
sudo docker-compose build
```
Запускаем приложение:
```shell
sudo docker-compose up -d
```
Посмотреть логи:
```shell
sudo docker-compose logs -f
```
Останавливаем приложение:
```shell
sudo docker-compose down
```
---
Приложение доступно по адресу: http://127.0.0.1:5055/

---
### Копируем образы на удаленный сервер
```shell
# Пакуем образы в архив (сначала название архива, потом имя образа)
# Архивы будут сохранены в директории откуда вызывалась команда

sudo docker save -o emias_addon_app.tar emias_addon_app
sudo docker save -o uwsgi_nginx_flask.tar uwsgi_nginx_flask
```
```shell
# Переносим образы на удаленный сервер

scp emias_addon_app.tar <user>@<remote_host_ip>/home/<user>
scp uwsgi_nginx_flask.tar <user>@<remote_host_ip>/home/<user>

# docker-compose.yml понадобится для запуска приложения

scp docker-compose.yml  <user>@<remote_host_ip>/home/<user>
```
```shell
# Выгружаем образы из архива

sudo docker load -i /home/<user>/emias_addon_app.tar
sudo docker load -i /home/<user>/uwsgi_nginx_flask.tar
```
```shell
# Запускаем контейнер с приложением
cd mkdir /home/<user> && sudo docker-compose up -d
```
