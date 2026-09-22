# State Machine Diagram — методичка + старый эталон

> Legacy XML относится к StarUML 5. Новые автоматы строятся в каноническом StarUML 7 MDJ.

## Источники

- `../../methodology/statecharts.md`;
- methodology media;
- `Authorization_StatechartDiagramm_TO_BE.jpg`;
- `ViewCatalogProduct_Statechart_TO_BE.jpg`;
- legacy `authorization.fragment.xml`.

## Что подтверждает методичка

State Machine = состояния + переходы [METHOD: P0279–P0283].

Это реализация сценария/Use Case [METHOD: P0286–P0287].

Сценарии могут декомпозироваться [METHOD: P0288–P0298].

## Legacy lending

Старый storage:

`UMLStateMachine → TOP/composite states → transitions → UMLStatechartDiagram`.

Используем как техническую справку, но не повторяем XPD вручную.

## Urban Development

Кандидат: lifecycle запуска сценария — Draft/Validated/Queued/Running/Completed/Failed/Cancelled.
