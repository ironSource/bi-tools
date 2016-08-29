# Turn Rows Into Columns (postgress)
This script gets a table and a column name as input, and transforms the column's content (rows) into columns.
For example:

| Beer Name  |  Beer Rank |
|---|---|
| Guiness  | 9 |
| Goldstar | 9 |
| Guiness  | 8 |
| Maccabi  | 10 |

| Guiness  |  Goldstar | Maccabi
|---|---|---|
| 2 | 1 | 1

**How To Run**
```
python rows_to_columns.py {user} '{password}' {host} {schema.tablename} {column_to_transform}
```
