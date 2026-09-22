# Структура проекта: legacy и StarUML 7

## Старый lending.uml

Legacy-проект имеет четыре верхних UMLModel:

1. Use Case View;
2. Logical View;
3. Component View;
4. Deployment View.

При этом содержательные Component/Deployment Diagram местами лежат в Logical View. Это историческая особенность проекта, а не универсальное правило.

## Что сохраняем

Activity размещаем в Logical View, потому что это прямо требует METHOD [P0201].

Остальные диаграммы организуем логично в одном StarUML 7 проекте, не копируя странности старого дерева только ради сходства.

## Текущий проект

Импорт StarUML 7 сохранил существующие Views и `_id`, поэтому первую работу не перестраиваем без причины.

Новые этапы добавляем в этот же `.mdj`.

Сравнение форматов:

- [../technical/xpd-format.md](../technical/xpd-format.md);
- [../technical/mdj-format.md](../technical/mdj-format.md).
