Для запуска кода необходимо (Полноценный способ):
1) Прописать: "docker-compose build"
2) Прописать: "docker-compose up"


Если локально всё пошло по одному месту, то инструкция по обнулению БД:
1) Запустить сам контейнер через Десктоп
2) Открыть консоль где зпускаете докер и прописать следующее:
3) docker exec -it db bash
4) psql -U postgres -d postgres
5) DROP SCHEMA public CASCADE;
6) CREATE SCHEMA public;
7) \q
8) exit
