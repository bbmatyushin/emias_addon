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
