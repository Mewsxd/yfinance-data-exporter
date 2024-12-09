from flask import Flask, request, send_file, jsonify, Response
from flask_cors import CORS

from util.get_indicator_data import get_indicator_data
import io

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "Hello, Flask!"


@app.route('/api/v1/indicator')
def get_data():
    symbol = request.args.get('symbol')
    interval = request.args.get('interval')
    period = request.args.get('period')

    if not symbol or not interval or not period:
        return {"error": "Missing query parameters"}, 400

    indicator_data = get_indicator_data(symbol, interval, period)
    # print(indicator_data)
    if indicator_data is None:
        return jsonify({"error": "Invalid or unsupported symbol"}), 400
    # indicator_data.to_excel(symbol + "_RSI_MACD_ALL_TIME_5.xlsx", sheet_name="RSI_MACD Data")
    csv = indicator_data.to_csv()
    response = Response(csv, mimetype='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    return response
    # csv_io = io.StringIO(csv)

    # return send_file(csv_io, mimetype='text/csv', as_attachment=True, download_name='data.csv')
    # return {"message": "Hello"}, 200


if __name__ == '__main__':
    app.run(debug=True)
