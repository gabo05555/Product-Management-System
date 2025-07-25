# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Products.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProductsTab(object):
    def setupUi(self, ProductsTab):
        ProductsTab.setObjectName("ProductsTab")
        ProductsTab.resize(1722, 741)
        ProductsTab.setStyleSheet("background-color:#fff;")
        self.gridLayout = QtWidgets.QGridLayout(ProductsTab)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.search_button = QtWidgets.QPushButton(ProductsTab)
        self.search_button.setMinimumSize(QtCore.QSize(50, 50))
        self.search_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.search_button.setFont(font)
        self.search_button.setMouseTracking(True)
        self.search_button.setTabletTracking(True)
        self.search_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.search_button.setStyleSheet("QPushButton {\n"
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
"\n"
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
        self.search_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/search/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon)
        self.search_button.setIconSize(QtCore.QSize(20, 20))
        self.search_button.setObjectName("search_button")
        self.horizontalLayout_2.addWidget(self.search_button)
        self.search_input = QtWidgets.QLineEdit(ProductsTab)
        self.search_input.setMinimumSize(QtCore.QSize(300, 50))
        self.search_input.setMaximumSize(QtCore.QSize(600, 75))
        self.search_input.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.search_input.setStyleSheet("border-radius:25px;\n"
"padding-right:10px;\n"
"padding-left:10px;\n"
"background-color:#f6f4f4;\n"
"")
        self.search_input.setText("")
        self.search_input.setCursorPosition(0)
        self.search_input.setDragEnabled(False)
        self.search_input.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.search_input.setObjectName("search_input")
        self.horizontalLayout_2.addWidget(self.search_input)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(ProductsTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(290, -1, 290, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.add_button = QtWidgets.QPushButton(ProductsTab)
        self.add_button.setMinimumSize(QtCore.QSize(175, 50))
        self.add_button.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.add_button.setFont(font)
        self.add_button.setMouseTracking(True)
        self.add_button.setTabletTracking(True)
        self.add_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.add_button.setStyleSheet("QPushButton {\n"
" background-color: #10cc94;\n"
"border-radius:12px;\n"
"color:#fff;\n"
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
"   background-color: #0a9c73;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"}\n"
"\n"
"border:none;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/Shop/Shoppingcart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_button.setIcon(icon1)
        self.add_button.setIconSize(QtCore.QSize(22, 22))
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.modify_button = QtWidgets.QPushButton(ProductsTab)
        self.modify_button.setMinimumSize(QtCore.QSize(175, 50))
        self.modify_button.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.modify_button.setFont(font)
        self.modify_button.setMouseTracking(True)
        self.modify_button.setTabletTracking(True)
        self.modify_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.modify_button.setStyleSheet("QPushButton {\n"
" background-color: #10cc94;\n"
"border-radius:12px;\n"
"color:#fff;\n"
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
"   background-color: #0a9c73;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"}\n"
"\n"
"border:none;\n"
"")
        self.modify_button.setIcon(icon1)
        self.modify_button.setIconSize(QtCore.QSize(22, 22))
        self.modify_button.setObjectName("modify_button")
        self.horizontalLayout.addWidget(self.modify_button)
        self.changeStatus_button = QtWidgets.QPushButton(ProductsTab)
        self.changeStatus_button.setMinimumSize(QtCore.QSize(175, 50))
        self.changeStatus_button.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.changeStatus_button.setFont(font)
        self.changeStatus_button.setMouseTracking(True)
        self.changeStatus_button.setTabletTracking(True)
        self.changeStatus_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.changeStatus_button.setStyleSheet("QPushButton {\n"
" background-color: #5698d2;\n"
"border-radius:12px;\n"
"color:#fff;\n"
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
"   background-color: #4379a5;\n"
"   transition: background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1);\n"
"}\n"
"\n"
"border:none;\n"
"")
        self.changeStatus_button.setIcon(icon1)
        self.changeStatus_button.setIconSize(QtCore.QSize(22, 22))
        self.changeStatus_button.setObjectName("changeStatus_button")
        self.horizontalLayout.addWidget(self.changeStatus_button)
        spacerItem3 = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(ProductsTab)
        QtCore.QMetaObject.connectSlotsByName(ProductsTab)

    def retranslateUi(self, ProductsTab):
        _translate = QtCore.QCoreApplication.translate
        ProductsTab.setWindowTitle(_translate("ProductsTab", "Products"))
        self.search_input.setPlaceholderText(_translate("ProductsTab", "  Search Products..."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ProductsTab", "Product ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ProductsTab", "Product"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ProductsTab", "Brand"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ProductsTab", "Variation"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ProductsTab", "Size"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ProductsTab", "Price"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("ProductsTab", "Stock"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("ProductsTab", "Threshold"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("ProductsTab", "Category"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("ProductsTab", "Status"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("ProductsTab", "Supplier"))
        self.add_button.setText(_translate("ProductsTab", "Add"))
        self.modify_button.setText(_translate("ProductsTab", "Modify"))
        self.changeStatus_button.setText(_translate("ProductsTab", "Change Status"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProductsTab = QtWidgets.QWidget()
    ui = Ui_ProductsTab()
    ui.setupUi(ProductsTab)
    ProductsTab.show()
    sys.exit(app.exec_())
