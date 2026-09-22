# Sequence Diagram — эталон + методичка

## Быстрый маршрут

- Методика: `../../methodology/interactions.md`.
- XML: `sequence.fragment.xml`.
- Карта рисунков DOCX: `../../methodology/MEDIA_MAP.md`.

## XML-эталон

[sequence.fragment.xml](./sequence.fragment.xml)

## Где скрыта диаграмма в lending

`Logical View → Interface → CollaborationInstanceSet1 → InteractionInstanceSet1 → SequenceDiagram1`.

Это хороший пример того, почему нельзя искать диаграммы только по верхним View.

## Порядок проектирования

Рекомендуемая цепочка методички:

`Activity/State Machine → Class → Sequence` [METHOD: P0478–P0485].

Для простых процессов Sequence может помочь выделить классы [METHOD: P0486–P0489].

## Главное правило согласованности

Имя сообщения на Sequence Diagram — операция класса, объект которого получает сообщение. Такая операция обязана существовать в Class Model [METHOD: P0496–P0501].

Это одно из ключевых cross-diagram правил нашего будущего validator.

## Combined Fragment

`alt`, `opt`, `loop`, `strict`, `par`, `seq` описаны в [METHOD: P0461–P0470].

## Controller

В методическом примере Controller формирует порядок сообщений между другими объектами [METHOD: P0510]. В Urban Development конкретный control-class будет взят из нашей Class Model.
