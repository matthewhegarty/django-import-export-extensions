# Development Guide for Claude

## Running Django Migrations

This project uses Docker Compose for PostgreSQL and Redis. To run migrations:

1. **Start the PostgreSQL container:**
   ```bash
   docker compose up -d postgres
   ```

2. **Run migrations with `DB_HOST=localhost`:**
   ```bash
   cd test_project
   DB_HOST=localhost python3 manage.py migrate
   ```

   Or from the project root:
   ```bash
   DB_HOST=localhost python3 test_project/manage.py migrate
   ```

### Why `DB_HOST=localhost`?

The Django settings default to `DB_HOST=postgres` (for Docker container networking), but when running Django commands from the host machine, you need to override it to `localhost` since the PostgreSQL port 5432 is exposed to localhost.

## Project Structure

- `test_project/` - Django test project for development and testing
- `import_export_extensions/` - Main package code
- `docker-compose.yaml` - PostgreSQL and Redis services
- Dependencies managed with Poetry

## Database Configuration

From `test_project/settings.py`:
- Database: PostgreSQL
- Default host: `postgres` (for Docker networking)
- Default user: `django-import-export-extensions-user`
- Default database: `django-import-export-extensions-dev`
- Default password: `testpass`
- Port: 5432

All can be overridden via environment variables (DB_HOST, DB_USER, DB_NAME, DB_PASSWORD, DB_PORT).