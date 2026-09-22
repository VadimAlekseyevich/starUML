# Legacy StarUML XPD

> Исторический reference. Текущий формат — StarUML 7 `.mdj`.

`lending.uml` использует XML/XPD StarUML 5.

Полезный общий принцип, который переносится дальше:

**semantic model element отделён от visual View.**

В XPD связи строились через GUID и `XPD:REF`, а collections имели счётчики `#OwnedElements`, `#Views` и т. п.

Ручное изменение таких collections оказалось хрупким. В частности, несогласованные reverse relations include/extend могли приводить к `Invalid class typecast`.

Legacy паттерны:

- Use Case: UMLUseCase + UMLUseCaseView;
- Activity: UMLActivityGraph/TOP + diagram;
- Statechart: UMLStateMachine + states/transitions;
- Class: semantic class + compartment Views.

Эти детали нужны для чтения lending и истории миграции, но **не задают структуру новых диаграмм StarUML 7**.

Современная модель: [mdj-format.md](./mdj-format.md).
