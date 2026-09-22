# Class Diagram — эталон + методичка

## Быстрый маршрут

1. Правила: `../../methodology/classes.md`.
2. XML: `entity_with_relation.fragment.xml`.
3. Изображения lending: `ClassEntityPackeges.jpg`, `ClassEntityDetail.jpg`, `ClassEntityDetailWithRelation.jpg`, `ControlClass.jpg`, `BoundaryClass.jpg`.
4. Рисунки методички: см. Class-раздел `../../methodology/MEDIA_MAP.md`.

## XML-эталон

[entity_with_relation.fragment.xml](./entity_with_relation.fragment.xml)

![Class Entity With Relation](../../../Костыль/диаграммы/ClassEntityDetailWithRelation.jpg)

## Почему в lending так много Class Diagram

Методичка требует три вида представления Class Model [METHOD: P0406–P0410]:

1. package view;
2. detail view;
3. relations view.

Именно поэтому в lending регулярно встречаются тройки:

- `...Packages`;
- `...DetailClass`;
- `...DetailClassWithRelation`.

Это не случайное дублирование диаграмм.

## Boundary / Control / Entity

Методичка предлагает делить классы на:

- entity — носители информации;
- boundary — интерфейс;
- control — прикладная логика/управление [METHOD: P0359–P0374; P0405].

Это объясняет `BoundaryClass`, `ControlClass` и Entity packages в lending.

## Происхождение классов

Классы целесообразно выделять из поведенческих моделей [METHOD: P0355].

ActionState трансформируется в операции и помогает выделять реализующий класс [METHOD: P0355–P0380].

## Логическая целостность

Все классы package view должны присутствовать в detail view [METHOD: P0450–P0452].

Эту проверку мы позже добавим в автоматический validator.

## Отношения

Aggregation/composition обосновываются жизненным циклом части [METHOD: P0415–P0419].

Dependency `call/use/instantiate/create` выбирается по реальному характеру использования [METHOD: P0426–P0438].
