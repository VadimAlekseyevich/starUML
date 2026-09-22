# Deployment Diagram — старый пример + реальный deployment

> В методичке отдельной Deployment-главы нет. Lending/Костыль дают визуальный ориентир, но не диктуют дерево StarUML 7.

## Старые материалы

- `Lending_Arch.jpg`;
- `Architecture.jpg`;
- `deployment.jpg`;
- `rasm_art.jpg`;
- legacy `lending.fragment.xml`.

Историческое размещение диаграммы lending в Logical View/Arch не является обязательным.

## Urban Development

Deployment должен показать:

- browser/client;
- frontend;
- api;
- worker;
- PostgreSQL/PostGIS;
- Redis;
- storage;
- сетевые связи.

Он должен трассироваться к Component Model.

Важно различать logical component и node/execution environment.
