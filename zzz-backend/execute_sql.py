import psycopg2
import config_reader

config = config_reader.reader()

def connect_to_postgres(config):
    conn = psycopg2.connect(
        dbname='postgres',
        user=config['database']['user'],
        password=config['database']['password'],
        host=config['database']['host'],
        port=config['database']['port']
    )
    conn.autocommit = True
    return conn

        
#和数据库进行连接
def connect_to_db(dbname,config):
    conn = psycopg2.connect(
        dbname=dbname,
        user=config['database']['user'],
        password=config['database']['password'],
        host=config['database']['host'],
        port=config['database']['port']
    )
    return conn
    

def execute_sql_file(conn, sql_file):
    with open(sql_file, 'r') as file:
        sql = file.read()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
  
conn_w_engines = connect_to_db('W_Engines', config)
execute_sql_file(conn_w_engines, 'W_Engines.sql')
conn_w_engines.close()

#获取函数    
def get_attack_base_value(config, level):
    conn = connect_to_db('ZZZlevelBaseoftheAttacker', config)
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM attack_level WHERE level = %s;", (level,))
    value = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return value

print(get_attack_base_value(config, 5))

def get_WEngine_value(config, WEngineName):
    conn = connect_to_db('W_Engines', config)
    cursor = conn.cursor()
    cursor.execute("SELECT ATTACK, CRIT_RATE, CRIT_DMG, ATTACK_PERCENT, Impact, AttributeDamageBonus, DamageBonus FROM WEngine_status WHERE WEngineName = %s;", (WEngineName,))
    record = cursor.fetchone()
    cursor.close()
    conn.close()
    if record:
        ATTACK, CRIT_RATE, CRIT_DMG, ATTACK_PERCENT, Impact, AttributeDamageBonus, DamageBonus = record
        return ATTACK, CRIT_RATE, CRIT_DMG, ATTACK_PERCENT, Impact, AttributeDamageBonus, DamageBonus
    else:
        return None

print(get_WEngine_value(config, 'SteelCushion'))



# def execute_sql_file(sql_file, conn):
#     with open(sql_file, 'r') as file:
#         sql = file.read()
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     conn.commit()
#     cursor.close()

# def main():
#     # 连接PostgreSQL服务器
#     config = config_reader.reader()

#     # 连接数据库
#     conn = connect_to_db(config)

#     # 执行SQL
#     execute_sql_file('ZZZlevelBaseoftheAttacker.sql', conn)
    
#     conn.close()

# if __name__ == "__main__":
#     main()
