import pymysql
import config

def get_all():
    
	connector = pymysql.connect(
		host = config.host,
		user = config.user,
		passwd = config.passwd,
		db = config.db,
		charset = config.charset,
		cursorclass = pymysql.cursors.DictCursor
	)

	with connector.cursor() as cursor:
		sql = 'select * from users;'
		cursor.execute(sql)
		sql_result = cursor.fetchall()

		json_response = {"all_user" : sql_result}
		return json_response

def get_id_user(id):

	connector = pymysql.connect(
		host = config.host,
		user = config.user,
		passwd = config.passwd,
		db = config.db,
		charset = config.charset,
		cursorclass = pymysql.cursors.DictCursor
	)

	with connector.cursor() as cursor:
		sql = 'select id, name, bikou from userinfo where id = "%s";'% (id)
		cursor.execute(sql)
		sql_result = cursor.fetchall()

		json_response = { "id_user" : sql_result }					
		return json_response

def get_id_user_pass(id):

	connector = pymysql.connect(
		host = config.host,
		user = config.user,
		passwd = config.passwd,
		db = config.db,
		charset = config.charset,
		cursorclass = pymysql.cursors.DictCursor
	)

	with connector.cursor() as cursor:
		sql = 'select pass from userinfo where id = "%s";'% (id)
		cursor.execute(sql)
		sql_result = cursor.fetchall()

		json_response = { "user_pass" : sql_result }				
		return json_response