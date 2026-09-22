# Каталог lending.uml

Этот файл автоматически составлен по структуре исходного `/lending.uml`. Он нужен как индекс: перед анализом большой XML-модели сначала смотрим сюда и открываем только нужный фрагмент.

## Сводка

| Тип | Количество |
|---|---:|
| Use Case | 8 |
| Activity | 5 |
| Statechart | 4 |
| Class | 13 |
| Component | 8 |
| Deployment | 2 |
| Sequence | 1 |

## Use Case

- `Lending` — GUID `N6lwPhX2SUGsbB1UUCtbHQAA`; владелец: `AS IS` → `Use Case View`.
- `CreditProductManagement` — GUID `3qmbEX3An0GTnpuD64Bh6QAA`; владелец: `TO BE` → `Use Case View`.
- `LoanRepayment` — GUID `NyGkKdYDKUqZt4hw2UJOqwAA`; владелец: `TO BE` → `Use Case View`.
- `CreditRegistration` — GUID `qlLdWAG4T0GKoaLKKEvUrwAA`; владелец: `TO BE` → `Use Case View`.
- `ApplyingForLoan` — GUID `KlF7MhujPkiEiDMBShlSAQAA`; владелец: `TO BE` → `Use Case View`.
- `Login` — GUID `hHr8110G1UmKIhw/XxGDPAAA`; владелец: `TO BE` → `Use Case View`.
- `Lending` — GUID `fjgg3vKMzEasR+L8Ny2FnQAA`; владелец: `TO BE` → `Use Case View`.
- `Main` — GUID `+P5V+QYHXUC5wLI0cV2loQAA`; владелец: `TO BE` → `Use Case View`.

## Activity

- `ApplyingForLoan` — GUID `EZ7mE6Q8ZkSByidD8h8EdwAA`; владелец: `ApplyingForLoan` → `Logical View`.
- `ApplicationApproval` — GUID `1BtccH+PcU2y2rscLjehrwAA`; владелец: `ApplicationApproval` → `Logical View`.
- `CreditRegistration` — GUID `iYYIW8VGEUSwzBWJ2EXv4QAA`; владелец: `CreditRegistration` → `Logical View`.
- `LoanRepayment` — GUID `gJSzNqK850WWfVobk1i42QAA`; владелец: `LoanRepayment` → `Logical View`.
- `ConsultationOnCreditProducts` — GUID `VgPH7GfIyUu62o5RxvhA3gAA`; владелец: `ConsultationOnCreditProducts` → `AS IS` → `Logical View`.

## Statechart

- `ClientStatechartDiagram` — GUID `tHlut8fReUWHuDrAnCvI0AAA`; владелец: `ClientStatechartDiagram` → `Logical View`.
- `AuthorizationStatechartDiagramm` — GUID `VaIZbvaeYE2Y0K3Sw5UB5gAA`; владелец: `AuthorizationStatechartDiagramm` → `Logical View`.
- `ViewCatalogProductStatechart` — GUID `/N9GDlkmPUqoFKz2ndH66QAA`; владелец: `ViewCatalogProductStatechart` → `Logical View`.
- `CreditRegistrationStatechart` — GUID `0GznlMlxsESAga21MhQC5AAA`; владелец: `CreditRegistrationStatechart` → `Logical View`.

## Class

- `AuthPackages` — GUID `4YmjspdXQUGOnotyDW6zeQAA`; владелец: `Class` → `Logical View`.
- `AuthDetailClass` — GUID `9FhQrRJ0O0iikuw0/fTr3gAA`; владелец: `Class` → `Logical View`.
- `AuthDetailClassWithRelation` — GUID `cgjRlX48vkOe2/ooOS8WRgAA`; владелец: `Class` → `Logical View`.
- `ProductsCatalogPackages` — GUID `qD2Hhi93d0GuRgm7c4nWdgAA`; владелец: `Class` → `Logical View`.
- `ProductsCatalogDetailClass` — GUID `BFIi59RalkKPfvSwW5LriwAA`; владелец: `Class` → `Logical View`.
- `ProductsCatalogDetailClassWithRelation` — GUID `KsuMKQPHBECItJT/hQBxyQAA`; владелец: `Class` → `Logical View`.
- `ClassEntityPackeges` — GUID `6dOTEQ4SckqGFb7EYBwOswAA`; владелец: `Class` → `Logical View`.
- `ClassEntityDetail` — GUID `BOndBiCvUEuBe1ge3X4uVwAA`; владелец: `Class` → `Logical View`.
- `ClassEntityDetailWithRelation` — GUID `eLAXJtA5EkifooirIOAwegAA`; владелец: `Class` → `Logical View`.
- `ClassEntityPackeges_` — GUID `C+RI+ux5xEO8EG7yYOeUpwAA`; владелец: `Class` → `Logical View`.
- `ControlClass` — GUID `S4x/xnz6xU6O7oNnz6vfQgAA`; владелец: `Class` → `Logical View`.
- `BoundaryClass` — GUID `QlPOehsWRUGjMPmxJOFkXwAA`; владелец: `Class` → `Logical View`.
- `Main` — GUID `2ejymZ3kgEKhhz7tNr0nkAAA`; владелец: `Architecture` → `AS IS` → `Logical View`.

## Component

- `ClientClient` — GUID `PH/KMHAzekeUR9K8eeWsXQAA`; владелец: `Component` → `Logical View`.
- `ClientServer` — GUID `vu1UVoBccEuzbXI57sPlewAA`; владелец: `Component` → `Logical View`.
- `ManagerClient` — GUID `CZ17q8FKeEi6xoKny2lr9AAA`; владелец: `Component` → `Logical View`.
- `ManagerServer` — GUID `pixa+MrfWUWfRKxRWK5TTAAA`; владелец: `Component` → `Logical View`.
- `Service` — GUID `J32zSa72I0aehsFYZLGEoQAA`; владелец: `Component` → `Logical View`.
- `Executable` — GUID `1d5naEx2f0Wi2b4duHLuawAA`; владелец: `Component` → `Logical View`.
- `artifact` — GUID `IKg8vF1pBku7Yt1O5qWUxAAA`; владелец: `Component` → `Logical View`.
- `Main` — GUID `Rs+lMQMNGUOD/YEOrhbkdQAA`; владелец: `Component View`.

## Deployment

- `Lending` — GUID `Qwf50Tgg80G18RrWjxuvTQAA`; владелец: `Arch` → `Logical View`.
- `Main` — GUID `aq+60CwkbU67mdh9VkirtwAA`; владелец: `Deployment View`.

## Sequence

- `SequenceDiagram1` — GUID `7I6JAkRe9EO2lKKVzQMfIQAA`; владелец: `InteractionInstanceSet1` → `CollaborationInstanceSet1` → `Interface`.

## Изображения из Костыль/диаграммы

- [ApplicationApproval_Activity_TO_BE.jpg](../../Костыль/диаграммы/ApplicationApproval_Activity_TO_BE.jpg)
- [ApplyingForLoan_Activity_TO_BE.jpg](../../Костыль/диаграммы/ApplyingForLoan_Activity_TO_BE.jpg)
- [ApplyingForLoan_UseCase_TO_BE.jpg](../../Костыль/диаграммы/ApplyingForLoan_UseCase_TO_BE.jpg)
- [Architecture.jpg](../../Костыль/диаграммы/Architecture.jpg)
- [AuthorizationStatechartDiagramm.jpg](../../Костыль/диаграммы/AuthorizationStatechartDiagramm.jpg)
- [Authorization_StatechartDiagramm_TO_BE.jpg](../../Костыль/диаграммы/Authorization_StatechartDiagramm_TO_BE.jpg)
- [BoundaryClass.jpg](../../Костыль/диаграммы/BoundaryClass.jpg)
- [ClassEntityDetail.jpg](../../Костыль/диаграммы/ClassEntityDetail.jpg)
- [ClassEntityDetailWithRelation.jpg](../../Костыль/диаграммы/ClassEntityDetailWithRelation.jpg)
- [ClassEntityPackeges.jpg](../../Костыль/диаграммы/ClassEntityPackeges.jpg)
- [ClientClient.jpg](../../Костыль/диаграммы/ClientClient.jpg)
- [ClientServer.jpg](../../Костыль/диаграммы/ClientServer.jpg)
- [ControlClass.jpg](../../Костыль/диаграммы/ControlClass.jpg)
- [CreditProductManagement_UseCase_TO_BE.jpg](../../Костыль/диаграммы/CreditProductManagement_UseCase_TO_BE.jpg)
- [CreditRegistration_Activity_TO_BE.jpg](../../Костыль/диаграммы/CreditRegistration_Activity_TO_BE.jpg)
- [CreditRegistration_UseCase_TO_BE.jpg](../../Костыль/диаграммы/CreditRegistration_UseCase_TO_BE.jpg)
- [Data_Full_ClassEntityPackeges_.jpg](../../Костыль/диаграммы/Data_Full_ClassEntityPackeges_.jpg)
- [Executable.jpg](../../Костыль/диаграммы/Executable.jpg)
- [Interface.jpg](../../Костыль/диаграммы/Interface.jpg)
- [Lending_Arch.jpg](../../Костыль/диаграммы/Lending_Arch.jpg)
- [Lending_UseCase_TO_BE.jpg](../../Костыль/диаграммы/Lending_UseCase_TO_BE.jpg)
- [LoanRepayment_Activity_TO_BE.jpg](../../Костыль/диаграммы/LoanRepayment_Activity_TO_BE.jpg)
- [LoanRepayment_UseCase_TO_BE.jpg](../../Костыль/диаграммы/LoanRepayment_UseCase_TO_BE.jpg)
- [Login_UseCase_TO_BE.jpg](../../Костыль/диаграммы/Login_UseCase_TO_BE.jpg)
- [ManagerClient.jpg](../../Костыль/диаграммы/ManagerClient.jpg)
- [ManagerServer.jpg](../../Костыль/диаграммы/ManagerServer.jpg)
- [Service.jpg](../../Костыль/диаграммы/Service.jpg)
- [UseCase_AS_IS.jpg](../../Костыль/диаграммы/UseCase_AS_IS.jpg)
- [ViewCatalogProduct_Statechart_TO_BE.jpg](../../Костыль/диаграммы/ViewCatalogProduct_Statechart_TO_BE.jpg)
- [ViewingLoan_UseCase_TO_BE.jpg](../../Костыль/диаграммы/ViewingLoan_UseCase_TO_BE.jpg)
- [artifact.jpg](../../Костыль/диаграммы/artifact.jpg)
- [deployment.jpg](../../Костыль/диаграммы/deployment.jpg)
- [rasm_art.jpg](../../Костыль/диаграммы/rasm_art.jpg)

## Практическое правило

Каталог описывает то, **что реально существует в lending.uml**, а не перечень того, что обязательно должно быть один-в-один в нашей предметной области. Решение о необходимости конкретной диаграммы принимается вместе с файлами `../methodology/` и требованиями курсовой.
