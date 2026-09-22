# Scripts

Все скрипты используют только стандартную библиотеку Python.

## Сборка

```bash
python scripts/build_uml.py
```

По умолчанию читается `fragments/manifest.json`, фрагменты объединяются **как байты** в заданном порядке, затем выполняется базовая XML/GUID-проверка и создаётся `dist/urban_development.uml`.

Текущая сборка намеренно крупнозернистая: один фрагмент = один корневой StarUML View. Это безопаснее, пока не реализована автоматическая зависимость каждой диаграммы от общих model elements.

## Валидация

```bash
python scripts/validate_uml.py dist/urban_development.uml \
  --registry model/registry.json \
  --forbid кредит --forbid заявк --forbid платеж
```

Проверяется:

- XML читается;
- GUID уникальны;
- каждый `XPD:REF` разрешается;
- имена и связи совпадают с machine registry;
- запрещённые остатки исходной банковской предметной области отсутствуют;
- счётчики коллекций проверяются как warnings (или errors с `--strict-counts`).

## Извлечение lending reference

```bash
python scripts/extract_lending_examples.py ../lending.uml reference
```

Скрипт извлекает точные текстовые объекты диаграмм без пересериализации XML.

## Почему пока не режем Use Case View на десятки файлов

Модель StarUML не является набором независимых картинок. DiagramView ссылается на UseCase/Actor/Association через GUID, а один и тот же объект может быть показан на нескольких схемах.

До появления dependency-aware builder мелкое физическое дробление сборочных файлов создаёт больше риска, чем пользы. В `reference/` мелкие фрагменты разрешены, потому что они используются только как документация.
