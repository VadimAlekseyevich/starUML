# 5. Модель размещения

## Статус источников

В текущем `методичка.docx` отдельной главы по Deployment Diagram нет.

Этот раздел основан на `lending.uml` [LENDING] и реальном deployment Urban Development Generator [PROJECT].

## Наблюдение по lending

Рабочая Deployment Diagram `Lending` находится в `Logical View / Arch`, тогда как верхний `Deployment View / Main` является базовой заготовкой [LENDING].

## Urban Development

Фактический `docker-compose.yml` задаёт основные deployment units:

- `frontend`;
- `api`;
- `worker`;
- `db` PostgreSQL/PostGIS;
- `redis`;
- одноразовый `migrate` job.

Также API/worker используют примонтированное storage.

Итоговая Deployment Diagram должна трассироваться к Component Model: логический компонент должен быть сопоставим с исполняемым artifact/service/node.
