from PySide6 import QtWidgets, QtGui
import sys
import mysql.connector
	

class MainForm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        # connecting to the database
        self.dataBase = mysql.connector.connect(
					host = "localhost",
					user = "root",
					passwd = "root",
					database = " parkin",
					 port=8889 )
	
        self.resize(300,100)
        self.setWindowTitle("BTS SNIR2 - QDialog")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
       
        # self.main_widget()

    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        self.layoutFormulaire = QtWidgets.QFormLayout()

        self.lbl_login = QtWidgets.QLabel("Login")
        self.LEdit_login = QtWidgets.QLineEdit("korri")
        self.LEdit_login.setPlaceholderText("Saisir votre login")

        self.lbl_pw = QtWidgets.QLabel("Password")
        self.LEdit_pw = QtWidgets.QLineEdit("word")
        self.LEdit_pw.setPlaceholderText("Saisir votre mot de passe")

        self.btn_connect = QtWidgets.QPushButton("Connect")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")

    def addWigets_to_layouts(self):
        self.layoutFormulaire.addRow("Login   ",self.LEdit_login)
        self.layoutFormulaire.addRow("Password",self.LEdit_pw)
        self.layoutFormulaire.addRow(self.btn_connect, self.btn_Quitter)
    

        # self.layoutH1.addWidget(self.lbl_login)
        # self.layoutH1.addWidget(self.LEdit_login)

        # self.layoutH2.addWidget(self.lbl_pw)
        # self.layoutH2.addWidget(self.LEdit_pw)

        # self.layoutH3.addWidget(self.btn_connect)
        # self.layoutH3.addWidget(self.btn_Quitter)
        # self.layoutV.addLayout(self.layoutH1)
        # self.layoutV.addLayout(self.layoutH2)
        # self.layoutV.addLayout(self.layoutH3)
        # self.layoutV.addLayout(self.layoutH4)
        # self.setLayout(self.layoutV)
        self.setLayout(self.layoutFormulaire)

    # def main_widget(self):
    #     self.widget = QtWidgets.QWidget(self)  
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)
       
    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        self.btn_connect.clicked.connect(self.verificate)
         
    def clear_Ledit(self):
        self.LEdit_login.setText("")
        self.LEdit_pw.setText("")
    
    def goToSecond(self):
        print("Je change de fenetre")
        # form2.show()
        # form.hide()
    
        # pass
        login = self.LEdit_login.text()  # Get the login from the QLineEdit
        form2.showWithLogin(login)
        form.hide()

        

    def verificate(self):
        login_s = self.LEdit_login.text()
        password_s = self.LEdit_pw.text()

        # Preparing a cursor object
        cursorObject = self.dataBase.cursor()

        # Selecting query
        query = f"SELECT login, mot_de_pass FROM users WHERE login = '{login_s}' AND mot_de_pass ='{password_s}'"
        print(query)
        cursorObject.execute(query)

        # query = "SELECT login, mot_de_pass FROM users WHERE login = %s AND mot_de_pass = %s"
        # cursorObject.execute(query, (login, password))

        

        # Fetch the result
        result = cursorObject.fetchone()

        # Close the cursor
        cursorObject.close()

        if result:
            # Credentials are correct
            self.goToSecond()
        else:
            # Credentials are incorrect
            message = QtWidgets.QMessageBox()
            message.setIcon(QtWidgets.QMessageBox.Warning)
            message.setText("Erreur d'authentification\nVeuillez saisir des valeurs correctes.")
            message.setWindowTitle("Erreur")
            message.exec_()

            # Clear the QLineEdit fields
            self.clear_Ledit()

                
        # disconnecting from server
       


class SecondForm(QtWidgets.QDialog):
    def showWithLogin(self, login):
        self.lbl_login.setText(f"Bonjour {login}")  # Set the login in the QLabel
        self.show()
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle("BTS SNIR2 - QDialog")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        # self.main_widget()

    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        

        self.lbl_login = QtWidgets.QLabel("Login")
       
        self.lbl_image = QtWidgets.QLabel("Ici une iamge")

        self.carImage = QtGui.QPixmap("Oxygen.icns")


        # Créer deux boutons (Ajouter et Supprimer) sur la même ligne

        self.lbl_image.setPixmap(self.carImage)
       

        self.btn_connect = QtWidgets.QPushButton("Disconnect")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")

    def addWigets_to_layouts(self):

        self.layoutH1.addWidget(self.lbl_login)
       

        self.layoutH2.addWidget(self.lbl_image)
   

        self.layoutH3.addWidget(self.btn_connect)
        self.layoutH3.addWidget(self.btn_Quitter)
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.setLayout(self.layoutV)

    # def main_widget(self):
    #     self.widget = QtWidgets.QWidget(self)  
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)
       
    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        self.btn_connect.clicked.connect(self.goToFirst)
         
    
    
    def goToFirst(self):
        print("Je retourne vers la principale")
        
        form.show()
        form2.hide()
        pass

    

  

    
if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    # Create and show the form
    form = MainForm()
    form2 = SecondForm()
    form.show()
    form2.hide()
    # Run the main Qt loop
    sys.exit(app.exec())
    # app.exec()