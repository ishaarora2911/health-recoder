from flask import *
from diseasehelper import *

app = Flask("disease",template_folder="web")
db = firestore.client()
print("run")
patients=Patient()
newdocs=vars(patients)
updated = vars(patients)
@app.route("/")
def index():
    print("running")
    return render_template("index1.html")

@app.route("/enterdata")
def add_health_log():
    return render_template("add_data.html")
# @app.route("/show")
# def view():
#     rows=[]
#     documents = db.collection('patient').get()

@app.route("/show")
def view():
    rows=[]
    lines = []
    documents=db.collection('patient').get()

    for document in documents:
        print(document.id)
        print(document.to_dict())
        print(type(document))
        doc = document.to_dict()
        doc['id'] = document.id
        print(document.id)
        rows.append(doc)

       # line = "{id},{name},{phone_no}\n".format_map(doc)
    #    lines.append(line)

    # file = open('data.csv', 'a')
    # for line in lines:
    #     file.write(line)
    return render_template("showdata.html", result=rows)

@app.route("/delete/<id>")
def delete_customer_from_db(id):
    #documents = db.collection('patient').get()
    print(id)
    # p1=Patient(id=id)
    # p1.deletes(id)

    db.collection('patient').document(id).delete()
    print("Document Deleted...")

    return render_template("successs.html", message="Customer with ID  Deleted Successfully..")


@app.route("/savedata", methods=["POST"])
def save_data_in_db():
    print("save health executed")
    patients=Patient(
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
    document=(vars(patients))
    db.collection('patient').add(document)
    print("Data Saved:)")

    return render_template("successs.html", message=patients.name + " Inserted Successfully...")

@app.route("/update/<id>")
def update_customer():



    db.collection('patient').document('key').set(newdocs)
    print("Document Updated..")

    return render_template("editdata.html")

def main():
    app.run(host='127.0.0.1', port=8083)

if __name__ == "__main__":
    main()
