from flask import Flask, url_for, render_template, request
from conndb import init_from_db,get_date,get_word


app = Flask(__name__)


@app.route('/wiki2008/')
def hello_world():
    x = render_template('charts.html') # type:str
    return x


@app.route('/getdata/', methods=['POST'])
def get_data():
    if request.form['type'] == 'date':

        print('posted:'+request.form['data'])
        data = get_date(request.form['data'])
        return data
    elif request.form['type'] == 'word':

        print('posted:' + request.form['data'])
        data = get_word(request.form['data'])
        return data

@app.route('/init/',methods=['POST'])
def init_data():
    print(request.args.to_dict())
    if request.form['type'] == 'date':
        # get top10 access data of the date
        # [[keywd,accesstimes]*10]
        # transfer to json
        data = init_from_db('date')
        return data
    elif request.form['type'] == 'keywd':
        # get overall access data of this keywd
        # [[date,accesstimes]*366]
        # transfer to json
        data = init_from_db('keywd')
        return data
    return "hello"
if __name__ == '__main__':
    app.run()
