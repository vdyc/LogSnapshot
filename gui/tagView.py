# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TagView.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(954, 863)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeView_tag = QtWidgets.QTreeView(Form)
        self.treeView_tag.setObjectName("treeView_tag")
        self.verticalLayout.addWidget(self.treeView_tag)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_generate_tag_file = QtWidgets.QPushButton(Form)
        self.pushButton_generate_tag_file.setObjectName("pushButton_generate_tag_file")
        self.horizontalLayout.addWidget(self.pushButton_generate_tag_file)
        self.pushButton_open_tag_file = QtWidgets.QPushButton(Form)
        self.pushButton_open_tag_file.setObjectName("pushButton_open_tag_file")
        self.horizontalLayout.addWidget(self.pushButton_open_tag_file)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonBox_tag = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox_tag.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_tag.setObjectName("buttonBox_tag")
        self.horizontalLayout.addWidget(self.buttonBox_tag)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_generate_tag_file.setText(_translate("Form", "Generate"))
        self.pushButton_open_tag_file.setText(_translate("Form", "Open"))
