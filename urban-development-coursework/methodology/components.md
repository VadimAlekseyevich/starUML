# 4. Модель компонентов

## Наблюдение по lending

**[LENDING]** В эталоне 8 Component Diagram. Содержательные схемы лежат в `Logical View / Component`: `ClientClient`, `ClientServer`, `ManagerClient`, `ManagerServer`, `Service`, `Executable`, `artifact`. Верхний `Component View / Main` почти пуст.

Это означает, что при воспроизведении проекта надо ориентироваться не только на стандартный StarUML View, но и на реальную организацию эталона.

## Цель

Component Model показывает программные части системы и зависимости/интерфейсы между ними.

## Urban Development

**[PROJECT]** Реальная архитектура репозитория задаёт сильную основу:

- `frontend` — React/TypeScript/MapLibre;
- `backend` — FastAPI/REST/application layer;
- `core` — независимое алгоритмическое ядро;
- `worker` — фоновые GIS-задачи;
- PostgreSQL/PostGIS;
- Redis;
- storage/artifact subsystem.

## Несколько уровней

По примеру lending полезно разделить:

- клиентскую часть;
- серверную часть;
- сервисы;
- исполняемые компоненты;
- артефакты.

Точная декомпозиция будет определена после модели классов, чтобы компоненты не противоречили уже установленным обязанностям классов.

## Граница с Deployment

Component = логическая/программная единица.

Deployment Node = среда/узел, на котором программные артефакты выполняются.

Не заменять одно другим.
