import string
from flask import request
from flask import render_template
from jieba.analyse import extract_tags

from flask import Flask
from flask_cors import CORS
from flask import jsonify
import utils

app = Flask(__name__)
CORS(app,supports_credentitals=True)

@app.route("/details")
def get_details():
    return "hello"

# 主页地图
@app.route("/home_map")
def get_home_map():
    res = []
    for tup in utils.get_home_map():
        res.append({"name": tup[0], "value": int(tup[1]),"confirm":int(tup[2])})
    return jsonify({"data": res})

# 主页大屏数据
@app.route("/home_data")
def get_home_data():
    data = utils.get_home_data()
    return jsonify({"confirm": data[0]}, {"suspect": data[1]}, {"heal": data[2]}, {"dead": data[3]})

# 数据图表-累计数据
@app.route("/alldetails")
def get_alldetails_data():
    data = utils.get_alldetails_data()
    day, province,city,confirm, confirm_add,confirm_now, heal, dead = [], [], [], [], [],[], [], []
    res = []
    for tup in data:
        res.append({"day":tup[0].strftime("%m-%d"),"province":tup[1],"city":tup[2],"confirm":tup[3],"confirm_add":tup[4],"confirm_now":tup[5],"heal":tup[6],"dead":tup[7]})
    return jsonify({"data":res})

# 疫情统计数据——累计确证
@app.route("/allconfirmed")
def get_allconfirmed_data():
    res = utils.get_allconfirmed_data()
    day, confirm, suspect, heal, dead = [], [], [], [], []
    for a, b, c, d, e in res:
        day.append(a.strftime("%m-%d"))
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"day": day, "confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead})

# 疫情确诊病例前五省份
@app.route('/maxconfirmed')
def get_maxConfirmed_data():
    res = utils.get_maxConfirmed_data()
    shanghai = utils.get_ProvinceConfirmed1_data()
    hubei = utils.get_ProvinceConfirmed2_data()
    shanxi = utils.get_ProvinceConfirmed3_data()
    xianggang = utils.get_ProvinceConfirmed4_data()
    taiwan = utils.get_ProvinceConfirmed5_data()
    time, name, text, value = [], [], [], []
    for a, b, c in res:
        time.append(a.strftime("%m-%d"))
        text.append(b)
        value.append(c)
    text = list(set(text))
    for index  in range(len(time)):
        if((index +1)%5==0):
            name.append(time[index ])
    return jsonify({"name":name},{"text":text},{"value":value},{"shanghai":shanghai},{"hubei":hubei},{"shanxi":shanxi},{"xianggang":xianggang},{"taiwan":taiwan})

# 新增图表数据
@app.route("/addallconfirmed")
def get_AllAddConfirmed_data():
    res = utils.get_AllAddConfirmed_data()
    day, confirm_add,confirm_now, suspect_add, heal_add, dead_add = [], [], [], [], [], []
    for a, b, c, d, e,f in res:
        day.append(a.strftime("%m-%d"))
        confirm_add.append(b)
        confirm_now.append(c)
        suspect_add.append(d)
        heal_add.append(e)
        dead_add.append(f)
    return jsonify({"day": day, "confirm_add": confirm_add, "confirm_now": confirm_now, "suspect_add": suspect_add, "heal_add": heal_add,"dead_add":dead_add})

# 安徽数据
@app.route("/anhui")
def get_anhui_data():
    res = []
    for tup in utils.get_anhui_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})

if __name__ == '__main__':
    app.run()

