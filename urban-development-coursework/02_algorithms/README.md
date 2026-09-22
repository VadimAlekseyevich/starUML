# 02 — Модель алгоритмов системы

Вторая работа выполнена непосредственно в каноническом StarUML 7 проекте:

`../01_functionality/urban_development_functionality.mdj`

Отдельный `.mdj` не создаётся: идентичность элементов и трассировка между этапами сохраняются в одном проекте.

## Покрытие Use Case первого уровня

| Use Case | Activity Diagram |
|---|---|
| Создать проект | `ProjectCreation` |
| Управление исходными геоданными | `DataManagement` |
| Настроить сценарий развития | `ScenarioConfiguration` |
| Запустить сценарий развития | `ScenarioLaunch` |
| Просмотр и сравнение сценариев | `ScenarioComparison` |
| Экспортировать результаты | `ResultExport` |

Дополнительно создана `GenerationExecution` — детальная Activity Diagram для внутреннего генерационного pipeline.

## State Machine

`GenerationRunLifecycle` описывает состояния запуска:

`Draft → Validated → Queued → Running → Completed / Failed / Cancelled`.

Она дополняет `ScenarioLaunch` и `GenerationExecution`, а не заменяет Activity Diagram.

## Методические решения

- поведенческая реализация есть у каждого Use Case первого уровня [METHOD: P0219–P0225; P0241–P0245];
- используются содержательные guards вместо «Да/Нет» [METHOD: P0227–P0229];
- действия разделены по swimlane пользователя/системы, а в генерационном pipeline выделен Worker [METHOD: P0234–P0239];
- действия и переходы имеют Documentation [METHOD: P0251–P0256];
- State Machine используется только там, где предметная логика действительно имеет жизненный цикл [METHOD: P0279–P0298].

## Трассировка

Каноническая связь Use Case → Activity хранится в `../model/traceability.json`.

Следующая работа: **модель классов системы**.
