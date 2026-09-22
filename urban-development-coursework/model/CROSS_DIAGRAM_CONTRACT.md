# Cross-diagram contract

Этот документ задаёт правила согласованности между разными UML-представлениями Urban Development Generator.

## 1. Semantic identity

Один предметный элемент = один semantic object = один GUID.

Если один Use Case показан на трёх диаграммах, создаются три View одного `UMLUseCase`, а не три разных `UMLUseCase` с одинаковым названием.

Источник идентичностей: `registry.json / registry.yaml`.

## 2. Use Case → Behavior

Каждый финализированный Use Case основной диаграммы должен иметь алгоритмическую реализацию [METHOD: P0220; P0225].

В `traceability.json` для него фиксируется:

- decomposition diagram;
- behavior diagram;
- статус покрытия.

Имя алгоритма должно явно трассироваться к реализуемому Use Case.

## 3. include / extend ↔ текстовый поток

Безусловный подпоток `S...` должен быть согласован с `include`.

Условный подпоток `S... [condition]` должен быть согласован с `extend`, а текст условия — с `UMLExtend.Condition` [METHOD: P0161–P0172].

Нельзя, чтобы диаграмма говорила `include`, а текстовый алгоритм описывал условный вызов.

## 4. Activity → Class

Действия системы не исчезают при переходе к Class Model: они превращаются в операции классов [METHOD: P0355–P0357; P0378].

Если Action/Activity реализуется конкретным control/boundary/entity классом, это должно быть отражено в Class Model.

Ориентир ActionState → Class не является механическим правилом 1:1 [METHOD: P0379–P0380].

## 5. Class package → Class detail

Каждый класс, показанный в package view, должен существовать в detail view [METHOD: P0450–P0452].

Validator должен считать отсутствие детального класса ошибкой логической целостности после финализации Class Model.

## 6. Class → Sequence

Каждый объект Sequence Diagram имеет тип-класс.

Каждое сообщение, входящее в lifeline объекта, должно соответствовать операции класса-получателя [METHOD: P0496–P0501].

Создание объекта согласуется с constructor/create dependency, уничтожение — destroy semantics.

## 7. Class → Component

Component Model группирует реализацию классов/пакетов на более крупном программном уровне.

Компонент не вводит новую прикладную терминологию, если уже существует соответствующий пакет/подсистема Class Model.

Boundary/control/entity — аналитическая классификация классов; Frontend/API/Core/Worker — архитектурные компоненты. Это разные уровни и они должны быть связаны, а не смешаны.

## 8. Component → Deployment

Каждый исполняемый software component должен иметь понятное соответствие deployment artifact/service/node.

Канонический словарь: `architecture.yaml`.

Например:

- Backend API → compose service `api`;
- Worker → `worker`;
- PostgreSQL/PostGIS → `db`;
- Redis → `redis`;
- Frontend → `frontend`.

## 9. Actor / worker consistency

Внешний пользователь — Actor.

Внутренний человек, выполняющий часть системной функциональности, — worker/Class [METHOD: P0121–P0135].

Одна и та же роль не должна в разных диаграммах произвольно становиться то Actor, то внутренним worker.

## 10. Documentation

Документация является частью модели, а не пояснительной запиской «после UML».

Use Case relation Documentation должна объяснять тип связи [METHOD: P0149–P0163].

Activity Documentation уточняет действия и переходы [METHOD: P0251–P0256].

Class detail документирует members и relations [METHOD: P0408–P0410].

## 11. Rename protocol

Переименование semantic element требует одновременно:

1. изменения canonical registry;
2. изменения semantic object Name;
3. обновления Documentation;
4. обновления traceability;
5. проверки текстовых потоков;
6. проверки diagram captions/report references.

GUID при обычном переименовании **не меняется**, потому что идентичность элемента остаётся прежней.

## 12. Delete protocol

Перед удалением semantic object validator должен доказать отсутствие:

- View на диаграммах;
- XPD:REF;
- traceability links;
- cross-model references.

Удаление подписи/View не равно удалению semantic object.
