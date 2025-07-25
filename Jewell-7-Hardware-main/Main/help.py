from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QVBoxLayout, QScrollArea, QWidget, QLabel, QPushButton, QFileDialog, QDialog
from PyQt5.QtGui import QPixmap
import fitz #pip install PyMuPDF

class HelpTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(HelpTab, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
            Form.setObjectName("Form")
            Form.resize(1079, 840)
            Form.setStyleSheet("background-color:#fff;")
            self.gridLayout_10 = QtWidgets.QGridLayout(Form)
            self.gridLayout_10.setObjectName("gridLayout_10")
            self.verticalLayout_2 = QtWidgets.QVBoxLayout()
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.verticalLayout = QtWidgets.QVBoxLayout()
            self.verticalLayout.setContentsMargins(-1, 0, -1, 40)
            self.verticalLayout.setSpacing(5)
            self.verticalLayout.setObjectName("verticalLayout")
            self.label = QtWidgets.QLabel(Form)
            self.label.setMaximumSize(QtCore.QSize(16777215, 71))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Semibold")
            font.setPointSize(40)
            font.setBold(True)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.verticalLayout.addWidget(self.label)
            self.label_2 = QtWidgets.QLabel(Form)
            self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(12)
            font.setBold(False)
            font.setWeight(50)
            self.label_2.setFont(font)
            self.label_2.setObjectName("label_2")
            self.verticalLayout.addWidget(self.label_2)
            self.verticalLayout_2.addLayout(self.verticalLayout)
            
            # Adding "View User Manual" button
            self.view_manual_button = QtWidgets.QPushButton("View User Manual")
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(8)
            font.setBold(True)
            font.setWeight(75)
            font.setStrikeOut(False)
            self.view_manual_button.setFont(font)
            self.view_manual_button.setMaximumSize(QtCore.QSize(16777215, 35))
            self.view_manual_button.clicked.connect(self.openUserManual)
            self.view_manual_button.setStyleSheet("QPushButton {\n"
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
                    
            self.verticalLayout_2.addWidget(self.view_manual_button)
        
            self.line = QtWidgets.QFrame(Form)
            self.line.setFrameShape(QtWidgets.QFrame.HLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line.setObjectName("line")
            self.verticalLayout_2.addWidget(self.line)
            self.gridLayout_9 = QtWidgets.QGridLayout()
            self.gridLayout_9.setContentsMargins(-1, 20, -1, 0)
            self.gridLayout_9.setHorizontalSpacing(30)
            self.gridLayout_9.setVerticalSpacing(20)
            self.gridLayout_9.setObjectName("gridLayout_9")
            self.gridLayout_5 = QtWidgets.QGridLayout()
            self.gridLayout_5.setVerticalSpacing(10)
            self.gridLayout_5.setObjectName("gridLayout_5")
            self.label_11 = QtWidgets.QLabel(Form)
            self.label_11.setMaximumSize(QtCore.QSize(16777215, 35))
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.label_11.setFont(font)
            self.label_11.setObjectName("label_11")
            self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)
            self.widget_3 = QtWidgets.QWidget(Form)
            self.widget_3.setMinimumSize(QtCore.QSize(375, 130))
            self.widget_3.setMaximumSize(QtCore.QSize(375, 130))
            self.widget_3.setStyleSheet("background-color:#f3f2f0;\n"
    "border:none;\n"
    "border-radius: 10px;")
            self.widget_3.setObjectName("widget_3")
            self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_3)
            self.gridLayout_6.setObjectName("gridLayout_6")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.label_13 = QtWidgets.QLabel(self.widget_3)
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            self.label_13.setFont(font)
            self.label_13.setObjectName("label_13")
            self.horizontalLayout_4.addWidget(self.label_13)
            self.gridLayout_6.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
            self.gridLayout_5.addWidget(self.widget_3, 1, 0, 1, 1)
            self.gridLayout_9.addLayout(self.gridLayout_5, 0, 0, 1, 1)
            self.gridLayout_7 = QtWidgets.QGridLayout()
            self.gridLayout_7.setVerticalSpacing(10)
            self.gridLayout_7.setObjectName("gridLayout_7")
            self.widget_4 = QtWidgets.QWidget(Form)
            self.widget_4.setMinimumSize(QtCore.QSize(375, 130))
            self.widget_4.setMaximumSize(QtCore.QSize(375, 130))
            self.widget_4.setStyleSheet("background-color:#f3f2f0;\n"
    "border:none;\n"
    "border-radius: 10px;")
            self.widget_4.setObjectName("widget_4")
            self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_4)
            self.gridLayout_8.setObjectName("gridLayout_8")
            self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_6.setObjectName("horizontalLayout_6")
            self.label_15 = QtWidgets.QLabel(self.widget_4)
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            self.label_15.setFont(font)
            self.label_15.setObjectName("label_15")
            self.horizontalLayout_6.addWidget(self.label_15)
            self.gridLayout_8.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
            self.gridLayout_7.addWidget(self.widget_4, 1, 0, 1, 1)
            self.label_12 = QtWidgets.QLabel(Form)
            self.label_12.setMaximumSize(QtCore.QSize(16777215, 35))
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.label_12.setFont(font)
            self.label_12.setObjectName("label_12")
            self.gridLayout_7.addWidget(self.label_12, 0, 0, 1, 1)
            self.gridLayout_9.addLayout(self.gridLayout_7, 0, 1, 1, 1)
            self.gridLayout_3 = QtWidgets.QGridLayout()
            self.gridLayout_3.setVerticalSpacing(10)
            self.gridLayout_3.setObjectName("gridLayout_3")
            self.label_10 = QtWidgets.QLabel(Form)
            self.label_10.setMaximumSize(QtCore.QSize(16777215, 17))
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.label_10.setFont(font)
            self.label_10.setObjectName("label_10")
            self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
            self.widget_2 = QtWidgets.QWidget(Form)
            self.widget_2.setMinimumSize(QtCore.QSize(375, 130))
            self.widget_2.setMaximumSize(QtCore.QSize(375, 130))
            self.widget_2.setStyleSheet("background-color:#f3f2f0;\n"
    "border:none;\n"
    "border-radius: 10px;")
            self.widget_2.setObjectName("widget_2")
            self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
            self.gridLayout_4.setContentsMargins(-1, 9, -1, 50)
            self.gridLayout_4.setVerticalSpacing(0)
            self.gridLayout_4.setObjectName("gridLayout_4")
            self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_5.setObjectName("horizontalLayout_5")
            self.label_14 = QtWidgets.QLabel(self.widget_2)
            self.label_14.setMaximumSize(QtCore.QSize(16777215, 30))
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            self.label_14.setFont(font)
            self.label_14.setObjectName("label_14")
            self.horizontalLayout_5.addWidget(self.label_14)
            self.gridLayout_4.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
            self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)
            self.gridLayout_9.addLayout(self.gridLayout_3, 1, 0, 1, 1)
            self.gridLayout_2 = QtWidgets.QGridLayout()
            self.gridLayout_2.setVerticalSpacing(10)
            self.gridLayout_2.setObjectName("gridLayout_2")
            self.label_3 = QtWidgets.QLabel(Form)
            self.label_3.setMaximumSize(QtCore.QSize(16777215, 17))
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.label_3.setFont(font)
            self.label_3.setObjectName("label_3")
            self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
            self.widget = QtWidgets.QWidget(Form)
            self.widget.setMinimumSize(QtCore.QSize(375, 130))
            self.widget.setMaximumSize(QtCore.QSize(375, 130))
            self.widget.setStyleSheet("background-color:#f3f2f0;\n"
    "border:none;\n"
    "border-radius: 10px;")
            self.widget.setObjectName("widget")
            self.gridLayout = QtWidgets.QGridLayout(self.widget)
            self.gridLayout.setObjectName("gridLayout")
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.label_4 = QtWidgets.QLabel(self.widget)
            self.label_4.setMinimumSize(QtCore.QSize(30, 30))
            self.label_4.setMaximumSize(QtCore.QSize(30, 30))
            self.label_4.setStyleSheet("border-radius:15px;\n"
    "background-color:#00bf63;")
            self.label_4.setText("")
            self.label_4.setObjectName("label_4")
            self.horizontalLayout.addWidget(self.label_4)
            self.label_7 = QtWidgets.QLabel(self.widget)
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            self.label_7.setFont(font)
            self.label_7.setObjectName("label_7")
            self.horizontalLayout.addWidget(self.label_7)
            self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.label_5 = QtWidgets.QLabel(self.widget)
            self.label_5.setMinimumSize(QtCore.QSize(30, 30))
            self.label_5.setMaximumSize(QtCore.QSize(30, 30))
            self.label_5.setStyleSheet("border-radius:15px;\n"
    "background-color:#ff914d;")
            self.label_5.setText("")
            self.label_5.setObjectName("label_5")
            self.horizontalLayout_2.addWidget(self.label_5)
            self.label_8 = QtWidgets.QLabel(self.widget)
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            self.label_8.setFont(font)
            self.label_8.setObjectName("label_8")
            self.horizontalLayout_2.addWidget(self.label_8)
            self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.label_6 = QtWidgets.QLabel(self.widget)
            self.label_6.setMinimumSize(QtCore.QSize(30, 30))
            self.label_6.setMaximumSize(QtCore.QSize(30, 30))
            self.label_6.setStyleSheet("border-radius:15px;\n"
    "background-color:#ff3131;")
            self.label_6.setText("")
            self.label_6.setObjectName("label_6")
            self.horizontalLayout_3.addWidget(self.label_6)
            self.label_9 = QtWidgets.QLabel(self.widget)
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            self.label_9.setFont(font)
            self.label_9.setObjectName("label_9")
            self.horizontalLayout_3.addWidget(self.label_9)
            self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
            self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)
            self.gridLayout_9.addLayout(self.gridLayout_2, 2, 0, 1, 1)
            self.verticalLayout_2.addLayout(self.gridLayout_9)
            self.gridLayout_10.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

            self.retranslateUi(Form)
            QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Form"))
            self.label.setText(_translate("Form", "Frequently Asked Questions"))
            self.label_2.setText(_translate("Form", " Quick answers to questions you may have. Can\'t find what you\'re are looking for? Check out our full documentation."))
            self.label_11.setText(_translate("Form", "When I generate a line graph from the data of the previous\n"
    " week, it shows a broken line. What does this indicate?"))
            self.label_13.setText(_translate("Form", "The broken line represents the projected values of the graph\n"
    " for the next day, estimating the number of transactions \n"
    "based on past transaction data."))
            self.label_15.setText(_translate("Form", "The broken line represents the projected values of the graph\n"
    " for the next day, estimating the number of transactions \n"
    "based on past transaction data."))
            self.label_12.setText(_translate("Form", "When I generate a pie chart or a bar chart, not all \n"
    "product names or categories are displayed. Why is that?"))
            self.label_10.setText(_translate("Form", "What does “Threshold” mean?"))
            self.label_14.setText(_translate("Form", "Threshold is a point or level where inventory must be\n"
    "reordered to avoid stockouts."))
            self.label_3.setText(_translate("Form", "What do colors signify in product management?"))
            self.label_7.setText(_translate("Form", "High stock level, restocking is not a priority."))
            self.label_8.setText(_translate("Form", "Moderate stock level, restocking is optional."))
            self.label_9.setText(_translate("Form", "Low stock level, restocking is highly recommended."))

    def openUserManual(self):
        import os
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "Jewell 7 Hardware User Manual.pdf")
        doc = fitz.open(file_path)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        widget = QWidget()
        layout = QVBoxLayout(widget)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            img = QPixmap.fromImage(QtGui.QImage(pix.samples, pix.width, pix.height, pix.stride, QtGui.QImage.Format_RGB888))
            label = QLabel()
            label.setPixmap(img)
            layout.addWidget(label)
        scroll_area.setWidget(widget)
        
        dialog = QDialog(self)
        dialog.setWindowTitle("User Manual")
        dialog.setLayout(QVBoxLayout())
        dialog.layout().addWidget(scroll_area)
        dialog.resize(663, 850)
        dialog.exec_()
