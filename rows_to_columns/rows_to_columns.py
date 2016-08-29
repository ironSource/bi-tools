import psycopg2, sys, re
def rows_to_columns(user, password, host, table, column):
    """
    Prints result of rows content transformation into columns; For each row, the new columns will contain aggregation of sum of apperances of the given row content.
    :param user: db user
    :param password: db password
    :param host: db host
    :param table: table containing the rows to transform
    :param column: column containing the rows to transform
    """
    connStr = "dbname=ic user={0} password={1} host={2} port=5439".format(user, password, host)
    rsConn = psycopg2.connect(connStr)
    cursor = rsConn.cursor()

    select_query = 'SELECT DISTINCT {0} FROM {1}'.format(column, table)
    cursor.execute(select_query)
    result_tuples = cursor.fetchall()

    regex = re.compile('[^a-zA-Z_]')
    #column header shouldn't contain special chars
    columns = [(result[0],regex.sub('', result[0])) for result in result_tuples]

    transform_query = ','.join(["SUM(DECODE ({0}.{1},{2},1,0)) AS {3}".format(table, column, "'{0}'".format(column_tuple[0]), column_tuple[1]) for column_tuple in columns])

    print 'SELECT {0} FROM {1}'.format(transform_query, table)

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    host = sys.argv[3]
    table = sys.argv[4]
    column = sys.argv[5]
    rows_to_columns(user, password, host, table, column)
