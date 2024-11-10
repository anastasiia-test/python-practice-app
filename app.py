from flask import Flask


def create_app():
    app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 12.33
            }
        ]

    }
]

@app.get("/store")
def get_stores():
    return {"stores": stores}