# State Machine Diagram — эталон + методичка

## Быстрый маршрут

- Методика: `../../methodology/statecharts.md`.
- Изображения методички: P0303, P0306, P0309 и последующие в `../../methodology/MEDIA_MAP.md`.
- XML-эталон: `authorization.fragment.xml`.
- JPG: `Authorization_StatechartDiagramm_TO_BE.jpg`, `ViewCatalogProduct_Statechart_TO_BE.jpg`.

## XML-эталон

[authorization.fragment.xml](./authorization.fragment.xml)

![Authorization Statechart](../../../Костыль/диаграммы/Authorization_StatechartDiagramm_TO_BE.jpg)

## Назначение

State Machine — состояние + переходы; стрелка может иметь Trigger, Guard Condition и Effect [METHOD: P0279–P0283].

Диаграмма автомата рассматривается как алгоритмическая реализация конкретного сценария/Use Case [METHOD: P0286–P0287].

## Декомпозиция

Методичка предлагает строить сценарий по Actor, затем детализировать реализуемые им Use Case и вспомогательные процессы [METHOD: P0288–P0298].

## StarUML-структура

В `lending.uml`:

`UMLStateMachine → UMLCompositeState(TOP) / states / transitions → UMLStatechartDiagram`.

## Urban Development

Естественные кандидаты — lifecycle `GenerationRun`, `Job`, `DatasetVersion`, но State Machine следует вводить только как часть реализации реального сценария, а не для количества.
