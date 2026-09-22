# 4. Модель компонентов

## Статус источников

В `методичка.docx` отдельной главы по Component Diagram нет.

Поэтому используем:

- lending как старый учебный пример [LENDING];
- `Костыль` как визуальный reference [COURSEWORK];
- реальную архитектуру Urban Development Generator [PROJECT].

Это не METHOD.

## Что берём из lending

Старый lending показывает полезные виды Component Diagram и способы представления client/server/service/artifact.

То, что его содержательные Component Diagram находятся в `Logical View / Component`, — **историческая структура файла**, а не обязательное правило для StarUML 7.

## Urban Development

Канонические компоненты:

- Frontend;
- Backend API;
- Algorithmic Core;
- Worker;
- PostgreSQL/PostGIS;
- Redis;
- artifact/file storage при необходимости.

Точный набор и dependencies выводим из Class Model и реальной архитектуры.

## Граница с Deployment

Component Model отвечает: **из каких программных частей состоит система и как они зависят друг от друга**.

Deployment отвечает: **где эти части исполняются/размещаются**.

Нельзя превращать Component Diagram в копию Docker Compose.
