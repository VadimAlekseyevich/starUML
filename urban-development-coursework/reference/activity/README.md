# Activity Diagram — методичка + старый эталон

> XML/ActivityGraph ниже относятся к StarUML 5. Новые Activity строятся непосредственно в StarUML 7 MDJ.

## Маршрут

1. `../../methodology/algorithms.md`;
2. methodology media;
3. Activity JPG из `Костыль`;
4. legacy XML `applying_for_loan.fragment.xml` при необходимости;
5. реализация в StarUML 7.

## Методические правила

Activity Diagram реализует Use Case [METHOD: P0219].

Для каждого Use Case первого уровня требуется поведенческая реализация [METHOD: P0220; P0225].

Activity помещается в Logical View [METHOD: P0201].

Decision использует реальные guards и `else`, а не «Да/Нет» [METHOD: P0227–P0229].

Swimlanes показывают логические действия ролей [METHOD: P0234–P0239].

Узлы/переходы документируются [METHOD: P0251–P0256].

## Legacy StarUML 5

В lending storage был:

`UMLActivityGraph → TOP → states/transitions → UMLActivityDiagram`.

Это пример внутреннего формата старого редактора, а не требование к StarUML 7.

## Старые изображения

- ApplyingForLoan;
- ApplicationApproval;
- CreditRegistration;
- LoanRepayment.

Используем их как визуальный ориентир композиции.
