# 5. Модель размещения

## Статус источников

Отдельной главы Deployment в методичке нет.

Основа:

- lending [LENDING];
- реальный deployment Urban Development Generator [PROJECT].

## Старый lending

Рабочая Deployment Diagram у lending лежит в `Logical View / Arch`, а верхний Deployment View/Main почти пуст.

Это полезное наблюдение об эталонном файле, но **не требование повторить такую структуру в StarUML 7**.

## Urban Development

Фактические runtime units:

- browser/client;
- frontend;
- api;
- worker;
- PostgreSQL/PostGIS;
- Redis;
- migrate job;
- storage при наличии.

Deployment Diagram строится после Component Model и показывает размещение компонентов/artifacts на execution environments/nodes и связи между ними.

## Cross-diagram правило

Каждый значимый исполняемый компонент должен иметь понятное deployment mapping.

Словарь — `model/architecture.yaml`.
