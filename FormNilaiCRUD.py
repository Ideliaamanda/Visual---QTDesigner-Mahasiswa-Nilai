# IDENTITAS DIRI
# -------------------------------------------------
# NAMA : Idelia Amanda Putri
# NPM : 2310010271
# KELAS : 4M REGULER PAGI
# -------------------------------------------------

import sys
import mysql.connector as mc
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi

class HalloPython(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('FormNilai.ui',self)
        self.setWindowTitle('PYTHON GUI TABLEWIDGET')
        self.sqlLoad()
        self.pushButton_3.clicked.connect(self.hapus)         
        self.pushButton_5.clicked.connect(self.sqlLoad)  
        self.pushButton.clicked.connect(self.insertkategori)  
        self.pushButton_2.clicked.connect(self.updatekategori)  
        self.pushButton_3.clicked.connect(self.deleteKategori)  
        self.pushButton_4.clicked.connect(self.batal)  
        self.tableWidget.cellClicked.connect(self.isiFormDariTabel)

    def hapus(self):
        self.tableWidget.clear()
        self.label.setText("Data dihapus")

    def sqlLoad(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_mahasiswa"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM nilai Order By field_id ASC")
            result = mycursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.label.setText("Data berhasil ditampilkan")
        except mc.Error as err:
            self.label.setText("Gagal tampilkan data")

    def insertkategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_mahasiswa"
            )
            cursor = mydb.cursor()
            field_id = self.lineEdit.text()
            id_mahasiswa = self.lineEdit_2.text()
            nilai_harian = self.lineEdit_3.text()
            nilai_tgs = self.lineEdit_4.text()
            nilai_uts = self.lineEdit_6.text()
            nilai_uas = self.lineEdit_7.text()

            sql = "INSERT INTO nilai (field_id, id_mahasiswa, nilai_harian, nilai_tgs, nilai_uts, nilai_uas) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (field_id, id_mahasiswa, nilai_harian, nilai_tgs, nilai_uts, nilai_uas)
            cursor.execute(sql, val)
            mydb.commit()

            self.label.setText("Data berhasil disimpan")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
            self.sqlLoad()
        except mc.Error as err:
            self.label.setText("Gagal tampilkan data")
    
    def updatekategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_mahasiswa"
            )
            cursor = mydb.cursor()
            field_id = self.lineEdit.text()
            id_mahasiswa = self.lineEdit_2.text()
            nilai_harian = self.lineEdit_3.text()
            nilai_tgs = self.lineEdit_4.text()
            nilai_uts = self.lineEdit_6.text()
            nilai_uas = self.lineEdit_7.text()
         
            sql = "UPDATE nilai SET id_mahasiswa = %s, nilai_harian = %s, nilai_tgs = %s, nilai_uts = %s, nilai_uas = %s WHERE field_id = %s"
            val = (id_mahasiswa, nilai_harian, nilai_tgs, nilai_uts, nilai_uas, field_id)
            cursor.execute(sql, val)
            mydb.commit()

            self.label.setText("Data berhasil di Update")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
            self.sqlLoad()
        except mc.Error as err:
            self.label.setText("Gagal update data")

    def deleteKategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_mahasiswa"
            )
            mycursor = mydb.cursor()
            field_id = self.lineEdit.text()
            id_mahasiswa = self.lineEdit_2.text()
            nilai_harian = self.lineEdit_3.text()
            nilai_tgs = self.lineEdit_4.text()
            nilai_uts = self.lineEdit_6.text()
            nilai_uas = self.lineEdit_7.text()

            sql = "DELETE FROM nilai WHERE field_id = %s"
            adr = (field_id,)
            mycursor.execute(sql, adr)
            mydb.commit()

            self.label.setText("Data berhasil di Delete")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
            self.sqlLoad()
        except mc.Error as err:
            self.label.setText("Gagal Delete Data")

    def isiFormDariTabel(self, row, column):
        self.lineEdit.setText(self.tableWidget.item(row, 0).text())
        self.lineEdit_2.setText(self.tableWidget.item(row, 1).text())
        self.lineEdit_3.setText(self.tableWidget.item(row, 2).text())
        self.lineEdit_4.setText(self.tableWidget.item(row, 3).text())
        self.lineEdit_6.setText(self.tableWidget.item(row, 4).text())
        self.lineEdit_7.setText(self.tableWidget.item(row, 5).text())

    def batal(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.label.setText("Form dibersihkan")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = HalloPython()
    form.show()
    sys.exit(app.exec_())