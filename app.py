from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/wiki2008/')
def hello_world():
    x = render_template('main.html') # type:str
    return x


@app.route('/getdata/', methods=['POST'])
def get_data():
    if request.form['type'] == 'date':
        # get top10 access data of the date
        # [[keywd,accesstimes]*10]
        # transfer to json
        print('posted'+request.form['data'])
        json = render_template('heatmap.html')
        return json
    elif request.form['type'] == 'date2':
        # get overall access data of this keywd
        # [[date,accesstimes]*366]
        # transfer to json
        print('posted2'+request.form['data'])
        json = render_template('heatmap2.html')
        return json


# url_for('static', filename='style.css')

if __name__ == '__main__':
    app.run()
