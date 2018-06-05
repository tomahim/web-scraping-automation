from flask import Flask, jsonify

app = Flask(__name__)


class CollectionProperty:
    def __init__(self, properties):
        self.properties = properties

    def serialize(self):
        return self.properties


@app.route('/')
def get_all_data_collection():

    return jsonify([
        elem.serialize() for elem in [CollectionProperty({'id': 'string'})]
    ])


if __name__ == "__main__":
    app.run()