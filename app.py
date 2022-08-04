from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('13.125.254.186', 27017, username="test", password="test")
db = client.movie_list

@app.route('/')
def work_list():
    return render_template('work_list.html')

@app.route('/work_list', methods=['GET'])
def get_aerobic():
    aerobic_list = list(db.aerobic.find({},{'_id':False}))
    return jsonify({'aerobic_list': aerobic_list})

if __name__ == '__main__': app.run('0.0.0.0', port=5000, debug=True)