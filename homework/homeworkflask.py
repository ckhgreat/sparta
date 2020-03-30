from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('homework.html')

@app.route('/dollbuying', methods=['POST'])
def buying_details():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    detail = {
       'name': name_receive,
       'count': count_receive,
       'address': address_receive,
       'phone': phone_receive
    }

    db.dollbuying.insert_one(detail)
    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다!!'})


@app.route('/dollbuying', methods=['GET'])
def read_details():
    dollbuying = list(db.dollbuying.find({},{'_id':0}))
    return jsonify({'result': 'success', 'dollbuying': dollbuying})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)