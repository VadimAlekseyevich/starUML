# Class Diagram — методичка + старый эталон

> XML fragments — legacy StarUML 5 reference. Новая Class Model будет создаваться непосредственно в StarUML 7.

## Источники

- `../../methodology/classes.md`;
- methodology media;
- `ClassEntityPackeges.jpg`;
- `ClassEntityDetail.jpg`;
- `ClassEntityDetailWithRelation.jpg`;
- `ControlClass.jpg`;
- `BoundaryClass.jpg`;
- legacy `entity_with_relation.fragment.xml`.

## Почему в lending много Class Diagram

Потому что METHOD требует три представления [P0406–P0410]:

1. package;
2. detail;
3. relations.

Поэтому этот паттерн **сохраняем и в StarUML 7**.

## Boundary / Control / Entity

Это методическое правило, а не особенность XPD [METHOD: P0359–P0374; P0405].

## Происхождение классов

Классы/операции выводятся из поведенческой модели [METHOD: P0355–P0380].

## Логическая целостность

Все классы package view присутствуют в detail view [METHOD: P0450–P0452].

## Отношения

Aggregation/composition — по lifecycle [METHOD: P0415–P0419].

Dependencies call/use/create — по реальному характеру взаимодействия [METHOD: P0426–P0438].
