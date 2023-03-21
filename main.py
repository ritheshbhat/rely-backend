import pandas as pd
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class ExcelData(Resource):
    def get(self):
        # Read CSV file into a Pandas dataframe
        data = pd.read_csv('src/rely/dataset.csv')

        # Extract specific columns as a new dataframe
        specific_data = data[['ADDRESS']]

        # Convert specific data to a list of dictionaries
        specific_data_list = specific_data.to_dict(orient='records')

        return jsonify({'response': specific_data_list[0]})

api.add_resource(ExcelData, '/')

if __name__ == '__main__':
    app.run(debug=True)
