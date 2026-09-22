# Scripts

После перехода на StarUML 7 скрипты делятся на активные document/reference utilities и legacy StarUML 5 tooling.

## Активно

### StarUML 7 audit

`audit_staruml7.py` проверяет канонический `.mdj`: уникальность `_id`, разрешимость `$ref`, покрытие Activity, вызовы декомпозиционных Activity через `UMLCallBehaviorAction`, правило одного входа в Action, guards/`else`, содержательность Documentation, State Machine, Use Case → behavior traceability и базовую геометрию подписей/узлов без наложений.

```bash
python scripts/audit_staruml7.py 01_functionality/urban_development_functionality.mdj --traceability model/traceability.json
```

### Методичка

`extract_methodology_docx.py` извлекает из `методичка.docx` текст, таблицы и изображения.

### Lending reference

```bash
python scripts/extract_lending_examples.py ../lending.uml reference
```

Извлекает точные XML-фрагменты старого эталона. Они используются только для изучения.

## Legacy StarUML 5

### build_uml.py

Собирает старые fragments в `dist/urban_development.uml`.

### validate_uml.py

Проверяет XPD/XML, GUID, XPD:REF и legacy reverse relations.

### audit_functionality.py

Проверяет первую XPD-версию функциональной модели.

Эти инструменты сохраняются для воспроизводимости, но **не входят в обычный workflow StarUML 7**.

## Текущий запуск

Использовать корневой:

`run_coursework.bat`

Он выполняет pull и открывает канонический `.mdj` в StarUML 7.

## Развитие validator

`audit_staruml7.py` уже покрывает структуру `.mdj` и вторую работу. На следующих этапах его следует расширить проверками:

- Activity action → Class operation;
- Sequence message → receiver operation;
- Class → Component → Deployment coverage.

Новый XPD-компилятор больше не строим.
