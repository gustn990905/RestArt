import os
import pymysql

def connect_db(config):
    """?곗씠?곕쿋?댁뒪 ?곌껐 ?ㅼ젙"""
    connection = pymysql.connect(host=config['host'],
                                 user=config['user'],
                                 password=config['password'],
                                 database=config['database'],
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

def insert_exhibitions(connection, exhibitions):
    """?꾩떆???뺣낫瑜??곗씠?곕쿋?댁뒪???쎌엯"""
    with connection.cursor() as cursor:
        sql = """
        INSERT INTO exhibitions (name, latitude, longitude, start_date, end_date, description)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        for exhibition in exhibitions:
            name = exhibition[1]
            start_date, end_date = exhibition[2]
            latitude, longitude = exhibition[3]
            description = exhibition[4]
            cursor.execute(sql, (name, latitude, longitude, start_date, end_date, description))
        connection.commit()

# ?곗씠?곕쿋?댁뒪 ?곌껐 ?ㅼ젙
db_config = {
    "host": os.getenv("RESTART_DB_HOST", "localhost"),
    "user": os.getenv("RESTART_DB_USER", "restart_user"),
    "password": os.getenv("RESTART_DB_PASSWORD", ""),
    "database": os.getenv("RESTART_DB_NAME", "restart"),
}

# ?곗씠?곕쿋?댁뒪 ?곌껐
db_connection = connect_db(db_config)

# ?꾩떆???뺣낫
exhibitions = [
    ["https://ifh.cc/g/KtVo8L.jpg", "?꾨Ⅴ??, ["2024-04-01", "2024-08-12"], [37.5119564733933, 127.088282780728], "?딆엫?놁씠 ?덈꼍???ν빐 臾쇰낫?쇰? ?쇱쑝?ㅻ뒗 ?뚮룄, 嫄곗꽱 諛붾엺?????놁씠 遺덉뼱?ㅻ뒗 洹??몃뜒???앹뿉 洹몃?媛 ???덈떎. Never Silence, ???쒕쾲??怨좎슂?????놁뿀??洹몃????띠뿉 ????댁빞湲곌? ?쒖옉?쒕떎."],
    ["https://ifh.cc/g/V7NpL0.jpg", "??뭾???몃뜒?먯꽌", ["2024-04-01", "2024-08-12"], [37.5173319258532, 127.047377408384], "媛뺣쫱? 諛몃━(VALLEY)?쇰뒗 ?뚮쭏濡?諛깅몢?媛꾩쓽 以묒텛??媛뺤썝?꾩? 媛뺣쫱??吏??쟻 ?뱀꽦??諛섏쁺??12媛쒖쓽 ?ㅻ옒珥먯슫 誘몃뵒?댁븘???꾩떆媛 1,500?됱쓽 怨듦컙?먯꽌 ?쒓컖??媛뺣젹?④낵 ?붾텋??媛먭컖?곸씤 ?ъ슫?? ?덇꺽?덈뒗 ?κ린? ?④퍡 紐곗엯 寃쏀뿕???쒓났"]
]

# ?꾩떆???뺣낫 ?쎌엯
insert_exhibitions(db_connection, exhibitions)
