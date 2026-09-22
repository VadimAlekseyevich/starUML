# Use Case Diagram — эталон + методичка

## Быстрый маршрут

1. Методические правила: `../../methodology/functionality.md`.
2. Рисунки методички: `../../methodology/MEDIA_MAP.md`, прежде всего P0093/P0095/P0110/P0114.
3. Эталонный XML: `applying_for_loan.fragment.xml`.
4. Эталонные изображения: `Костыль/диаграммы/*_UseCase_*.jpg`.
5. Текущая Urban Development модель: `../../dist/urban_development.uml`.

## Основной XML-эталон

[applying_for_loan.fragment.xml](./applying_for_loan.fragment.xml)

![ApplyingForLoan Use Case](../../../Костыль/диаграммы/ApplyingForLoan_UseCase_TO_BE.jpg)

## Что подтверждает методичка

Use Case — функция/процесс [METHOD: P0063–P0066].

Основная модель должна быть не одной диаграммой, а системой «основная + декомпозиционные» [METHOD: P0102–P0103].

На основной диаграмме обычно 3–9 относительно независимых Use Case, без частичной декомпозиции [METHOD: P0104–P0107].

Декомпозиционная диаграмма обязана содержать декомпозируемый Use Case как логический центр [METHOD: P0112].

## Очень важный момент: worker

Методичка отличает внешнего Actor от человека, который является частью системы. Внутренний сотрудник создаётся как Class со стереотипом `worker` [METHOD: P0121–P0135].

Это объясняет реальный `lending.uml`:

- `Клиент` — `UMLActor`;
- `Менеджер` — `UMLClass` со стереотипом worker/caseWorker.

Поэтому наша структура `Пользователь` + `ГИС-аналитик` не является случайным наследием шаблона; она соответствует методике, если ГИС-аналитик действительно является внутренним работником системы.

## StarUML-типы

- `UMLUseCase`;
- `UMLActor`;
- `UMLClass` + worker stereotype;
- `UMLAssociation`;
- `UMLInclude`;
- `UMLExtend`;
- `UMLUseCaseDiagram`;
- соответствующие `*View`.

## include / extend

`include` — обязательная часть реализации base Use Case [METHOD: P0083–P0085].

`extend` — условная дополнительная часть [METHOD: P0084–P0085].

У `extend` должно быть конкретное свойство `Condition` [METHOD: P0161–P0163].

## Documentation

Все узлы и стрелки должны иметь Documentation, а стрелки — обоснование выбранного отношения [METHOD: P0149–P0163].

## Urban Development

Сейчас есть `UrbanDevelopment`, `ProjectCreation`, `DataManagement`, `ScenarioConfiguration`, `ScenarioLaunch`, `GenerationExecution`.

Методический аудит текущего состояния: `../../methodology/audits/current-functionality-audit.md`.
