from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/calc", methods=["GET", "POST"])
def calc():
    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])
        op = request.form["op"]

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b if b != 0 else "0 ga bo‘linmaydi"

        return render_template("result48.html", result=result)

    return render_template("index48.html")

if __name__ == "__main__":
    app.run(debug=True)
