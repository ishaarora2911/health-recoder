import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore # DataBase


cred = credentials.Certificate("service-account.json")
firebase_admin.initialize_app(cred)
print("Firebase Initialized :)")

db = firestore.client()# got the access of cloud database


class Patient:

    def __init__(self,id=id, name=None, phone_no=None, e_mail=None, date_of_birth=None, gender=None,
                 country=None, state=None,diseases=None, symptoms=None):
        self.id = id
        self.name = name
        self.phone_no = phone_no
        self.e_mail = e_mail
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.country = country
        self.state = state
        self.diseases=diseases
        self.symptoms = symptoms

    def delete(self):

        db.collection('patient').document('id').delete()
        print("Document Deleted...")

patients=Patient()

patients.delete()
document = vars(patients)