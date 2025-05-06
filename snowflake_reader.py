import snowflake.connector
import configparser

# Load config
config = configparser.ConfigParser()
config.read('config.ini')

sf_config = config['Snowflake']

# Connect using host
conn = snowflake.connector.connect(
    user=sf_config['user'],
    password=sf_config['password'],
    account=sf_config['account'],
    host=sf_config['host'],
    warehouse=sf_config['warehouse'],
    database=sf_config['database'],
    schema=sf_config['schema'],
    protocol='https',
    ocsp_fail_open=True  # helpful in private network setups
)


try:
    cursor = conn.cursor()
    query = f'''
                SELECT *
                FROM {sf_config['database']}.{sf_config['schema']}.{sf_config['table']}
            '''
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
finally:
    cursor.close()
    conn.close()
