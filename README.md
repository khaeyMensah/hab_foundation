# HAB Beacon of Hope Foundation

## Local development

Use:

```bash
python manage.py tailwind start
```

This now:

- starts Tailwind in watch mode
- runs `python manage.py migrate`
- runs `python manage.py sync_programs`
- starts the Django development server

## Render build command

Use this build command on Render:

```bash
pip install -r requirements.txt && npm install --prefix theme/static_src && npm run build --prefix theme/static_src && python manage.py migrate && python manage.py sync_programs && python manage.py collectstatic --noinput
```

If you ever want production to match the code-managed program catalog exactly and remove any extra database records not in the catalog, replace:

```bash
python manage.py sync_programs
```

with:

```bash
python manage.py sync_programs --prune
```
