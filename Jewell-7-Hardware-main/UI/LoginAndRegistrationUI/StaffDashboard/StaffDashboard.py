# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StaffDashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StaffDashboard(object):
    def setupUi(self, StaffDashboard):
        StaffDashboard.setObjectName("StaffDashboard")
        StaffDashboard.resize(1254, 1119)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        StaffDashboard.setFont(font)
        StaffDashboard.setToolTipDuration(-1)
        StaffDashboard.setLayoutDirection(QtCore.Qt.LeftToRight)
        StaffDashboard.setStyleSheet("background-color:#fff;\n"
"")
        StaffDashboard.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(StaffDashboard)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 783, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(30, 15, 70, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.aboutUs_button = QtWidgets.QPushButton(self.centralwidget)
        self.aboutUs_button.setMinimumSize(QtCore.QSize(150, 50))
        self.aboutUs_button.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.aboutUs_button.setFont(font)
        self.aboutUs_button.setMouseTracking(True)
        self.aboutUs_button.setTabletTracking(True)
        self.aboutUs_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.aboutUs_button.setStyleSheet("QPushButton {\n"
" background-color: #f6f4f4;\n"
"border-radius:25px;\n"
"color:black;\n"
";\n"
"}\n"
"QPushButton#quit_button {\n"
"   background-color: green;\n"
"}\n"
"QPushButton::pressed {\n"
"background-color: #fff;\n"
"}\n"
"QpushButton{\n"
"border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"border-width:200px;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"\n"
"shoppingbag:hover{\n"
"color:#fff;\n"
"background-repeat:no-repeat;\n"
"}\n"
"\n"
"border:none;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Help/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aboutUs_button.setIcon(icon)
        self.aboutUs_button.setIconSize(QtCore.QSize(30, 30))
        self.aboutUs_button.setObjectName("aboutUs_button")
        self.horizontalLayout.addWidget(self.aboutUs_button)
        self.line = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(0, 25))
        self.line.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setMinimumSize(QtCore.QSize(50, 50))
        self.help_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.help_button.setFont(font)
        self.help_button.setMouseTracking(True)
        self.help_button.setTabletTracking(True)
        self.help_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.help_button.setStyleSheet("QPushButton {\n"
" background-color: #f6f4f4;\n"
"border-radius:25px;\n"
"color:black;\n"
";\n"
"}\n"
"QPushButton#quit_button {\n"
"   background-color: green;\n"
"}\n"
"QPushButton::pressed {\n"
"background-color: #fff;\n"
"}\n"
"QpushButton{\n"
"border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"border-width:200px;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"\n"
"shoppingbag:hover{\n"
"color:#fff;\n"
"background-repeat:no-repeat;\n"
"}\n"
"\n"
"border:none;\n"
"")
        self.help_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Info/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_button.setIcon(icon1)
        self.help_button.setIconSize(QtCore.QSize(20, 20))
        self.help_button.setObjectName("help_button")
        self.horizontalLayout.addWidget(self.help_button)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 2)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(325, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(325, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.widget_2.setFont(font)
        self.widget_2.setToolTipDuration(-1)
        self.widget_2.setStyleSheet("background-color: #f6f4f4 ;\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(50, 10, -1, 10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.logo = QtWidgets.QLabel(self.widget_2)
        self.logo.setMinimumSize(QtCore.QSize(200, 150))
        self.logo.setMaximumSize(QtCore.QSize(200, 150))
        self.logo.setStyleSheet("image: url(:/Icon/logo.png);")
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo.setText("")
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.verticalLayout_4.addWidget(self.logo)
        self.adminLabel = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.adminLabel.setFont(font)
        self.adminLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.adminLabel.setStyleSheet("background:none;")
        self.adminLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.adminLabel.setObjectName("adminLabel")
        self.verticalLayout_4.addWidget(self.adminLabel)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.line_3 = QtWidgets.QFrame(self.widget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_5.addWidget(self.line_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem4)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 50, -1, -1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, -1, 40, -1)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.shop_button = QtWidgets.QPushButton(self.widget_2)
        self.shop_button.setMinimumSize(QtCore.QSize(150, 40))
        self.shop_button.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.shop_button.setFont(font)
        self.shop_button.setMouseTracking(True)
        self.shop_button.setTabletTracking(True)
        self.shop_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.shop_button.setStyleSheet("QPushButton {\n"
" background-color: #f6f4f4;\n"
"border-radius:17px;\n"
"color:black;\n"
"padding-right:98px;\n"
"}\n"
"QPushButton#quit_button {\n"
"   background-color: green;\n"
"}\n"
"QPushButton::pressed {\n"
"background-color: #fff;\n"
"}\n"
"QpushButton{\n"
"border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"border-width:200px;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"\n"
"shoppingbag:hover{\n"
"color:#fff;\n"
"background-repeat:no-repeat;\n"
"}\n"
"\n"
"border:none;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Shop/shopping-bag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/Shop/white_bag.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.shop_button.setIcon(icon2)
        self.shop_button.setIconSize(QtCore.QSize(20, 20))
        self.shop_button.setObjectName("shop_button")
        self.verticalLayout.addWidget(self.shop_button)
        self.cart_button = QtWidgets.QPushButton(self.widget_2)
        self.cart_button.setMinimumSize(QtCore.QSize(150, 40))
        self.cart_button.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.cart_button.setFont(font)
        self.cart_button.setMouseTracking(True)
        self.cart_button.setTabletTracking(True)
        self.cart_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cart_button.setStyleSheet("QPushButton {\n"
" background-color: #f6f4f4;\n"
"border-radius:17px;\n"
"color:black;\n"
"padding-right:106px;\n"
"}\n"
"QPushButton#quit_button {\n"
"   background-color: green;\n"
"}\n"
"QPushButton::pressed {\n"
"background-color: #fff;\n"
"}\n"
"QpushButton{\n"
"border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"border-width:200px;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"\n"
"border:none;\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Cart/cart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cart_button.setIcon(icon3)
        self.cart_button.setIconSize(QtCore.QSize(22, 22))
        self.cart_button.setObjectName("cart_button")
        self.verticalLayout.addWidget(self.cart_button)
        spacerItem5 = QtWidgets.QSpacerItem(20, 400, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(25, 190, 25, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_2 = QtWidgets.QFrame(self.widget_2)
        self.line_2.setStyleSheet("background-color:none;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.logout_button = QtWidgets.QPushButton(self.widget_2)
        self.logout_button.setMinimumSize(QtCore.QSize(100, 40))
        self.logout_button.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.logout_button.setFont(font)
        self.logout_button.setMouseTracking(True)
        self.logout_button.setTabletTracking(True)
        self.logout_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logout_button.setStyleSheet("QPushButton {\n"
" background-color: #f6f4f4;\n"
"border-radius:13px;\n"
"color: #636363;\n"
";\n"
"}\n"
"QPushButton#quit_button {\n"
"   background-color: green;\n"
"}\n"
"QPushButton::pressed {\n"
"background-color: #fff;\n"
"}\n"
"QpushButton{\n"
"border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"border-width:200px;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"   background-color: #81cdc6;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"color:#fff;\n"
"}\n"
"\n"
"shoppingbag:hover{\n"
"color:#fff;\n"
"background-repeat:no-repeat;\n"
"}\n"
"\n"
"border:none;\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/logout/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_button.setIcon(icon4)
        self.logout_button.setIconSize(QtCore.QSize(25, 25))
        self.logout_button.setObjectName("logout_button")
        self.verticalLayout_2.addWidget(self.logout_button)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 3, 1)
        StaffDashboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(StaffDashboard)
        QtCore.QMetaObject.connectSlotsByName(StaffDashboard)

    def retranslateUi(self, StaffDashboard):
        _translate = QtCore.QCoreApplication.translate
        StaffDashboard.setWindowTitle(_translate("StaffDashboard", "Staff Dashboard"))
        self.aboutUs_button.setText(_translate("StaffDashboard", "About us"))
        self.adminLabel.setText(_translate("StaffDashboard", "    Staff  Dashboard"))
        self.shop_button.setText(_translate("StaffDashboard", "  Shop"))
        self.cart_button.setText(_translate("StaffDashboard", "  Cart"))
        self.logout_button.setText(_translate("StaffDashboard", "Sign out"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StaffDashboard = QtWidgets.QMainWindow()
    ui = Ui_StaffDashboard()
    ui.setupUi(StaffDashboard)
    StaffDashboard.show()
    sys.exit(app.exec_())
