from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sqlite3
import sys
import os
import time


class Ui_Aegis(QMainWindow):
    def __init__(self):
        super(Ui_Aegis,self).__init__()
        self.setObjectName("Aegis")
        self.setFixedWidth(787)
        self.setFixedHeight(268)
        self.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.detailcover=QtWidgets.QLabel(self.centralwidget)
        self.detailcover.setGeometry(QtCore.QRect(251, 0, 270, 490))
        self.detailcover.setAutoFillBackground(True)
        self.detailcover.setStyleSheet("background:black")
        self.detailcover.setText("")
        self.detailcover.setObjectName("detailcover")
        self.titlein = QtWidgets.QLineEdit(self)
        self.titlein.setGeometry(QtCore.QRect(581, 39, 191, 20))
        self.titlein.setObjectName("titlein")
        self.usernamein = QtWidgets.QLineEdit(self)
        self.usernamein.setGeometry(QtCore.QRect(581, 69, 191, 20))
        self.usernamein.setObjectName("usernamein")
        self.titlel = QtWidgets.QLabel(self)
        self.titlel.setGeometry(QtCore.QRect(521, 40, 131, 20))
        self.titlel.setObjectName("titlel")
        self.usernamel = QtWidgets.QLabel(self)
        self.usernamel.setGeometry(QtCore.QRect(521, 70, 131, 20))
        self.usernamel.setObjectName("usernamel")
        self.passwordl = QtWidgets.QLabel(self)
        self.passwordl.setGeometry(QtCore.QRect(521, 100, 131, 20))
        self.passwordl.setObjectName("passwordl")
        self.passwordin = QtWidgets.QLineEdit(self)
        self.passwordin.setGeometry(QtCore.QRect(581, 99, 191, 20))
        self.passwordin.setObjectName("passwordin")
        self.inputcover=QtWidgets.QLabel(self.centralwidget)
        self.inputcover.setGeometry(QtCore.QRect(521, 0, 260, 490))
        self.inputcover.setAutoFillBackground(True)
        self.inputcover.setStyleSheet("background:black")
        self.inputcover.setText("")
        self.inputcover.setObjectName("inputcover")
        self.message=QtWidgets.QLabel(self)
        self.message.setGeometry(QtCore.QRect(10, 200, 233, 48))
        self.message.setAutoFillBackground(True)
        self.message.setStyleSheet("background:transparent")
        self.message.setObjectName("message")
        self.enterkey = QtWidgets.QPushButton(self.centralwidget)
        self.enterkey.setGeometry(QtCore.QRect(10, 80, 233, 23))
        self.enterkey.setObjectName("enterkey")

        self.createkey = QtWidgets.QPushButton(self.centralwidget)
        self.createkey.setGeometry(QtCore.QRect(10, 110, 233, 23))
        self.createkey.setObjectName("createkey")

        self.encryptkey = QtWidgets.QPushButton(self.centralwidget)
        self.encryptkey.setGeometry(QtCore.QRect(10, 140, 233, 23))
        self.encryptkey.setObjectName("encryptkey")

        self.decryptkey = QtWidgets.QPushButton(self.centralwidget)
        self.decryptkey.setGeometry(QtCore.QRect(10, 170, 233, 23))
        self.decryptkey.setObjectName("decryptkey")
        
        self.infocover = QtWidgets.QLabel(self.centralwidget)
        self.infocover.setGeometry(QtCore.QRect(0, 0, 251, 461))
        self.infocover.setAutoFillBackground(True)
        self.infocover.setStyleSheet("background:transparent")
        self.infocover.setText("")
        self.infocover.setObjectName("infocover")
        self.newconfirm = QtWidgets.QPushButton(self.centralwidget)
        self.newconfirm.setGeometry(QtCore.QRect(521, 126, 251, 23))
        self.newconfirm.setObjectName("newconfirm")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(72, 20, 171, 20))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(72, 50, 171, 20))
        self.password.setObjectName("password")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(260, 20, 251, 21))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 60, 61, 16))
        self.label_2.setObjectName("label_2")
        self.usernameshow = QtWidgets.QLabel(self.centralwidget)
        self.usernameshow.setGeometry(QtCore.QRect(336, 60, 171, 16))
        self.usernameshow.setStyleSheet("background:white")
        self.usernameshow.setObjectName("usernameshow")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 90, 61, 16))
        self.label_4.setObjectName("label_4")
        self.passwordshow = QtWidgets.QLabel(self.centralwidget)
        self.passwordshow.setGeometry(QtCore.QRect(336, 90, 171, 16))
        self.passwordshow.setStyleSheet("background:white")
        self.passwordshow.setObjectName("passwordshow")
        self.newentry = QtWidgets.QPushButton(self.centralwidget)
        self.newentry.setGeometry(QtCore.QRect(260, 110, 251, 23))
        self.newentry.setObjectName("newentry")
        self.deleteentry = QtWidgets.QPushButton(self.centralwidget)
        self.deleteentry.setGeometry(QtCore.QRect(260, 150, 251, 23))
        self.deleteentry.setObjectName("deleteentry")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(260, 190, 251, 23))
        self.logout.setObjectName("logout")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.label_7.setObjectName("label_7")
        self.username.raise_()
        self.password.raise_()
        self.comboBox.raise_()
        self.message.raise_()
        self.label_2.raise_()
        self.usernameshow.raise_()
        self.label_4.raise_()
        self.passwordshow.raise_()
        self.newentry.raise_()
        self.deleteentry.raise_()
        self.logout.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.infocover.lower()
        self.titlein.lower()
        self.passwordin.lower()
        self.usernamein.lower()
        self.inputcover.raise_()
        self.detailcover.raise_()
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.enterkey.clicked.connect(self.passclicked)
        self.comboBox.activated[str].connect(self.onChanged)
        self.newentry.clicked.connect(self.onNew)
        self.newconfirm.clicked.connect(self.conNew)
        self.deleteentry.clicked.connect(self.onDel)
        self.createkey.clicked.connect(self.onCreate)
        self.encryptkey.clicked.connect(self.onEncrypt)
        self.decryptkey.clicked.connect(self.onDecrypt)
        self.logout.clicked.connect(self.onLogout)
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Aegis", "Aegis"))
        self.label_2.setText(_translate("Aegis", "Username"))
        self.usernameshow.setText(_translate("Aegis", " "))
        self.label_4.setText(_translate("Aegis", "Password"))
        self.message.setText(_translate("Aegis", " "))
        self.passwordshow.setText(_translate("Aegis", " "))
        self.newentry.setText(_translate("Aegis", "New Entry"))
        self.enterkey.setText(_translate("Aegis", "Login"))
        self.createkey.setText(_translate("Aegis", "Create"))
        self.encryptkey.setText(_translate("Aegis", "Encrypt the file"))
        self.decryptkey.setText(_translate("Aegis", "Decrypt the file"))
        self.newconfirm.setText(_translate("Aegis", "Enter"))
        self.deleteentry.setText(_translate("Aegis", "Delete Entry"))
        self.label_6.setText(_translate("Aegis", "Username"))
        self.label_7.setText(_translate("Aegis", "Password"))
        self.logout.setText(_translate("Aegis", "Logout"))
        self.titlel.setText(_translate("Aegis", "Title"))
        self.usernamel.setText(_translate("Aegis", "Username"))
        self.passwordl.setText(_translate("Aegis", "Password"))
        
    def passclicked(self):
        global mainfile
        global mainlist
        global mp
        mainlist=[]
        mainfile=self.username.text()
        mp=self.password.text()
        p=passcheck(mainfile,mp)
        print(p)
        print(mainfile)
        if p==50:
            k=KeyGen(mp)
            print(k)
            spdecrypt(k,mainfile+'.db')
            self.comboBox.addItems(sift(mainfile))
            self.detailcover.setStyleSheet("background:transparent")
            self.detailcover.lower()
            self.infocover.setStyleSheet("background:black")
            self.infocover.raise_()
            n=mainfile+'.db'
            c=sqlite3.connect(n)
            comm='SELECT * FROM '+mainfile+';'
            viewer=c.execute(comm)
            for row in viewer:
                mainlist+=[row]
            c.close()
            spencrypt(k,mainfile+'.db')
            self.username.clear()
            self.password.clear()
            self.message.setStyleSheet("background:transparent")
        elif p==100:
            self.message.setText('Incorrect Details')
            self.message.setStyleSheet("background:red")
            
    def onLogout(self):
        mp=''
        mainfile=''
        mainlist=[]
        self.comboBox.clear()
        print(mp,mainfile,mainlist)
        self.usernameshow.setText(' ')
        self.passwordshow.setText(' ')
        self.inputcover.setStyleSheet("background:black")
        self.inputcover.raise_()
        self.titlein.lower()
        self.passwordin.lower()
        self.usernamein.lower()
        self.detailcover.setStyleSheet("background:black")
        self.detailcover.raise_()
        self.infocover.setStyleSheet("background:transparent")
        self.infocover.lower()
        self.message.setText(' ')
        
    def onEncrypt(self):
        file=self.username.text()
        cp=self.password.text()
        k=KeyGen(cp)
        if os.path.exists(file)==True:
            encrypt(k,file)
            self.message.setStyleSheet("background:transparent")
        else:
            self.message.setText('file nonexistent')
            self.message.setStyleSheet("background:red")

    def onDecrypt(self):
        file=self.username.text()
        cp=self.password.text()
        k=KeyGen(cp)
        if os.path.exists(file)==True:
            decrypt(k,file)
            self.message.setStyleSheet("background:transparent")
        else:
            self.message.setText('file nonexistent')
            self.message.setStyleSheet("background:red")
            
    def onCreate(self):
        file=self.username.text()
        cp=self.password.text()
        k=KeyGen(cp)
        if os.path.exists(file+'.db')==True:
            self.message.setText('file exists')
            self.message.setStyleSheet("background:red")
        else:
            create(file)
            addmastertable(file,cp)
            print('increate')
            spencrypt(k,file+'.db')
            self.message.setText('file created')
            self.message.setStyleSheet("background:green")
        
    def onDel(self):
        x=self.comboBox.currentText()
        k=KeyGen(mp)
        spdecrypt(k,mainfile+'.db')
        delete(mainfile,x)
        self.comboBox.clear()
        self.comboBox.addItems(sift(mainfile))
        mainlist=[]
        n=mainfile+'.db'
        c=sqlite3.connect(n)
        comm='SELECT * FROM '+mainfile+';'
        viewer=c.execute(comm)
        for row in viewer:
            mainlist+=[row]
            print(mainlist)
        c.close()
        self.usernameshow.setText(' ')
        self.passwordshow.setText(' ')
        spencrypt(k,mainfile+'.db')
        
    def conNew(self):
        tx=self.titlein.text()
        us=self.usernamein.text()
        ps=self.passwordin.text()
        print(tx,us,ps)
        k=KeyGen(mp)
        spdecrypt(k,mainfile+'.db')
        add(mainfile,tx,us,ps)
        self.comboBox.clear()
        self.comboBox.addItems(sift(mainfile))
        mainlist=[]
        n=mainfile+'.db'
        c=sqlite3.connect(n)
        comm='SELECT * FROM '+mainfile+';'
        viewer=c.execute(comm)
        for row in viewer:
            mainlist+=[row]
            print(mainlist)
        c.close()
        spencrypt(k,mainfile+'.db')
        self.inputcover.setStyleSheet("background:black")
        self.inputcover.raise_()
        self.titlein.lower()
        self.passwordin.lower()
        self.usernamein.lower()
        self.titlein.clear()
        self.passwordin.clear()
        self.usernamein.clear()
        
    def onChanged(self):
        x=self.comboBox.currentText()
        for i in mainlist:
            if i[0]==x:
                self.usernameshow.setText(i[1])
                self.passwordshow.setText(i[2])
                break

    def onNew(self):
        self.inputcover.setStyleSheet("background:transparent")
        self.inputcover.lower()
        self.titlein.raise_()
        self.passwordin.raise_()
        self.usernamein.raise_()

def passcheck(file,password):
    k=KeyGen('123456789')
    spdecrypt(k,'eTable.db')
    n='eTable.db'
    c=sqlite3.connect(n)
    comm='SELECT * FROM eTable;'
    viewer=c.execute(comm)
    p=100
    for row in viewer:
        print(row)
        if (file,password)==row:
            p=50
            print('positive')
            c.close()
            print('here')
            spencrypt(k,'eTable.db')
            return p
            break
    if p==100:
        print('negative')
        print('nice')
        c.close()
        print('here')
        spencrypt(k,'eTable.db')
        return p

def encrypt(key,filename):
    chunksize= 64*1024
    outf='pr'+filename
    filesize=str(os.path.getsize(filename)).zfill(16)
    IV=Random.new().read(16)
    encryptor= AES.new(key,AES.MODE_CBC,IV)
    print('in')
    with open(filename,'rb') as inputfile:
        with open(outf,'wb') as outputfile:
            outputfile.write(filesize.encode('utf-8'))
            outputfile.write(IV)
            print('loopin')
            while True:
                chunk = inputfile.read(chunksize)
                print(chunk)
                if len(chunk)==0:
                    break
                elif len(chunk)%16 !=0:
                    chunk+=b' '*(16-(len(chunk)%16))
                outputfile.write(encryptor.encrypt(chunk))

def decrypt(key,filename):
    chunksize=64*1024
    outf='dec'+filename
    with open(filename,'rb') as infile:
        filesize=int(infile.read(16))
        IV=infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outf,'wb')as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk)==0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)

def spencrypt(key,filename):
    encrypt(key,filename)
    os.remove(filename)
    os.rename('pr'+filename,filename)
    print('encrypted')
    
def spdecrypt(key,filename):
    decrypt(key,filename)
    os.remove(filename)
    os.rename('dec'+filename,filename)
    print('decrypted')
    
def KeyGen(password):
    hasher=SHA256.new(password.encode('utf-8'))
    return hasher.digest()

def create(filename):
    n=filename+'.db'
    c=sqlite3.connect(n)
    c.execute('CREATE TABLE '+filename+' (TITLE TEXT PRIMARY KEY NOT NULL, USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL);')
    print('created')

def add(filename,title,username,password):
    n=filename+'.db'
    c=sqlite3.connect(n)
    cursor=c.cursor()
    comm='INSERT INTO '+filename+'("TITLE","USERNAME","PASSWORD") VALUES ("'+title+'","'+username+'","'+password+'");'
    print(comm)
    cursor.execute(comm)
    print('inserted')
    cursor.close()
    c.commit()
    c.close()

def retrieve(filename):
    n=filename+'.db'
    c=sqlite3.connect(n)
    comm='SELECT * FROM '+filename+';'
    viewer=c.execute(comm)
    for row in viewer:
        for k in row:
            print(k,end=' ')
        print()
    print('done')
    c.close()

def delete(filename,title):
    n=filename+'.db'
    c=sqlite3.connect(n)
    comm='DELETE FROM '+filename+' WHERE TITLE="'+title+'";'
    cursor=c.cursor()
    cursor.execute(comm)
    c.commit()
    c.close()
    print('deleted')

def sift(filename):
    n=filename+'.db'
    c=sqlite3.connect(n)
    comm='SELECT * FROM '+filename+';'
    viewer=c.execute(comm)
    L=[]
    for row in viewer:
        L+=[row[0]]
    c.close()
    return L

def addmastertable(file,password):
    k=KeyGen('123456789')
    spdecrypt(k,'eTable.db')
    n='eTable.db'
    c=sqlite3.connect(n)
    comm='INSERT INTO eTable ("USERNAME","PASSWORD") VALUES ("'+file+'","'+password+'");'
    c.execute(comm)
    c.commit()
    c.close()
    spencrypt(k,'eTable.db')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win=Ui_Aegis()
    win.show()
    sys.exit(app.exec_())
