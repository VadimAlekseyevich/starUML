# StarUML 7 MDJ — текущий формат

Канонический проект:

`../../01_functionality/urban_development_functionality.mdj`

MDJ — JSON-модель StarUML 7.

## Базовая структура

```json
{
  "_type": "Project",
  "_id": "...",
  "ownedElements": []
}
```

Model elements содержат `_type`, `_id`, `_parent`.

Ссылки:

```json
{ "$ref": "<id>" }
```

## Идентичность

После импорта старые GUID сохранились как `_id`.

Поэтому registry/traceability первой работы можно продолжать использовать.

## Model vs View

Например:

- `UMLUseCase` — semantic element;
- `UMLUseCaseView` — отображение;
- View содержит `model: { "$ref": "..." }`.

Один Use Case может показываться на нескольких диаграммах без дублирования model element.

## Отношения

В импортированном MDJ include/extend представлены semantic elements со `source` и `target` через `$ref`.

Это намного удобнее для будущей автоматической проверки, чем XPD reverse collections.

## Documentation

Documentation хранится непосредственно у model element.

Attachments первой работы после импорта представлены tags; дальше способ внешних вложений можно упрощать, если методичка/преподаватель не требует именно file attachment внутри редактора.

## Будущий validator

Проверять:

1. уникальные `_id`;
2. разрешимые `$ref`;
3. View → model type consistency;
4. отсутствие semantic duplicates;
5. traceability;
6. cross-diagram contract.

Мы не строим собственный генератор MDJ: StarUML 7 остаётся основным редактором.
