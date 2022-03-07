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

# 各省份数据
@app.route("/anhui")
def get_anhui_data():
    res = []
    for tup in utils.get_anhui_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})

@app.route("/aomen")
def get_aomen_data():
    res = []
    for tup in utils.get_aomen_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})

@app.route("/beijing")
def get_beijing_data():
    res = []
    for tup in utils.get_beijing_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})

@app.route("/chongqing")
def get_chongqing_data():
    res = []
    for tup in utils.get_chongqing_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})

@app.route("/fujian")
def get_fujian_data():
    res = []
    for tup in utils.get_fujian_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})

@app.route("/gansu")
def get_gansu_data():
    res = []
    for tup in utils.get_gansu_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/guangdong")
def get_guangdong_data():
    res = []
    for tup in utils.get_guangdong_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/guangxi")
def get_guangxi_data():
    res = []
    for tup in utils.get_guangxi_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/guizhou")
def get_guizhou_data():
    res = []
    for tup in utils.get_guizhou_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/hainan")
def get_hainan_data():
    res = []
    for tup in utils.get_hainan_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/hebei")
def get_hebei_data():
    res = []
    for tup in utils.get_hebei_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/heilongjiang")
def get_heilongjiang_data():
    res = []
    for tup in utils.get_heilongjiang_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/henan")
def get_henan_data():
    res = []
    for tup in utils.get_henan_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/hubei")
def get_hubei_data():
    res = []
    for tup in utils.get_hubei_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/hunan")
def get_hunan_data():
    res = []
    for tup in utils.get_hunan_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/jiangsu")
def get_jiangsu_data():
    res = []
    for tup in utils.get_jiangsu_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/jiangxi")
def get_jiangxi_data():
    res = []
    for tup in utils.get_jiangxi_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/jilin")
def get_jilin_data():
    res = []
    for tup in utils.get_jilin_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/liaoning")
def get_liaoning_data():
    res = []
    for tup in utils.get_liaoning_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/neimenggu")
def get_neimenggu_data():
    res = []
    for tup in utils.get_neimenggu_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/ningxia")
def get_ningxia_data():
    res = []
    for tup in utils.get_ningxia_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/qinghai")
def get_qinghai_data():
    res = []
    for tup in utils.get_qinghai_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/shandong")
def get_shandong_data():
    res = []
    for tup in utils.get_shandong_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/shanghai")
def get_shanghai_data():
    res = []
    for tup in utils.get_shanghai_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/shanxi")
def get_shanxi_data():
    res = []
    for tup in utils.get_shanxi_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/shanxizizhiqu")
def get_shanxi1_data():
    res = []
    for tup in utils.get_shanxi1_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/sichuan")
def get_sichuan_data():
    res = []
    for tup in utils.get_sichuan_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/taiwan")
def get_taiwan_data():
    res = []
    for tup in utils.get_taiwan_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/tianjin")
def get_tianjin_data():
    res = []
    for tup in utils.get_tianjin_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/xianggang")
def get_xianggang_data():
    res = []
    for tup in utils.get_xianggang_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/xinjiang")
def get_xinjiang_data():
    res = []
    for tup in utils.get_xinjiang_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/xizang")
def get_xizang_data():
    res = []
    for tup in utils.get_xizang_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/yunnan")
def get_yunnan_data():
    res = []
    for tup in utils.get_yunnan_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})
@app.route("/zhejiang")
def get_zhejiang_data():
    res = []
    for tup in utils.get_zhejiang_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})



if __name__ == '__main__':
    app.run()

