# Дерево проекта lending.uml

Это не пересказ по названиям файлов, а структура, реально извлечённая из `lending.uml`.

## Use Case View

- `AS IS`
  - Use Case Diagram `Lending`
- `TO BE`
  - `CreditProductManagement`
  - `LoanRepayment`
  - `CreditRegistration`
  - `ApplyingForLoan`
  - `Login`
  - `Lending`
  - `Main`

## Logical View

На этом уровне находится большая часть содержательной модели.

### Поведение

- Activity Graph `ApplyingForLoan` → Activity Diagram `ApplyingForLoan`
- Activity Graph `ApplicationApproval` → Activity Diagram `ApplicationApproval`
- Activity Graph `CreditRegistration` → Activity Diagram `CreditRegistration`
- Activity Graph `LoanRepayment` → Activity Diagram `LoanRepayment`
- State Machine `ClientStatechartDiagram`
- State Machine `AuthorizationStatechartDiagramm`
- State Machine `ViewCatalogProductStatechart`
- State Machine `CreditRegistrationStatechart`

### Class

Пакет `Class` содержит 12 основных Class Diagram:

- `AuthPackages`
- `AuthDetailClass`
- `AuthDetailClassWithRelation`
- `ProductsCatalogPackages`
- `ProductsCatalogDetailClass`
- `ProductsCatalogDetailClassWithRelation`
- `ClassEntityPackeges`
- `ClassEntityDetail`
- `ClassEntityDetailWithRelation`
- `ClassEntityPackeges_`
- `ControlClass`
- `BoundaryClass`

Внутри также есть отдельные пакеты boundary/control/entity для разных функциональных областей.

### AS IS

В `Logical View / AS IS` лежат:

- Activity Graph `ConsultationOnCreditProducts`;
- пакет `Architecture`;
- Class Diagram `Main`;
- дополнительные предметные пакеты.

### Arch

- Deployment Diagram `Lending`

### Component

- `ClientClient`
- `ClientServer`
- `ManagerClient`
- `ManagerServer`
- `Service`
- `Executable`
- `artifact`

### Interface

Sequence Diagram вложена глубже обычного:

`Interface → CollaborationInstanceSet1 → InteractionInstanceSet1 → SequenceDiagram1`.

## Component View

- Component Diagram `Main`

Содержательная компонентная модель при этом находится в `Logical View / Component`.

## Deployment View

- Deployment Diagram `Main`

Содержательная диаграмма размещения при этом находится в `Logical View / Arch`.

## Вывод для нашего проекта

Нельзя строить генератор на предположении «тип диаграммы = одноимённый верхний View». В старом StarUML `View` — часть организации проекта, а реальные диаграммы могут принадлежать пакетам/behavior внутри `Logical View`.

Поэтому структура Urban Development будет повторять **модель организации lending**, а не только четыре стандартных названия View.
