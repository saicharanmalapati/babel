from flask import Flask, render_template
from babel import numbers, dates
from datetime import datetime, time, date

app = Flask(__name__)


@app.route('/')
def index():
    us_num = numbers.format_decimal(12345, locale='en_US')
    se_num = numbers.format_decimal(12345, locale='sv_SE')
    de_num = numbers.format_decimal(12345, locale='de_DE')

    d = date(2007, 4, 1)

    us_date = dates.format_date(d, locale='en_US')
    de_date = dates.format_date(d, locale='en_DE')

    result = {'us_num': us_num, 'se_num': se_num,
              'de_num': de_num, 'us_date': us_date, 'de_date': de_date}
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
