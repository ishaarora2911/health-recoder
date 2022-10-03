from flask import *
from project_2 import *

app = Flask("disease",template_folder="web")
db = firestore.client()

patients=Patient()

@app.route("/")
def index():

    return render_template("index1.html")

@app.route("/enterdata")
def add_health_log():
    return render_template("add_data.html")
@app.route("/show")
def view():
    rows=[]
    documents = db.collection('patient').get()

# @app.route("/show")
# def view():
#     rows=[]
#     lines = []
#     documents=db.collection('patient').get()
#
#     for document in documents:
#         print(document.id)
#         print(document.to_dict())
#         print(type(document))
#         doc = document.to_dict()
#         doc['id'] = document.id
#         rows.append(doc)
#
#         line = "{id},{name},{phone_no}\n".format_map(doc)
#         lines.append(line)
#
#     file = open('data.csv', 'a')
#     for line in lines:
#         file.write(line)
#     return render_template("showdata.html", result=rows)

@app.route("/delete/<id>")
def delete_customer_from_db(name):
    db.collection('restaurants').document(name).delete()
    # print("Document Deleted...")

    return render_template("success.html", message="Customer with ID " + id + " Deleted Successfully..")


@app.route("/savedata", methods=["POST"])
def save_data_in_db():
    print("save health executed")
    patients=Patient(name=request.form["name"],
                    phone_no=request.form["txtPhone"],
                    e_mail=request.form["mail"],
                     date_of_birth=request.form["dob"],
                     gender=request.form["gender"],
                     country=request.form["country"],
                     state=request.form["state"],
                     diseases=request.form["disease"],

                     symptoms=request.form["symptoms"])

    if len(patients.name) == 0:
        return render_template("error.html", message="Name cannot be Empty...")

    print(vars(patients))
    document=(vars(patients))
    db.collection('patient').add(document)
    print("Data Saved:)")

    return render_template("successs.html", message=patients.name + " Inserted Successfully...")

@app.route("/update-data")
def update_customer():
    return render_template("update_info.html")

def main():
    app.run()

if __name__ == "__main__":
    main()
