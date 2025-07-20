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
        loadUi('FormMahasiswa.ui',self)
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
            mycursor.execute("SELECT * FROM mhs Order By npm ASC")
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
            npm = self.lineEdit.text()
            nama_lengkap = self.lineEdit_2.text()
            nama_panggilan = self.lineEdit_3.text()
            telepon = self.lineEdit_4.text()
            email = self.lineEdit_5.text()
            kelas = self.lineEdit_6.text()
            mata_kuliah = self.lineEdit_7.text()
            lokasi_kampus = self.lineEdit_8.text()

            sql = "INSERT INTO mhs (npm, nama_lengkap, nama_panggilan, telepon, email, kelas, mata_kuliah, lokasi_kampus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (npm, nama_lengkap, nama_panggilan, telepon, email, kelas, mata_kuliah, lokasi_kampus)
            cursor.execute(sql, val)
            mydb.commit()

            self.label.setText("Data berhasil disimpan")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
            self.lineEdit_8.setText("")
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
            npm = self.lineEdit.text()
            nama_lengkap = self.lineEdit_2.text()
            nama_panggilan = self.lineEdit_3.text()
            telepon = self.lineEdit_4.text()
            email = self.lineEdit_5.text()
            kelas = self.lineEdit_6.text()
            mata_kuliah = self.lineEdit_7.text()
            lokasi_kampus = self.lineEdit_8.text()
         
            sql = "UPDATE mhs SET nama_lengkap = %s, nama_panggilan = %s, telepon = %s, email = %s, kelas = %s, mata_kuliah = %s, lokasi_kampus = %s WHERE npm = %s"
            val = (nama_lengkap, nama_panggilan, telepon, email, kelas, mata_kuliah, lokasi_kampus, npm)
            cursor.execute(sql, val)
            mydb.commit()

            self.label.setText("Data berhasil di Update")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
            self.lineEdit_8.setText("")
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
            npm = self.lineEdit.text()
            nama_lengkap = self.lineEdit_2.text()
            nama_panggilan = self.lineEdit_3.text()
            telepon = self.lineEdit_4.text()
            email = self.lineEdit_5.text()
            kelas = self.lineEdit_6.text()
            mata_kuliah = self.lineEdit_7.text()
            lokasi_kampus = self.lineEdit_8.text()

            sql = "DELETE FROM mhs WHERE npm = %s"
            adr = (npm,)
            mycursor.execute(sql, adr)
            mydb.commit()

            self.label.setText("Data berhasil di Delete")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
            self.lineEdit_8.setText("")
            self.sqlLoad()
        except mc.Error as err:
            self.label.setText("Gagal Delete Data")

    def isiFormDariTabel(self, row, column):
        self.lineEdit.setText(self.tableWidget.item(row, 0).text())
        self.lineEdit_2.setText(self.tableWidget.item(row, 1).text())
        self.lineEdit_3.setText(self.tableWidget.item(row, 2).text())
        self.lineEdit_4.setText(self.tableWidget.item(row, 3).text())
        self.lineEdit_5.setText(self.tableWidget.item(row, 4).text())
        self.lineEdit_6.setText(self.tableWidget.item(row, 5).text())
        self.lineEdit_7.setText(self.tableWidget.item(row, 6).text())
        self.lineEdit_8.setText(self.tableWidget.item(row, 7).text())

    def batal(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.label.setText("Form dibersihkan")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = HalloPython()
    form.show()
    sys.exit(app.exec_())