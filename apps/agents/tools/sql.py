import sqlite3
from langchain_core.tools import Tool

conn = sqlite3.connect("apps/agents/db.sqlite")


def list_tables():
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = c.fetchall()
    return "\n".join(row[0] for row in rows if row[0] is not None)


def run_sqlite_query(query):
    c = conn.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    except sqlite3.OperationalError as err:
        return f"The following error occured: {str(err)}"


def describe_tables(tables_names):
    c = conn.cursor()
    tables = ', '.join("'" + item + "'" for item in tables_names)
    rows = c.execute(
        f"SELECT sql FROM sqlite_master WHERE type='table' and name IN({tables});")
    return "\n".join(row[0] for row in rows if row[0] is not None)


decscribe_tables_tool = Tool.from_function(
    name="describe_tables",
    description="Given a list of table names, return the schema of this table.",
    func=describe_tables
)

run_query_tool = Tool.from_function(
    name="run_sqlite_query",
    description="Run s sqlite query.",
    func=run_sqlite_query
)
