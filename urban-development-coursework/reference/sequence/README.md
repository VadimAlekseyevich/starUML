# Sequence Diagram — методичка + старый эталон

> Старый XML — reference. Sequence следующих этапов строится непосредственно в StarUML 7.

## Источники

- `../../methodology/interactions.md`;
- methodology media;
- legacy `sequence.fragment.xml`.

В lending диаграмма находится глубоко в `Logical View → Interface → ...`; это пример старого дерева, а не обязательное размещение.

## Порядок

`Activity/State Machine → Class → Sequence` [METHOD: P0478–P0485].

## Ключевое правило

Сообщение должно существовать как operation у класса-получателя [METHOD: P0496–P0501].

## Combined fragments

`alt / opt / loop / strict / par / seq` [METHOD: P0461–P0470].

## Controller

Controller управляет порядком взаимодействий [METHOD: P0510].

Конкретный controller берём из нашей Class Model.
