# Техническая памятка по формату StarUML XPD

Исходный `lending.uml` — XML в старом формате StarUML:

```xml
<XPD:PROJECT xmlns:XPD="http://www.staruml.com" version="1">
```

Главная причина, почему нельзя бездумно «склеивать картинки»: StarUML хранит отдельно **семантические объекты** и **визуальные View**, связывая их GUID.

## Базовый паттерн

Условно:

```text
UMLUseCase (semantic model element)
    ↑ Model reference
UMLUseCaseView (visual occurrence on a diagram)
    ↑ belongs to
UMLUseCaseDiagramView
    ↑ represents
UMLUseCaseDiagram
```

Один `UMLUseCase` может иметь несколько View и поэтому появляться на нескольких диаграммах, оставаясь одной сущностью.

## Namespace и Owner

Частые ссылки:

- `Namespace` — семантический владелец элемента;
- `DiagramOwner` — владелец диаграммы;
- `Diagram` — связь DiagramView с Diagram;
- `Model` — визуальный View ссылается на семантический элемент;
- `Context` — behavior связывается с контекстом.

Эти ссылки нельзя заменять только совпадением строковых имён.

## Коллекции

Формат хранит коллекции двумя частями:

```xml
<XPD:ATTR name="#OwnedElements" type="integer">...</XPD:ATTR>
<XPD:OBJ name="OwnedElements[0]" ...>
<XPD:OBJ name="OwnedElements[1]" ...>
```

То же встречается для:

- `OwnedDiagrams`;
- `Views`;
- `Behaviors`;
- `Subvertices`;
- `Transitions`;
- `Associations`;
- `Connections`;
- `Attributes`;
- `Operations`;
- и других коллекций.

Поэтому после структурных изменений надо проверять не только XML-синтаксис, но и счётчики.

## Use Case relationships

### include

Семантический объект `UMLInclude` содержит:

- `Base` — базовый Use Case;
- `Addition` — включаемый Use Case.

Визуально ему соответствует `UMLIncludeView`.

### extend

`UMLExtend` содержит:

- `Base` — расширяемый Use Case;
- `Extension` — расширяющий Use Case;
- иногда `Condition`.

Визуально ему соответствует `UMLExtendView`.

### Association

`UMLAssociation` содержит `Connections[i]` типа `UMLAssociationEnd`. Каждый end ссылается на `Participant`.

## Activity

В lending Activity Diagram не является корневым поведением сама по себе:

```text
UMLActivityGraph
  ├─ Top: UMLCompositeState
  │   ├─ UMLPseudostate
  │   ├─ UMLActionState
  │   ├─ UMLObjectFlowState
  │   └─ ...
  ├─ UMLTransition...
  └─ UMLActivityDiagram
      └─ UMLActivityDiagramView
```

Поэтому при генерации Activity надо создавать не только визуальную Diagram.

## Statechart

Аналогично:

```text
UMLStateMachine
  ├─ Top / states
  ├─ transitions
  └─ UMLStatechartDiagram
```

## Class

Семантические классы содержат `UMLAttribute` и `UMLOperation`. DiagramView содержит отдельные compartment views:

- `UMLNameCompartmentView`;
- `UMLAttributeCompartmentView`;
- `UMLOperationCompartmentView`;
- `UMLTemplateParameterCompartmentView`.

Следовательно, «нарисовать прямоугольник с текстом» недостаточно для полноценного StarUML Class element.

## Component / Deployment / Sequence

Эти типы также используют разделение model/view. В lending особенно важны:

- `UMLComponent` и `UMLComponentView`;
- node/component instances для deployment;
- `UMLInteractionInstanceSet`, `UMLStimulus`, `UMLSeqStimulusView` для sequence.

## Инварианты нашего сборщика

1. Каждый GUID объявлен не более одного раза.
2. Каждый `XPD:REF` разрешается.
3. Общая сущность не дублируется из-за появления на новой диаграмме.
4. Счётчики коллекций синхронизированы.
5. Semantic object и View не путаются.
6. Итоговый XML остаётся одним `UMLProject`.
