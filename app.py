from flask import Flask, render_template
app = Flask(__name__)

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

productList = []
productList.append(Item("Sohva", 50))
productList.append(Item("Vanha PC", 75))
productList.append(Item("Auto", 700))

@app.route("/")
def index():
    return render_template("index.html", productList = productList)

if __name__ == "__main__":
    app.run()
