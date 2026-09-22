# 4. Модель компонентов

## Статус источников

В текущем `методичка.docx` отдельной главы по Component Diagram нет.

Поэтому этот раздел основан на:

- `lending.uml` [LENDING];
- материалах `Костыль/диаграммы` [COURSEWORK];
- реальной архитектуре `urban-development-generator` [PROJECT].

Нельзя ссылаться на этот файл как на прямое требование METHOD.

## Наблюдение по lending

Содержательные Component Diagram находятся в `Logical View / Component`: `ClientClient`, `ClientServer`, `ManagerClient`, `ManagerServer`, `Service`, `Executable`, `artifact` [LENDING].

Стандартный верхний `Component View / Main` при этом практически пуст [LENDING].

## Urban Development

Канонические компоненты из реального проекта:

- Frontend;
- Backend API;
- Algorithmic Core;
- Worker;
- PostgreSQL/PostGIS;
- Redis;
- subsystem хранения Artifact/файлов.

Точный набор Component Diagram будет выбран после Class Model, чтобы связи компонентов не противоречили обязанностям boundary/control/entity классов.

## Граница с Deployment

Component Model описывает программные части и зависимости.

Deployment Model описывает узлы/среды исполнения и размещённые на них artifacts/components.
