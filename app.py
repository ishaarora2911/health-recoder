from flask import *
from diseasehelper import *

app = Flask("disease", template_folder="web")
db = firestore.client()
print("run")
patients = Patient()
newdocs = vars(patients)
updated = vars(patients)


@app.route("/")
def index():
    print("running")
    return render_template("index1.html")


@app.route("/enterdata")
def add_health_log():
    return render_template("add_data.html")


@app.route("/show")
def view():
    rows = []
    lines=[]
    documents = db.collection('patient').get()

    for document in documents:
        print(document.id)
        print(document.to_dict())
        doc = document.to_dict()
        doc['id'] = document.id
        print(document.id)
        rows.append(doc)
        line = "{name},{phone_no},{e_mail},{date_of_birth},{gender},{country},{state},{diseases},{symptoms}\n".format_map(doc)

        lines.append(line)

    file = open('datas.csv', 'a')
    for line in lines:
        file.write(line)


    return render_template("showdata.html", result=rows)


@app.route("/delete/<id>")
def delete_record_from_db(id):
    db.collection('patient').document(id).delete()
    print("Document Deleted...")

    return render_template("successs.html", message="Customer Deleted Successfully..")


@app.route("/savedata", methods=["POST"])
def save_data_in_db():
    print("save health executed")
    patients = Patient(
        name=request.form["name"],

        phone_no=request.form["txtPhone"],
        e_mail=request.form["mail"],
        date_of_birth=request.form["dob"],
        gender=request.form["gender"],
        country=request.form["country"],
        state=request.form["state"],
        diseases=request.form["disease"],

        symptoms=request.form["symptoms"])

    if len(patients.name) == 0:
        return render_template("errors.html", message="Name cannot be Empty...")

    print(vars(patients))
    document = (vars(patients))
    db.collection('patient').add(document)
    print("Data Saved:)")

    return render_template("successs.html", message=patients.name + " Inserted Successfully...")


@app.route("/update/<id>")
def update_customer(id):
    documents = db.collection('patient').get()
    for document in documents:
        if ((document.id) == id):
            row = document.to_dict()
            print(row)

    return render_template("editdata.html", row=row, id=id)


@app.route("/updatedata/<id>", methods=["POST"])
def update_data_in_db(id):
    print("save health executed")

    patients = Patient(
        name=request.form["name"],
        phone_no=request.form["txtPhone"],
        e_mail=request.form["mail"],
        date_of_birth=request.form["dob"],
        gender=request.form["gender"],

        country=request.form["country"],
        state=request.form["state"],
        diseases=request.form["disease"],

        symptoms=request.form["symptoms"])

    if len(patients.name) == 0:
        return render_template("errors.html", message="Name cannot be Empty...")

    db.collection('patient').document(id).set(vars(patients))

    return render_template("successs.html", message=patients.name + " Inserted Successfully...")

def main():
    app.run(host='127.0.0.1', port=8082)


if __name__ == "__main__":
    main()
