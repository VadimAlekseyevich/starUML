# Reference library

Эта папка — **библиотека образцов**, а не рабочий формат проекта.

## Что оставляем из старой курсовой

`lending.uml` и `Костыль/` остаются важными, потому что показывают реальный принятый пример:

- виды диаграмм;
- уровень детализации;
- декомпозицию;
- boundary/control/entity;
- package/detail/relations;
- component/deployment/sequence;
- визуальное оформление.

## Что стало legacy

XML fragments и `generated/all-diagrams/` отражают внутренний формат StarUML 5.

Их можно читать для анализа старого примера, но новые диаграммы не строятся путём копирования XPD.

Технические документы:

- [technical/xpd-format.md](./technical/xpd-format.md) — legacy;
- [technical/mdj-format.md](./technical/mdj-format.md) — текущий формат;
- [LEGACY_STARUML5_REFERENCE.md](./LEGACY_STARUML5_REFERENCE.md) — как правильно пользоваться старым примером.

## Правильный маршрут

`methodology → reference README → Костыль/JPG → legacy XML при необходимости → построение в StarUML 7`

Сначала понимаем **смысл**, затем смотрим пример, и только потом рисуем.

## Покрытие lending

- Use Case: 8;
- Activity: 5;
- State Machine: 4;
- Class: 13;
- Component: 8;
- Deployment: 2;
- Sequence: 1.

Generated-файлы не редактируются вручную.

## Каноническая модель

Текущий проект:

`../01_functionality/urban_development_functionality.mdj`
