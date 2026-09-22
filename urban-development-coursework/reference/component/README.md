# Component Diagram — старый пример + реальная архитектура

> В методичке отдельной Component-главы нет. Старый lending — reference, не технический шаблон для копирования.

## Старые материалы

- `ClientServer.jpg`;
- `ClientClient.jpg`;
- `ManagerClient.jpg`;
- `ManagerServer.jpg`;
- `Service.jpg`;
- `Executable.jpg`;
- `artifact.jpg`;
- legacy `client_server.fragment.xml`.

То, что старые Component Diagram лежат в Logical View/Component, не обязаны повторять.

## Urban Development

Кандидаты:

- Frontend;
- Backend API;
- Algorithmic Core;
- Worker;
- PostgreSQL/PostGIS;
- Redis;
- storage/artifacts.

Component Diagram отвечает на вопрос о программной структуре и dependencies, а не о физических узлах.
