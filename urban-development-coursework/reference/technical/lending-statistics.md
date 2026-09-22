# Статистика lending.uml

Количество основных объектов, реально найденных в эталоне:

| Тип | Количество |
|---|---:|
| UMLProject | 1 |
| UMLModel | 4 |
| UMLPackage | 20 |
| UMLUseCaseDiagram | 8 |
| UMLUseCase | 56 |
| UMLActor | 1 |
| UMLAssociation | 55 |
| UMLInclude | 15 |
| UMLExtend | 31 |
| UMLActivityGraph | 5 |
| UMLActivityDiagram | 5 |
| UMLStateMachine | 4 |
| UMLStatechartDiagram | 4 |
| UMLClassDiagram | 13 |
| UMLClass | 50 |
| UMLComponentDiagram | 8 |
| UMLComponent | 31 |
| UMLDeploymentDiagram | 2 |
| UMLSequenceDiagram | 1 |

## Что эта статистика показывает

### Диаграмм действительно много

Эталонная курсовая не построена как «по одной диаграмме каждого вида». Например, Class Diagram — 13, Use Case — 8, Component — 8.

### Visual model очень крупная

Один семантический объект создаёт множество вспомогательных view/label/compartment objects. Поэтому размер файла в мегабайтах не означает такое же количество самостоятельных предметных сущностей.

### include/extend не редкость

В файле 15 `UMLInclude` и 31 `UMLExtend`. Это подтверждает, что преподавательский пример действительно использует отношения между Use Case, а не только actor-usecase associations.

## Как использовать статистику правильно

Количество из lending — ориентир сложности и структуры, **не квота**. Для Urban Development количество схем определяется предметной областью и требованиями, а не попыткой получить ровно 13 Class Diagram или 31 extend.
