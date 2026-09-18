# Workshop 4 — ORM

> **Course:** Web Applications — YachayTech  
> **Topic:** Object-Relational Mapping (ORM)

---

## Project Structure

```
workshop-4-ORM/
├── client/                  # Frontend application
├── server/                  # Backend / REST API
├── db/
│   ├── docker-compose.yaml  # MySQL database container
│   └── init.sql             # Runs automatically on first startup (user provisioning)
└── README.md
```

---

## Prerequisites

Before running this project, make sure you have the following installed:

- [Docker](https://www.docker.com/) (v20+)
- [Python](https://www.python.org/) (3.14+)

---

## Setup

### 1. Database — MySQL via Docker

The database runs as a Docker container managed by Docker Compose.

**Start the container:**

```bash
cd db
docker compose up -d
```

**Verify the container is running:**

```bash
docker compose ps
```

You should see the `mysql-ws4` container with status `running`.

**Stop the container:**

```bash
docker compose down
```

> **Note:** Data is persisted in the `mysql-ws4-data` Docker volume, so it survives container restarts.

#### Database users

Two users are available. Use `ormuser` for the application and `root` only for admin tasks.

| User      | Password     | Privileges             | Recommended for  |
|-----------|--------------|------------------------|------------------|
| `root`    | `root`       | Full admin access      | Admin / DBA only |
| `ormuser` | `ormpass123` | `ALL` on `webshop.*`   | Application code |

> `ormuser` is created automatically via [`db/init.sql`](db/init.sql) when the container is first initialized.

#### Connection details

| Parameter | Value        |
|-----------|--------------|
| Host      | `localhost`  |
| Port      | `3306`       |
| User      | `ormuser`    |
| Password  | `ormpass123` |
| Database  | `webshop`    |

#### Troubleshooting

- If the connection is refused right after starting, wait ~15 seconds for MySQL to initialize and try again.
- To inspect container logs: `docker compose logs -f`
- The `init.sql` script **only runs on the first startup** (when the volume is empty). If the container already existed, re-create the volume: `docker compose down -v && docker compose up -d`
