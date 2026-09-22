# Activity Diagram

## Эталон

XML: [applying_for_loan.fragment.xml](./applying_for_loan.fragment.xml)

![ApplyingForLoan Activity](../../../Костыль/диаграммы/ApplyingForLoan_Activity_TO_BE.jpg)

Другие эталонные изображения:

- `ApplicationApproval_Activity_TO_BE.jpg`;
- `CreditRegistration_Activity_TO_BE.jpg`;
- `LoanRepayment_Activity_TO_BE.jpg`.

## Структура lending.uml

Activity Diagram хранится не как один плоский объект. В `Logical View` существует `UMLActivityGraph`, содержащий состояние `TOP`, вершины и переходы. Внутри graph находится `UMLActivityDiagram` с визуальными View.

Характерные элементы:

- `UMLActivityGraph`;
- `UMLCompositeState` (TOP);
- `UMLPseudostate` — начальные/служебные узлы;
- `UMLActionState` — действия;
- `UMLObjectFlowState` — объектные состояния/элементы потока;
- `UMLTransition`;
- `UMLSwimlaneView` — дорожки;
- `UMLActivityDiagram` и `UMLActivityDiagramView`.

## Связь с Use Case

В lending названия Activity Graph часто совпадают с детализируемым прецедентом: например `ApplyingForLoan`, `CreditRegistration`, `LoanRepayment`.

Это важное правило согласованности для нашей модели: алгоритм реализации функции должен явно соответствовать функции из Use Case Model, а не существовать под случайным новым названием.

## Для urban-development

Первыми кандидатами на Activity Diagram являются нетривиальные сценарии:

- настройка сценария;
- импорт и валидация геоданных;
- запуск сценария;
- выполнение генерационного конвейера;
- сравнение вариантов/результатов.

Мелкие операции не обязаны получать отдельную большую Activity Diagram, если их алгоритм тривиален.
