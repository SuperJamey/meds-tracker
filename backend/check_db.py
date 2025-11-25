from sqlmodel import create_engine, inspect

sqlite_file_name = "meds.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

insp = inspect(engine)
print("Tables:", insp.get_table_names())
for table in insp.get_table_names():
    print(f"Schema for {table}:")
    for column in insp.get_columns(table):
        print(f"  {column['name']} ({column['type']})")
