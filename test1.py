from app.datasets import get_all_datasets_metadata
from app.db import conn

print(get_all_datasets_metadata(conn))