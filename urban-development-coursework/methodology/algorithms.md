# 2. Модель алгоритмов

## Назначение

Поведение ИС — совокупность процессов [METHOD: P0180–P0183].

Поведенческие диаграммы: State Machine, Activity, Sequence, Communication [METHOD: P0184–P0189].

Для второй работы основной инструмент — **Activity Diagram**.

## Связь с Use Case

Поведенческая диаграмма реализует Use Case [METHOD: P0219].

Для каждого Use Case основной диаграммы должна существовать поведенческая реализация [METHOD: P0220].

Для Activity это требование повторено в P0225 и P0241–P0245.

## StarUML 5 vs StarUML 7

Методичка P0202–P0206 описывает старый StarUML 5 через `ActivityGraph` и `TOP`.

Это полезно для чтения `lending.uml`, но **не требует воспроизводить XPD-контейнеры**.

В StarUML 7 Activity Diagram строим штатными средствами в каноническом `.mdj`, сохраняя семантику:

- действия;
- деятельности;
- переходы;
- guards;
- decision/merge;
- swimlanes;
- декомпозицию.

Размещение в `Logical View` сохраняем, потому что это прямо требует методичка [METHOD: P0201].

## Action / Subactivity

Action — элементарное/понятное действие [METHOD: P0191–P0194].

Нетривиальная деятельность, требующая отдельного алгоритма, должна иметь свою декомпозицию [METHOD: P0193–P0196; P0255].

В StarUML 7 конкретное название toolbox-элемента может отличаться от старого `ActionState/SubactivityState`; важен смысл декомпозиции.

## Ветвления

Не писать «Да/Нет» [METHOD: P0227–P0229].

Пишем реальные guards:

- `[данные корректны]`;
- `[обнаружена критическая ошибка]`;
- `[else]`.

## Swimlanes

Человек выполняет логическое действие, а не «нажимает мышь» [METHOD: P0234–P0236].

Для наших Activity разумная базовая гранулярность:

- Пользователь;
- Система.

Технические Frontend/API/Worker появляются только там, где уровень алгоритма действительно требует архитектурной детализации [METHOD: P0239].

## Documentation

Узлы и переходы документируются [METHOD: P0251–P0256].

## План второй работы

Нужно создать Activity Diagram:

1. `ProjectCreation`;
2. `DataManagement`;
3. `ScenarioConfiguration`;
4. `ScenarioLaunch`;
5. `ScenarioComparison`;
6. `ResultExport`.

Дополнительно:

- `GenerationExecution` — детальная Activity генерационного pipeline;
- State Machine для lifecycle запуска сценария, если она помогает раскрыть алгоритм.

Канонический pipeline проекта:

`prepare_snapshot → evaluate_constraints → suitability → zoning → roads → blocks_and_parcels → buildings → demography → infrastructure → final_validation → metrics → persist_manifest`.

Именно от этой предметной логики, а не от формы lending, строится новая алгоритмическая модель.


## Статус выполнения

Работа 2 реализована в каноническом `.mdj` в `Logical View`.

Созданы:

- `ProjectCreation` — Activity Diagram для «Создать проект»;
- `DataManagement` — Activity Diagram для «Управление исходными геоданными»;
- `ScenarioConfiguration` — Activity Diagram для «Настроить сценарий развития»;
- `ScenarioLaunch` — Activity Diagram для «Запустить сценарий развития»;
- `ScenarioComparison` — Activity Diagram для «Просмотр и сравнение сценариев»;
- `ResultExport` — Activity Diagram для «Экспортировать результаты»;
- `GenerationExecution` — детальная Activity Diagram генерационного pipeline;
- `GenerationRunLifecycle` — State Machine состояний запуска.

Все шесть Use Case первого уровня связаны с behavior diagram в `model/traceability.json`.


## Повторная сверка с первоисточниками

22.09.2026 модель алгоритмов повторно проверена по полному извлечению `методичка.docx` и полному `lending.uml`.

Практически значимые уточнения:

- [METHOD: P0225; P0246; P0255] — сложные вызываемые деятельности должны иметь отдельные диаграммы; поэтому добавлены `DatasetImport`, `DataQualityValidation`, `ScenarioValidation`, а `GenerationExecution` оформлена как реальная вызываемая деятельность;
- [METHOD: P0274–P0275] — у Action должен быть один вход; возвратные и альтернативные потоки теперь сходятся в merge до Action;
- [METHOD: P0227–P0229] — резервные ветви приведены к `[else]`;
- [METHOD: P0251–P0256] — Documentation расширена от формального повторения названия до описания входов, проверок, изменений состояния и результата;
- визуальная раскладка разрежена: увеличены swimlane, расстояния между рядами и пространство для guard-меток.

Подробности и сравнение с lending см. `audits/algorithms-second-review.md`.
