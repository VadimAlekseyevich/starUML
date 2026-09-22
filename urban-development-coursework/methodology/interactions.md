# Диаграмма последовательности / Interaction

## Роль

Sequence и Communication Diagram семантически эквивалентны как способы представления взаимодействий [METHOD: P0458–P0460].

Sequence показывает порядок сообщений и одновременно объекты, участвующие в поведении [METHOD: P0476].

## Рекомендуемый порядок

Методичка рекомендует:

`Activity/State Machine → Class → Sequence` [METHOD: P0478–P0485].

Для простого сценария возможен и обратный путь [METHOD: P0486–P0489].

## Главное cross-diagram правило

Сообщение на Sequence Diagram должно соответствовать операции класса-получателя [METHOD: P0495–P0501].

Поэтому Sequence не проектируется независимо от Class Model.

## Combined fragments

Используем:

- `alt`;
- `opt`;
- `loop`;
- `strict`;
- `par`;
- `seq` [METHOD: P0461–P0470].

## Создание объектов

Объект, создаваемый в ходе сценария, появляется на lifeline в момент create/constructor, а не обязательно в верхнем ряду [METHOD: P0508–P0509].

## Controller

Controller может задавать последовательность операций других объектов [METHOD: P0510].

Для Urban Development конкретные controller/application-service classes берём из нашей Class Model.

## StarUML 7

Старый `lending.uml` нужен как пример композиции Sequence, но legacy `UMLInteractionInstanceSet/UMLStimulus/UMLSeqStimulusView` не являются требованиями к современному `.mdj`.
