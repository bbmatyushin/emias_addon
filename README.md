#### Запуск в docker
Собираем необходимые образы для запуска:
```shell
sudo docker-compose -f docker-compose_build.yml build
```
Запускаем приложение:
```shell
sudo docker-compose -f docker-compose_up.yml up -d
```
Посмотреть логи:
```shell
sudo docker-compose -f docker-compose_up.yml logs -f
```
Останавливаем приложение:
```shell
sudo docker-compose -f docker-compose_up.yml down
```
---
Приложение доступно по адресу: http://127.0.0.1:5055/
