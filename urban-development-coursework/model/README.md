# Canonical model registry

После перехода на StarUML 7 источником истины является канонический `.mdj`.

## Идентичность

Каждый model element имеет `_id`.

Импорт сохранил старые GUID как значения `_id`, поэтому идентичность первой модели не потеряна.

`registry.json / registry.yaml` — теперь **индекс/проверочная проекция**, а не источник генерации UML.

## Файлы

- `registry.*` — индекс существующих элементов первой работы;
- `use_cases.yaml` — декомпозиция функциональности;
- `architecture.yaml` — канонические архитектурные названия;
- `traceability.json` — связь этапов;
- `CROSS_DIAGRAM_CONTRACT.md` — правила согласованности.

## Основная цепочка

`Use Case → Activity/State Machine → Class → Sequence → Component → Deployment`

Работа 2 обновила traceability: каждый Use Case первого уровня связан с Activity Diagram. Следующий этап — Class Model; он должен трассировать системные действия Activity в обязанности и операции классов.

## Переименование

Переименование выполняется в `.mdj`, Documentation и traceability.

`_id` при обычном переименовании не меняется.
