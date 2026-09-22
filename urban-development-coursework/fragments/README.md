# Build fragments

Это **сборочные** фрагменты Urban Development StarUML project.

Они отличаются от `reference/*.fragment.xml`:

- reference-фрагмент может иметь внешние GUID-ссылки и нужен только для изучения;
- build-fragment является частью единого проекта и собирается строго по `manifest.json`.

## Текущая гранулярность

Проект разделён на:

1. `project_prefix.xml`;
2. `views/00_use_case_view.xml`;
3. `views/10_logical_view.xml`;
4. `views/20_component_view.xml`;
5. `views/30_deployment_view.xml`;
6. `project_suffix.xml`.

Это повторяет четыре корневых View из `lending.uml` и уже позволяет не работать с одним монолитом.

## Следующая ступень

После стабилизации registry и dependency resolver можно делить `Use Case View` на:

- общие semantic objects;
- relations;
- diagram/view fragments.

При этом сборщик должен автоматически контролировать GUID и collection counters. До этого ручное мелкое дробление запрещено рабочим соглашением.
