# Use Case Diagram — методичка + старый эталон

> XML ниже — legacy StarUML 5 reference. Новая модель живёт в `../../01_functionality/urban_development_functionality.mdj`.

## Маршрут

1. `../../methodology/functionality.md`;
2. изображения методички;
3. JPG из `Костыль`;
4. `applying_for_loan.fragment.xml` — только если нужно глубже понять lending;
5. реализация в StarUML 7.

## Что подтверждает методичка

Use Case — функция/процесс [METHOD: P0063–P0066].

Модель: основная + декомпозиционные [METHOD: P0102–P0103].

На основном уровне обычно 3–9 независимых Use Case без частичной декомпозиции [METHOD: P0104–P0107].

Декомпозиция содержит базовый Use Case как логический центр [METHOD: P0112].

## Worker

Внутренний человек моделируется как Class со stereotype worker/caseWorker [METHOD: P0121–P0135].

Именно поэтому `ГИС-аналитик` не Actor.

## include / extend

- include — обязательная функция;
- extend — условная;
- extend имеет содержательный condition [METHOD: P0083–P0085; P0161–P0163].

## Documentation

Все элементы и связи документируются [METHOD: P0149–P0163].

## Старый образец

- XML: `applying_for_loan.fragment.xml`;
- JPG: `Костыль/диаграммы/ApplyingForLoan_UseCase_TO_BE.jpg`.

Используем композицию и уровень детализации, но не XPD-механику.
