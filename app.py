from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)



@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/<string:page>")
def show_page(page):
    return render_template(page)


@app.route("/contact_form", methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        with open("data.txt", mode="a") as contact_database:
            email = request.form.get("email")
            subject = request.form.get("subject")
            msg = request.form.get("msg")

            with open("contacts.csv", mode="a", newline='') as contact_database:
                writer = csv.writer(contact_database)
                writer.writerow([email, subject, msg])

        return redirect("/thankyou.html")
    else:
        return render_template("contact.html")



app.run(debug=True)

