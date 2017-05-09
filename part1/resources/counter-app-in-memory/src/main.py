from flask import Flask
app = Flask(__name__)

count = 0


@app.route("/")
def index():
    global count
    count += 1
    return "You have accessed this website {count} times".format(count=count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
