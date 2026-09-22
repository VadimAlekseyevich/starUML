# Build fragments — legacy StarUML 5 layer

Каталог содержит XPD/XML-сборку, использованную до перехода на StarUML 7.

Состав:

1. `project_prefix.xml`;
2. `views/00_use_case_view.xml`;
3. `views/10_logical_view.xml`;
4. `views/20_component_view.xml`;
5. `views/30_deployment_view.xml`;
6. `project_suffix.xml`.

## Статус

**Замороженный legacy. Не использовать для новых работ.**

Фрагменты нужны только для истории миграции и технического анализа старого `lending.uml`.

После импорта источником истины является `.mdj`.

Dependency-aware XPD builder, дальнейшее дробление XML и ручное управление GUID/counters больше не являются задачами курсача.
