# Структура StarUML-проекта

## Эталон lending.uml

На верхнем уровне `lending.uml` содержит четыре `UMLModel`:

1. `Use Case View`
2. `Logical View`
3. `Component View`
4. `Deployment View`

Точный сокращённый каркас: [lending_project_skeleton.fragment.xml](./lending_project_skeleton.fragment.xml).

## Важное наблюдение

Не все «реальные» диаграммы лежат в одноимённом верхнем View.

В эталоне:

- Use Case Diagram действительно находятся в `Use Case View`;
- Activity, Statechart, Class, большая часть Component и рабочая Deployment Diagram находятся внутри `Logical View` и его пакетов/behavior;
- верхние `Component View/Main` и `Deployment View/Main` фактически выступают как стандартные заготовки StarUML.

Поэтому при переносе структуры нельзя механически считать, что каждый тип диаграммы обязан жить только в одноимённом View. Для курсовой важнее повторять проверенную структуру эталона и сохранять связность модели.

## Наша структура

В Urban Development Generator уже созданы те же четыре верхнеуровневых View. Пока содержательной является Use Case View. Остальные View служат основой для следующих этапов.

## GUID

GUID верхних View нашего проекта намеренно совпадают с GUID исходного каркаса, на котором была построена первая версия модели. Не менять их без необходимости: большое количество ссылок может зависеть от них.
