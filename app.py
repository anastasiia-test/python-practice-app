from flask import Flask


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

app = Flask(__name__)

#def create_app():
#    app = Flask(__name__)

@app.get("/store")
def get_stores():
    return {"stores": stores}