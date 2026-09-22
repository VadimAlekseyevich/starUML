# Cross-diagram contract

## 1. Semantic identity

Один предметный элемент = один model element = один стабильный `_id`.

Несколько диаграмм показывают несколько View одной сущности, а не дубликаты.

Источник истины: канонический `.mdj`.

## 2. Use Case → Behavior

Каждый финализированный Use Case основной диаграммы имеет алгоритмическую реализацию [METHOD: P0220; P0225].

В `traceability.json` фиксируются decomposition и behavior diagram.

## 3. include / extend ↔ текстовый поток

Безусловный подпоток согласуется с include.

Условный подпоток согласуется с extend и его condition [METHOD: P0161–P0172].

## 4. Activity → Class

Действия системы превращаются в обязанности/операции классов [METHOD: P0355–P0357; P0378].

Не применять механическое «один Action = один Class» [METHOD: P0379–P0380].

## 5. Class package → detail

Каждый класс package view существует в detail view [METHOD: P0450–P0452].

## 6. Class → Sequence

Каждый lifeline типизирован классом.

Каждое входящее сообщение соответствует операции класса-получателя [METHOD: P0496–P0501].

## 7. Class → Component

Component Model группирует классы/пакеты на архитектурном уровне.

Boundary/control/entity и Frontend/API/Core/Worker — разные уровни модели.

## 8. Component → Deployment

Исполняемый компонент имеет понятное deployment mapping.

Канонический словарь: `architecture.yaml`.

## 9. Actor / worker

Внешний пользователь — Actor.

Внутренний человек — worker/Class [METHOD: P0121–P0135].

## 10. Documentation

Documentation — часть модели [METHOD: P0149–P0163; P0251–P0256; P0408–P0410].

## 11. Rename protocol

При переименовании:

1. изменить model element в `.mdj`;
2. не менять `_id`;
3. обновить Documentation;
4. обновить traceability;
5. проверить flows и подписи.

## 12. Delete protocol

Перед удалением проверить отсутствие:

- View;
- `$ref` на `_id`;
- traceability links;
- cross-model references.

Удаление View не означает удаление semantic element.

### Legacy

В XPD аналогом `_id/$ref` были GUID/XPD:REF. Эти правила нужны только для чтения старого `lending.uml`.
