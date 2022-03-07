import time
import pymysql

def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")
def get_conn():
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="wwj520hy",
                           db="covid-19",
                           charset="utf8")
    cursor = conn.cursor()
    return conn, cursor
def close_conn(conn, cursor):
    cursor.close()
    conn.close()

def query(sql,*args):
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res
# 主页头部数据展示
def get_home_data():
    sql = "select SUM(confirm),(SELECT SUM(suspect) FROM history ORDER BY ds DESC LIMIT 1),SUM(heal),SUM(dead) FROM details WHERE update_time=(SELECT update_time FROM details ORDER BY update_time DESC LIMIT 1)"
    res = query(sql)
    return res[0]
# 主页地图数据
def get_home_map():
    sql="select province,SUM(confirm_add),confirm from details WHERE update_time=(SELECT update_time FROM details ORDER BY update_time DESC LIMIT 1) GROUP BY province"
    res = query(sql)
    return res
# 数据图表-统计数据 数据集
def get_alldetails_data():
    sql="SELECT update_time,province,city,confirm,confirm_add,confirm_now,heal,dead FROM details WHERE update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1)"
    res=query(sql)
    return res
#  数据图表-累计图表 table-1
def get_allconfirmed_data():
    sql = "select ds,confirm,suspect,heal,dead from history"
    res = query(sql)
    return res
# 数据图表-累计图表 table-2
def get_maxConfirmed_data():
    sql = "SELECT update_time,province,confirm FROM details WHERE province IN ('香港','湖北','台湾','上海','陕西') GROUP BY update_time,province"
    res = query(sql)
    return res
def get_ProvinceConfirmed1_data():
    sql = "SELECT confirm FROM details WHERE province IN ('上海') GROUP BY update_time,province"
    res=query(sql)
    return res
def get_ProvinceConfirmed2_data():
    sql = "SELECT confirm FROM details WHERE province IN ('湖北') GROUP BY update_time,province"
    res=query(sql)
    return res
def get_ProvinceConfirmed3_data():
    sql = "SELECT confirm FROM details WHERE province IN ('陕西') GROUP BY update_time,province"
    res=query(sql)
    return res
def get_ProvinceConfirmed4_data():
    sql = "SELECT confirm FROM details WHERE province IN ('香港') GROUP BY update_time,province"
    res=query(sql)
    return res
def get_ProvinceConfirmed5_data():
    sql = "SELECT confirm FROM details WHERE province IN ('台湾') GROUP BY update_time,province"
    res=query(sql)
    return res
# 数据图表-新增图表 table-1
def get_AllAddConfirmed_data():
    sql = "select ds,confirm_add,confirm_now,suspect_add,heal_add,dead_add from history"
    res = query(sql)
    return res

def get_r2_data():
    sql = "select content from hotsearch ORDER BY id DESC LIMIT 30"
    res = query(sql)
    return res

def get_anhui_data():
    sql="SELECT city,confirm FROM details where province='安徽' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_aomen_data():
    sql="SELECT city,confirm FROM details where province='澳门' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_beijing_data():
    sql="SELECT city,confirm FROM details where province='北京' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_chongqing_data():
    sql="SELECT city,confirm FROM details where province='重庆' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_fujian_data():
    sql="SELECT city,confirm FROM details where province='福建' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_gansu_data():
    sql="SELECT city,confirm FROM details where province='甘肃' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_guangdong_data():
    sql="SELECT city,confirm FROM details where province='广东' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_guangxi_data():
    sql="SELECT city,confirm FROM details where province='广西' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_guizhou_data():
    sql="SELECT city,confirm FROM details where province='贵州' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_hainan_data():
    sql="SELECT city,confirm FROM details where province='海南' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_hebei_data():
    sql="SELECT city,confirm FROM details where province='河北' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_heilongjiang_data():
    sql="SELECT city,confirm FROM details where province='黑龙江' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_henan_data():
    sql="SELECT city,confirm FROM details where province='河南' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_hubei_data():
    sql="SELECT city,confirm FROM details where province='湖北' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_hunan_data():
    sql="SELECT city,confirm FROM details where province='湖南' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_jiangsu_data():
    sql="SELECT city,confirm FROM details where province='江苏' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_provinces_data():
    sql="SELECT province,city,confirm FROM details where province='澳门' AND  update_time=(SELECT update_time FROM details ORDER BY update_time DESC	LIMIT 1) AND city!='境外输入'"
    res = query(sql)
    return res
def get_allprovince():
    

if __name__ == "__main__":
    print(get_anhui_data())
