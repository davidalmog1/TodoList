# TodoList

[Setup]

pip install -r requierments.txt

alembic init alembic

alembic revision --autogenerate  -m "First revision"

alembic upgrade head/revision

