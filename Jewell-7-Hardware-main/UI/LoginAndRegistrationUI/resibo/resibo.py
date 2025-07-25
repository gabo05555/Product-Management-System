# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resibo.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Receipt(object):
    def setupUi(self, Receipt):
        Receipt.setObjectName("Receipt")
        Receipt.resize(500, 781)
        Receipt.setMinimumSize(QtCore.QSize(500, 700))
        Receipt.setMaximumSize(QtCore.QSize(500, 800))
        Receipt.setStyleSheet("background-color:#f0f0f0;")
        self.centralwidget = QtWidgets.QWidget(Receipt)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-50, -10, 671, 791))
        self.widget.setMaximumSize(QtCore.QSize(671, 16777215))
        self.widget.setStyleSheet("background-color:#ffffff;\n"
"")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(270, 30, 60, 60))
        self.label_3.setMinimumSize(QtCore.QSize(60, 60))
        self.label_3.setMaximumSize(QtCore.QSize(60, 60))
        self.label_3.setStyleSheet("background-color:#e4f3ed;\n"
"border-radius:30px;\n"
"")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/Icon/icons8-success-40.png"))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 90, 401, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color:gray;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.widget)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 160, 411, 601))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setMinimumSize(QtCore.QSize(0, 30))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:#5C5C5C;")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setMinimumSize(QtCore.QSize(0, 40))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:#5C5C5C;")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_19.setMinimumSize(QtCore.QSize(0, 40))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("")
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_2.addWidget(self.label_19)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setMinimumSize(QtCore.QSize(0, 40))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:#5C5C5C;")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_20.setMinimumSize(QtCore.QSize(0, 40))
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("")
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_3.addWidget(self.label_20)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setMinimumSize(QtCore.QSize(0, 40))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:#5C5C5C;")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.PaymentIDData = QtWidgets.QLabel(self.layoutWidget1)
        self.PaymentIDData.setMinimumSize(QtCore.QSize(0, 40))
        self.PaymentIDData.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.PaymentIDData.setFont(font)
        self.PaymentIDData.setStyleSheet("")
        self.PaymentIDData.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.PaymentIDData.setObjectName("PaymentIDData")
        self.horizontalLayout_4.addWidget(self.PaymentIDData)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setMinimumSize(QtCore.QSize(0, 30))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:#5C5C5C;")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setMinimumSize(QtCore.QSize(0, 40))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:#5C5C5C;")
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.AddressData = QtWidgets.QLabel(self.layoutWidget1)
        self.AddressData.setMinimumSize(QtCore.QSize(0, 40))
        self.AddressData.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.AddressData.setFont(font)
        self.AddressData.setStyleSheet("")
        self.AddressData.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AddressData.setObjectName("AddressData")
        self.horizontalLayout_5.addWidget(self.AddressData)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_13.setMinimumSize(QtCore.QSize(0, 40))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:#5C5C5C;")
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.ContactData = QtWidgets.QLabel(self.layoutWidget1)
        self.ContactData.setMinimumSize(QtCore.QSize(0, 40))
        self.ContactData.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.ContactData.setFont(font)
        self.ContactData.setStyleSheet("")
        self.ContactData.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ContactData.setObjectName("ContactData")
        self.horizontalLayout_6.addWidget(self.ContactData)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setMinimumSize(QtCore.QSize(0, 40))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:#5C5C5C;")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.NameData = QtWidgets.QLabel(self.layoutWidget1)
        self.NameData.setMinimumSize(QtCore.QSize(0, 40))
        self.NameData.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.NameData.setFont(font)
        self.NameData.setStyleSheet("")
        self.NameData.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.NameData.setObjectName("NameData")
        self.horizontalLayout_7.addWidget(self.NameData)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_15.setMinimumSize(QtCore.QSize(0, 30))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:#5C5C5C;")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_4.addWidget(self.label_15)
        self.ProductsLabel = QtWidgets.QHBoxLayout()
        self.ProductsLabel.setSpacing(5)
        self.ProductsLabel.setObjectName("ProductsLabel")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_16.setMinimumSize(QtCore.QSize(0, 40))
        self.label_16.setMaximumSize(QtCore.QSize(16777201, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:#5C5C5C;")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.ProductsLabel.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_17.setMinimumSize(QtCore.QSize(0, 40))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color:#5C5C5C;")
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.ProductsLabel.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_18.setMinimumSize(QtCore.QSize(0, 40))
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color:#5C5C5C;")
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.ProductsLabel.addWidget(self.label_18)
        self.verticalLayout_4.addLayout(self.ProductsLabel)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.line = QtWidgets.QFrame(self.layoutWidget1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_27 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_27.setMinimumSize(QtCore.QSize(0, 40))
        self.label_27.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color:#5C5C5C;")
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_9.addWidget(self.label_27)
        self.ChangeData = QtWidgets.QLabel(self.layoutWidget1)
        self.ChangeData.setMinimumSize(QtCore.QSize(0, 40))
        self.ChangeData.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.ChangeData.setFont(font)
        self.ChangeData.setStyleSheet("")
        self.ChangeData.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ChangeData.setObjectName("ChangeData")
        self.horizontalLayout_9.addWidget(self.ChangeData)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_25 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_25.setMinimumSize(QtCore.QSize(0, 40))
        self.label_25.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color:#5C5C5C;")
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_8.addWidget(self.label_25)
        self.TotalPriceData = QtWidgets.QLabel(self.layoutWidget1)
        self.TotalPriceData.setMinimumSize(QtCore.QSize(0, 40))
        self.TotalPriceData.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.TotalPriceData.setFont(font)
        self.TotalPriceData.setStyleSheet("")
        self.TotalPriceData.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TotalPriceData.setObjectName("TotalPriceData")
        self.horizontalLayout_8.addWidget(self.TotalPriceData)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_26 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_26.setMinimumSize(QtCore.QSize(0, 40))
        self.label_26.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:#5C5C5C;")
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_10.addWidget(self.label_26)
        self.AmountPaidData = QtWidgets.QLabel(self.layoutWidget1)
        self.AmountPaidData.setMinimumSize(QtCore.QSize(0, 40))
        self.AmountPaidData.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.AmountPaidData.setFont(font)
        self.AmountPaidData.setStyleSheet("")
        self.AmountPaidData.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AmountPaidData.setObjectName("AmountPaidData")
        self.horizontalLayout_10.addWidget(self.AmountPaidData)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        Receipt.setCentralWidget(self.centralwidget)

        self.retranslateUi(Receipt)
        QtCore.QMetaObject.connectSlotsByName(Receipt)

    def retranslateUi(self, Receipt):
        _translate = QtCore.QCoreApplication.translate
        Receipt.setWindowTitle(_translate("Receipt", "RECEIPT"))
        self.label.setText(_translate("Receipt", "Payment Success!"))
        self.label_10.setText(_translate("Receipt", "Jewell 7 Hardware"))
        self.label_7.setText(_translate("Receipt", "Address:"))
        self.label_19.setText(_translate("Receipt", "991 Hardware St."))
        self.label_8.setText(_translate("Receipt", "Contact:"))
        self.label_20.setText(_translate("Receipt", "09530330697\n"
"09852434838"))
        self.label_9.setText(_translate("Receipt", "Payment ID: "))
        self.PaymentIDData.setText(_translate("Receipt", "Data"))
        self.label_11.setText(_translate("Receipt", "Customer Details"))
        self.label_14.setText(_translate("Receipt", "Address:"))
        self.AddressData.setText(_translate("Receipt", "Data"))
        self.label_13.setText(_translate("Receipt", "Contact:"))
        self.ContactData.setText(_translate("Receipt", "Data"))
        self.label_12.setText(_translate("Receipt", "Name:"))
        self.NameData.setText(_translate("Receipt", "Data"))
        self.label_15.setText(_translate("Receipt", "Products Purchased"))
        self.label_16.setText(_translate("Receipt", "Qty"))
        self.label_17.setText(_translate("Receipt", "Product"))
        self.label_18.setText(_translate("Receipt", "Price"))
        self.label_27.setText(_translate("Receipt", "Change:"))
        self.ChangeData.setText(_translate("Receipt", "Data"))
        self.label_25.setText(_translate("Receipt", "Total Price:"))
        self.TotalPriceData.setText(_translate("Receipt", "Data"))
        self.label_26.setText(_translate("Receipt", "Amount Paid:"))
        self.AmountPaidData.setText(_translate("Receipt", "Data"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Receipt = QtWidgets.QMainWindow()
    ui = Ui_Receipt()
    ui.setupUi(Receipt)
    Receipt.show()
    sys.exit(app.exec_())
