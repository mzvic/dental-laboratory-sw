# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql
con = sql.connect("designer/db/sql.db")
cur = con.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("LogoDefault.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 521, 391))
        self.tableView.setObjectName("tableView")
        self.tableView.setColumnCount(6)
        cur.execute("SELECT COUNT(*) FROM all_works")
        number_str = str(cur.fetchall())
        number = int(number_str.strip(" ()[],' "))
        self.tableView.setRowCount(number) #CURRENT PROBLEM HERE
        self.tableView.setHorizontalHeaderLabels(['Client', 'Job', 'Status', 'Date Reception', 'Deadline', 'Additional Comments'])
        for j in range(6):
            for i in range(number):
                self.tableView.setItem(i, j, QtWidgets.QTableWidgetItem("PLEASE"))

        #################### DELETE SELECTED #####################
        self.delete_job = QtWidgets.QPushButton(self.centralwidget)
        self.delete_job.setGeometry(QtCore.QRect(10, 490, 191, 41))
        self.delete_job.setText("Delete selected job")
        self.delete_job.setObjectName("delete_job")

        #################### MARK AS DONE #######################
        self.mark_done = QtWidgets.QPushButton(self.centralwidget)
        self.mark_done.setGeometry(QtCore.QRect(150, 410, 231, 61))
        self.mark_done.setText("Mark as done")
        self.mark_done.setObjectName("mark_done")

        ################### JOBS CLIENT #############################
        self.jobs_of_client = QtWidgets.QPushButton(self.centralwidget)
        self.jobs_of_client.setGeometry(QtCore.QRect(330, 540, 191, 41))
        self.jobs_of_client.setText("Search jobs of client")
        self.jobs_of_client.setObjectName("jobs_of_client")

        ##################### CLIENT COMBOBOX ########################
        self.client_cb = QtWidgets.QComboBox(self.centralwidget)
        self.client_cb.setGeometry(QtCore.QRect(330, 490, 191, 41))
        self.client_cb.setObjectName("client_cb")
        cur.execute("SELECT * FROM clientsdb")
        datos = cur.fetchall()
        for i in datos:
            self.client_cb.addItems(i)

        font = QtGui.QFont()
        font.setPointSize(15)
        self.client_cb.setFont(font)
        self.client_cb.setEditable(True)
        self.client_cb.lineEdit().setAlignment(QtCore.Qt.AlignCenter)

        ################ SEEALL JOBS DONE ###########################
        self.all_jobs_done = QtWidgets.QPushButton(self.centralwidget)
        self.all_jobs_done.setGeometry(QtCore.QRect(10, 540, 191, 41))
        self.all_jobs_done.setText("See all jobs done")
        self.all_jobs_done.setObjectName("all_jobs_done")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
