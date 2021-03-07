# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogSnapshot.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1074, 861)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_pid_filter = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pid_filter.setObjectName("lineEdit_pid_filter")
        self.horizontalLayout_3.addWidget(self.lineEdit_pid_filter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_time_format = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_time_format.setObjectName("pushButton_time_format")
        self.horizontalLayout_3.addWidget(self.pushButton_time_format)
        self.pushButton_range = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_range.setObjectName("pushButton_range")
        self.horizontalLayout_3.addWidget(self.pushButton_range)
        self.pushButton_tag = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_tag.setObjectName("pushButton_tag")
        self.horizontalLayout_3.addWidget(self.pushButton_tag)
        self.comboBox_debug_level = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_debug_level.setObjectName("comboBox_debug_level")
        self.horizontalLayout_3.addWidget(self.comboBox_debug_level)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableView_main_log = QtWidgets.QTableView(self.centralwidget)
        self.tableView_main_log.setObjectName("tableView_main_log")
        self.verticalLayout.addWidget(self.tableView_main_log)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tabWidget_bottom = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget_bottom.setObjectName("tabWidget_bottom")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeView_filter = QtWidgets.QTreeView(self.tab)
        self.treeView_filter.setObjectName("treeView_filter")
        self.horizontalLayout.addWidget(self.treeView_filter)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButton_open_filter = QtWidgets.QPushButton(self.tab)
        self.pushButton_open_filter.setObjectName("pushButton_open_filter")
        self.verticalLayout_2.addWidget(self.pushButton_open_filter)
        self.pushButton_save_filter = QtWidgets.QPushButton(self.tab)
        self.pushButton_save_filter.setObjectName("pushButton_save_filter")
        self.verticalLayout_2.addWidget(self.pushButton_save_filter)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.tabWidget_bottom.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.treeView_report = QtWidgets.QTreeView(self.tab_2)
        self.treeView_report.setObjectName("treeView_report")
        self.horizontalLayout_2.addWidget(self.treeView_report)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.pushButton_report_generate = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_report_generate.setObjectName("pushButton_report_generate")
        self.verticalLayout_3.addWidget(self.pushButton_report_generate)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.tabWidget_bottom.addTab(self.tab_2, "")
        self.sub = QtWidgets.QWidget()
        self.sub.setObjectName("sub")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.sub)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableView_sub_log = QtWidgets.QTableView(self.sub)
        self.tableView_sub_log.setObjectName("tableView_sub_log")
        self.horizontalLayout_4.addWidget(self.tableView_sub_log)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.pushButton_3 = QtWidgets.QPushButton(self.sub)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_sub_log_open = QtWidgets.QPushButton(self.sub)
        self.pushButton_sub_log_open.setObjectName("pushButton_sub_log_open")
        self.verticalLayout_4.addWidget(self.pushButton_sub_log_open)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.tabWidget_bottom.addTab(self.sub, "")
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 20))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuOpen.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_bottom.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_pid_filter.setPlaceholderText(_translate("MainWindow", "PID/TID filter Delimiter: \":,;\" or space"))
        self.pushButton_time_format.setText(_translate("MainWindow", "Orig"))
        self.pushButton_range.setText(_translate("MainWindow", "Range"))
        self.pushButton_tag.setText(_translate("MainWindow", "Tag"))
        self.comboBox_debug_level.setPlaceholderText(_translate("MainWindow", "Debug"))
        self.pushButton_open_filter.setText(_translate("MainWindow", "Open"))
        self.pushButton_save_filter.setText(_translate("MainWindow", "Save"))
        self.tabWidget_bottom.setTabText(self.tabWidget_bottom.indexOf(self.tab), _translate("MainWindow", "Filter"))
        self.pushButton_report_generate.setText(_translate("MainWindow", "Generate"))
        self.tabWidget_bottom.setTabText(self.tabWidget_bottom.indexOf(self.tab_2), _translate("MainWindow", "Report"))
        self.pushButton_3.setText(_translate("MainWindow", "Sync"))
        self.pushButton_sub_log_open.setText(_translate("MainWindow", "Open"))
        self.tabWidget_bottom.setTabText(self.tabWidget_bottom.indexOf(self.sub), _translate("MainWindow", "2nd Log"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))