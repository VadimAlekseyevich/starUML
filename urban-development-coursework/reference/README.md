# Reference library

Эта папка — компактная, навигационная версия эталона `lending.uml` и связанных материалов.

## Центральный принцип

Перед созданием новой диаграммы не надо перечитывать весь `lending.uml`.

Маршрут:

`тип диаграммы → reference/<type>/README → methodology/<topic>.md → пример XML → изображение → generated/all-diagrams при необходимости`.

## Покрытие

| Тип | Методичка | Curated XML | Все XML-примеры lending | Картинки |
|---|---|---|---:|---|
| Use Case | да | да | 8 | `Костыль/диаграммы/*UseCase*` + methodology media |
| Activity | да | да | 5 | `*Activity*` + methodology media |
| State Machine | да | да | 4 | `*Statechart*` + methodology media |
| Class | да | да | 13 | Class/Boundary/Control images + methodology media |
| Sequence | да | да | 1 | methodology media / Interface reference |
| Component | нет отдельной главы | да | 8 | component images from `Костыль` |
| Deployment | нет отдельной главы | да | 2 | architecture/deployment images |

Полный машинный каталог: `generated/all-diagrams/catalog.json`.

## Curated vs generated

`reference/<type>/*.fragment.xml` — вручную выбранные учебные фрагменты, которые удобно читать и комментировать.

`reference/generated/all-diagrams/` — автоматически извлечены **все 41 диаграмма** из `lending.uml`:

- 8 Use Case;
- 5 Activity;
- 4 Statechart;
- 13 Class;
- 8 Component;
- 2 Deployment;
- 1 Sequence.

Generated-файлы не редактируются вручную; при изменении `lending.uml` их пересоздаёт GitHub Action.

## Структура проекта

`project-structure/` и `technical/` описывают XPD-формат, дерево `lending.uml`, GUID, semantic model vs View и collection counters.

## Методичка

Исходный DOCX хранится как `/методичка.docx`.

Автоматическая распаковка: `../methodology/source/`.

Карта правил: `../methodology/METHOD_INDEX.md`.

Карта изображений DOCX: `../methodology/MEDIA_MAP.md`.

## Важно

Reference fragment не обязательно является самодостаточным StarUML-файлом: он может ссылаться на semantic objects из других частей исходного проекта.

Для сборки Urban Development используются только `../fragments/` и registry/model-слой.
