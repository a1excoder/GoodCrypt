from PySide2.QtWidgets import *
from PySide2.QtCore import QRect, Qt, QCoreApplication, QMetaObject
from PySide2.QtGui import QCursor

class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        WizardPage.resize(790, 480)
        self.tabWidget = QTabWidget(WizardPage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 791, 481))
        self.tabWidget.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 261, 31))
        self.label.setStyleSheet(u"font-size: 26px;")
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(580, 130, 161, 71))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"font-size: 18px;")
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(140, 100, 371, 41))
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setStyleSheet(u"font-size: 18px;")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 80, 231, 16))
        self.label_4.setStyleSheet(u"font-size: 15px;")
        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 100, 101, 41))
        self.pushButton_3.setStyleSheet(u"font-size: 12px;")
        self.pushButton_9 = QPushButton(self.tab)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(710, 420, 71, 31))
        self.pushButton_9.setStyleSheet(u"font-size: 16px;")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 220, 521, 141))
        self.label_5.setStyleSheet(u"font-size: 40px; color: yellowgreen;")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 281, 31))
        self.label_2.setStyleSheet(u"font-size: 26px;")
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(140, 80, 251, 16))
        self.label_9.setStyleSheet(u"font-size: 15px;")
        self.lineEdit_3 = QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(140, 100, 371, 41))
        self.lineEdit_3.setTabletTracking(False)
        self.lineEdit_3.setStyleSheet(u"font-size: 18px;")
        self.pushButton_8 = QPushButton(self.tab_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(580, 130, 161, 71))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"font-size: 18px;")
        self.pushButton_10 = QPushButton(self.tab_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(710, 420, 71, 31))
        self.pushButton_10.setStyleSheet(u"font-size: 16px;")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 220, 521, 141))
        self.label_6.setStyleSheet(u"font-size: 40px; color: yellowgreen;")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 181, 31))
        self.label_3.setStyleSheet(u"font-size: 26px;")
        self.commandLinkButton = QCommandLinkButton(self.tab_3)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(590, 400, 181, 41))
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.textBrowser = QTextBrowser(self.tab_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 60, 741, 321))
        self.textBrowser.setStyleSheet(u"border: 0px;")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(WizardPage)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(WizardPage)
    # setupUi

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(QCoreApplication.translate("WizardPage", u"GoodCrypt", None))
        self.label.setText(QCoreApplication.translate("WizardPage", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.pushButton.setText(QCoreApplication.translate("WizardPage", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.label_4.setText(QCoreApplication.translate("WizardPage", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c \u0434\u043b\u044f \u0448\u0438\u0444\u0440\u043e\u0432\u043a\u0438:", None))
        self.pushButton_3.setText(QCoreApplication.translate("WizardPage", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_9.setText(QCoreApplication.translate("WizardPage", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.label_5.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("WizardPage", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("WizardPage", u"\u0420\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.label_9.setText(QCoreApplication.translate("WizardPage", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c \u0434\u043b\u044f \u0440\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u043a\u0438:", None))
        self.pushButton_8.setText(QCoreApplication.translate("WizardPage", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.pushButton_10.setText(QCoreApplication.translate("WizardPage", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.label_6.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("WizardPage", u"\u0420\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("WizardPage", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.commandLinkButton.setText(QCoreApplication.translate("WizardPage", u"\u0421\u0430\u0439\u0442 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430", None))
        self.textBrowser.setHtml(QCoreApplication.translate("WizardPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u042d\u0442\u043e </span><span style=\" font-size:12pt; font-weight:600; color:#00aa00;\">Open source</span><span style=\" font-size:12pt;\"> \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0444\u0430\u0439\u043b\u043e\u0432,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u0438\u0441\u0445\u043e\u0434\u043d"
                        "\u044b\u0439 \u043a\u043e\u0434 \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u043d\u0430 Github \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0435 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Github -&gt; https://github.com/a1excoder/</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">YouTube -&gt; https://www.youtube.com/c/alexcode</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">E-mail -&gt; alexco"
                        "de1dev@gmail.com</span></p><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">V3</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("WizardPage", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
    # retranslateUi