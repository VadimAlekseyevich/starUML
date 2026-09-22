# Диаграмма автомата / State Machine

## Назначение

State Machine — совокупность состояний и переходов [METHOD: P0279–P0283].

Методичка рассматривает State Machine как алгоритмическую реализацию сценария/Use Case, а не как декоративную диаграмму [METHOD: P0286–P0287].

## Поакторная модель

Разработку рекомендуется вести по Actor: сначала общий сценарий взаимодействия, затем реализация Use Case и вспомогательных процессов [METHOD: P0288–P0298].

## Иерархия

Сложное поведение показывается укрупнённо и затем декомпозируется [METHOD: P0291–P0297].

## StarUML 5 / StarUML 7

Старый `lending.uml` хранит автоматы через legacy `UMLStateMachine → TOP/composite state → transitions → UMLStatechartDiagram`.

Это полезно как reference структуры старого файла, но в StarUML 7 мы создаём State Machine штатными средствами и сохраняем только UML-семантику состояний, transitions, trigger/guard/effect и decomposition.

## Urban Development

Хороший кандидат:

`GenerationRunLifecycle`

Возможные состояния:

`Draft → Validated → Queued → Running → Completed / Failed / Cancelled`

Такая диаграмма имеет смысл только как часть реализации реального сценария запуска/выполнения, а не «для количества».
