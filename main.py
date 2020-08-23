import requests
import urllib.request
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")  
        self.WIDTH = 2000
        self.HEIGHT = 1600
        MainWindow.resize(self.WIDTH, self.HEIGHT)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #3171af;color: #fff")

        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, self.WIDTH, 100))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.header.setStyleSheet("background: #0063b1;")

        self.search_label = QtWidgets.QLabel(self.header)
        self.search_label.setGeometry(QtCore.QRect(1120, 20, 250, 60))
        font1 = QtGui.QFont()
        font1.setPixelSize(32)
        self.search_label.setFont(font1)
        self.search_label.setObjectName("search_label")

        self.search = QtWidgets.QLineEdit(self.header)
        self.search.setGeometry(QtCore.QRect(1380, 20, 450, 60))
        self.search.setFont(font1)
        self.search.setObjectName("search")
        self.search.setStyleSheet("background-color: #31719b;padding-left: 10px;")

        self.validate = QtWidgets.QPushButton(self.header)
        self.validate.setGeometry(QtCore.QRect(1840, 20, 100, 60))
        self.validate.setObjectName("validate")
        self.validate.setStyleSheet("background-color: #31719b;")
        self.validate.clicked.connect(self.request)

        self.current = QtWidgets.QFrame(self.centralwidget)
        self.current.setGeometry(QtCore.QRect(0, 100, self.WIDTH, 320))
        self.current.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.current.setFrameShadow(QtWidgets.QFrame.Raised)
        self.current.setObjectName("current_frame")

        self.location_label = QtWidgets.QLabel(self.current)
        self.location_label.setGeometry(QtCore.QRect(0, 20, self.WIDTH, 64))
        font2 = QtGui.QFont()
        font2.setPointSize(20)
        self.location_label.setFont(font2)
        self.location_label.setObjectName("location_label")
        self.location_label.setAlignment(QtCore.Qt.AlignCenter)

        self.condition_icon = QtWidgets.QLabel(self.current)
        self.condition_icon.setGeometry(QtCore.QRect(self.WIDTH // 2 - 180, 100, 110, 110))
        self.condition_icon.setText("")
        self.pixmap1 = QtGui.QPixmap()
        self.condition_icon.setScaledContents(True)
        self.condition_icon.setObjectName("condition_icon")

        self.temp_label = QtWidgets.QLabel(self.current)
        self.temp_label.setGeometry(QtCore.QRect(self.WIDTH // 2 - 70, 100, 200, 110))
        font3 = QtGui.QFont()
        font3.setPointSize(48)
        self.temp_label.setFont(font3)
        self.temp_label.setObjectName("temp_label")

        self.temp_f = QtWidgets.QPushButton(self.current)
        self.temp_f.setGeometry(QtCore.QRect(self.WIDTH // 2 + 130, 100, 50, 50))
        self.temp_f.setObjectName("temp_f_button")
        self.temp_f.clicked.connect(self.print_temp_f)
        self.temp_f_active = True
        self.temp_f.hide()

        self.temp_c = QtWidgets.QPushButton(self.current)
        self.temp_c.setGeometry(QtCore.QRect(self.WIDTH // 2 + 130, 150, 50, 50))
        self.temp_c.setObjectName("temp_c_button")
        self.temp_c.clicked.connect(self.print_temp_c)
        self.temp_c_active = False
        self.temp_c.hide()

        self.condition_text = QtWidgets.QLabel(self.current)
        self.condition_text.setGeometry(QtCore.QRect(0, 210, self.WIDTH, 64))
        self.condition_text.setFont(font2)
        self.condition_text.setObjectName("condition_text")
        self.condition_text.setAlignment(QtCore.Qt.AlignCenter)

        self.last_update_label = QtWidgets.QLabel(self.current)
        self.last_update_label.setGeometry(QtCore.QRect(0, 280, self.WIDTH, 40))
        font4 = QtGui.QFont()
        font4.setPointSize(12)
        self.last_update_label.setFont(font4)
        self.last_update_label.setObjectName("last_update_label")
        self.last_update_label.setAlignment(QtCore.Qt.AlignCenter)

        self.forecast = QtWidgets.QFrame(self.centralwidget)
        self.forecast.setGeometry(QtCore.QRect(0, 420, self.WIDTH, self.HEIGHT))
        self.forecast.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.forecast.setFrameShadow(QtWidgets.QFrame.Raised)
        self.forecast.setObjectName("forecast_label")

        self.frame1 = QtWidgets.QFrame(self.forecast)
        self.frame1.setGeometry(QtCore.QRect(0, 60, int(self.forecast.width() / 3), 400))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.frame1.setStyleSheet("border: 2px solid white")

        self.label1_1 = QtWidgets.QLabel(self.frame1)
        self.label1_1.setGeometry(QtCore.QRect(0, 0, self.frame1.width(), int(self.frame1.height() / 4)))
        self.label1_1.setObjectName("label1_1")
        self.label1_1.setFont(font4)
        self.label1_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_1.setStyleSheet("border-bottom: none;")

        self.label1_2 = QtWidgets.QLabel(self.frame1)
        self.label1_2.setGeometry(QtCore.QRect(0, int(self.frame1.height() / 4), self.frame1.width(), int(self.frame1.height() / 4)))
        self.label1_2.setObjectName("label1_2")
        self.pixmap2 = QtGui.QPixmap()
        self.label1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_2.setStyleSheet("border-top:none;border-bottom: none;")

        self.label1_3 = QtWidgets.QLabel(self.frame1)
        self.label1_3.setGeometry(QtCore.QRect(0, int(self.frame1.height() / 4 * 2), self.frame1.width(), int(self.frame1.height() / 4)))
        self.label1_3.setObjectName("label1_3")
        self.label1_3.setFont(font2)
        self.label1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_3.setStyleSheet("border-top:none;border-bottom: none;")

        self.label1_4 = QtWidgets.QLabel(self.frame1)
        self.label1_4.setGeometry(QtCore.QRect(0, int(self.frame1.height() / 4 * 3), self.frame1.width(), int(self.frame1.height() / 4)))
        self.label1_4.setObjectName("label1_4")
        self.label1_4.setFont(font4)
        self.label1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_4.setStyleSheet("border-top:none;")

        self.frame2 = QtWidgets.QFrame(self.forecast)
        self.frame2.setGeometry(QtCore.QRect(int(self.forecast.width() / 3), 60, int(self.forecast.width() / 3), 400))
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.frame2.setStyleSheet("border: 2px solid white")

        self.label2_1 = QtWidgets.QLabel(self.frame2)
        self.label2_1.setGeometry(QtCore.QRect(0, 0, self.frame2.width(), int(self.frame2.height() / 4)))
        self.label2_1.setObjectName("label2_1")
        self.label2_1.setFont(font4)
        self.label2_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_1.setStyleSheet("border-bottom: none;")

        self.label2_2 = QtWidgets.QLabel(self.frame2)
        self.label2_2.setGeometry(QtCore.QRect(0, int(self.frame2.height() / 4), self.frame2.width(), int(self.frame2.height() / 4)))
        self.label2_2.setObjectName("label2_2")
        self.pixmap3 = QtGui.QPixmap()
        self.label2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_2.setStyleSheet("border-top:none;border-bottom: none;")

        self.label2_3 = QtWidgets.QLabel(self.frame2)
        self.label2_3.setGeometry(QtCore.QRect(0, int(self.frame2.height() / 4 * 2), self.frame2.width(), int(self.frame2.height() / 4)))
        self.label2_3.setObjectName("label2_3")
        self.label2_3.setFont(font2)
        self.label2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_3.setStyleSheet("border-top:none;border-bottom: none;")

        self.label2_4 = QtWidgets.QLabel(self.frame2)
        self.label2_4.setGeometry(QtCore.QRect(0, int(self.frame2.height() / 4 * 3), self.frame2.width(), int(self.frame2.height() / 4)))
        self.label2_4.setObjectName("label2_4")
        self.label2_4.setFont(font4)
        self.label2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_4.setStyleSheet("border-top:none;")

        self.frame3 = QtWidgets.QFrame(self.forecast)
        self.frame3.setGeometry(QtCore.QRect(int(self.forecast.width() / 3 * 2), 60, int(self.forecast.width() / 3), 400))
        self.frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3.setObjectName("frame3")
        self.frame3.setStyleSheet("border: 2px solid white;")

        self.label3_1 = QtWidgets.QLabel(self.frame3)
        self.label3_1.setGeometry(QtCore.QRect(0, 0, self.frame3.width(), int(self.frame3.height() / 4)))
        self.label3_1.setObjectName("label3_1")
        self.label3_1.setFont(font4)
        self.label3_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_1.setStyleSheet("border-bottom: none;")
        
        self.label3_2 = QtWidgets.QLabel(self.frame3)
        self.label3_2.setGeometry(QtCore.QRect(0, int(self.frame3.height() / 4), self.frame3.width(), int(self.frame3.height() / 4)))
        self.label3_2.setObjectName("label3_2")
        self.pixmap4 = QtGui.QPixmap()
        self.label3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_2.setStyleSheet("border-top:none;border-bottom: none;")
        
        self.label3_3 = QtWidgets.QLabel(self.frame3)
        self.label3_3.setGeometry(QtCore.QRect(0, int(self.frame3.height() / 4 * 2), self.frame3.width(), int(self.frame3.height() / 4)))
        self.label3_3.setObjectName("label3_3")
        self.label3_3.setFont(font2)
        self.label3_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_3.setStyleSheet("border-top:none;border-bottom: none;")
        
        self.label3_4 = QtWidgets.QLabel(self.frame3)
        self.label3_4.setGeometry(QtCore.QRect(0, int(self.frame3.height() / 4 * 3), self.frame3.width(), int(self.frame3.height() / 4)))
        self.label3_4.setObjectName("label3_4")
        self.label3_4.setFont(font4)
        self.label3_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_4.setStyleSheet("border-top:none;")

        for i in [self.frame1, self.label1_1, self.label1_2, self.label1_3, self.label1_4, self.frame2, self.label2_1, self.label2_2, self.label2_3, self.label2_4, self.frame3, self.label3_1, self.label3_2, self.label3_3, self.label3_4]: i.hide()

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.location = ''; self.old_location = ''

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_label.setText("Enter a location : ")
        self.validate.setText("SEARCH")
        self.temp_f.setText("F")
        self.temp_c.setText("C")

    def request(self):
        self.location = self.search.text().capitalize()
        if self.location != self.old_location:
            r = requests.get('http://api.weatherapi.com/v1/forecast.json?key=0abae7750b5f49c58c8214425201908&q=' + self.location + '&days=6')
            if r:
                global infos
                infos = r.json()
                global infos_loc
                infos_loc = infos['location']
                global infos_curr
                infos_curr = infos['current']
                global infos_for
                infos_for = infos['forecast']

                if infos_curr['is_day']:
                    self.centralwidget.setStyleSheet("background-color: #3171af;color: #fff")
                    self.header.setStyleSheet("background-color: #0063b1;")
                    self.search.setStyleSheet("background-color: #31719b;padding-left: 10px;")
                    self.validate.setStyleSheet("background: #31719b;")
                elif not infos_curr['is_day']:
                    self.centralwidget.setStyleSheet("background-color: #132343;color: #fff")
                    self.header.setStyleSheet("background-color: #384052;")
                    self.search.setStyleSheet("background-color: #3f4554;padding-left: 10px;")
                    self.validate.setStyleSheet("background: #3f4554;")

                self.location_label.setText(self.location + ', ' + infos_loc['country'] + ' ' + infos_loc['localtime'].split()[1])
                self.pixmap1.loadFromData(urllib.request.urlopen('http:' + infos_curr['condition']['icon']).read())
                self.condition_icon.setPixmap(self.pixmap1)
                self.temp_label.setText(str(int(infos_curr['temp_f'])) + '°')
                self.temp_c.show()
                self.temp_f.show()
                self.condition_text.setText(infos_curr['condition']['text'])
                self.last_update_label.setText("Last update at " + infos_curr['last_updated'].split()[1])  
                for i in [self.frame1, self.label1_1, self.label1_2, self.label1_3, self.label1_4, self.frame2, self.label2_1, self.label2_2, self.label2_3, self.label2_4, self.frame3, self.label3_1, self.label3_2, self.label3_3, self.label3_4]: i.show()
                
                self.label1_1.setText(infos_for['forecastday'][0]['date']) 
                self.pixmap2.loadFromData(urllib.request.urlopen('http:' + infos_for['forecastday'][0]['day']['condition']['icon']).read())
                self.label1_2.setPixmap(self.pixmap2)
                self.label1_3.setText(str(int(infos_for['forecastday'][0]['day']['avgtemp_f'])) + '°')
                self.label1_4.setText(infos_for['forecastday'][0]['day']['condition']['text'])

                self.label2_1.setText(infos_for['forecastday'][1]['date']) 
                self.pixmap3.loadFromData(urllib.request.urlopen('http:' + infos_for['forecastday'][1]['day']['condition']['icon']).read())
                self.label2_2.setPixmap(self.pixmap3)
                self.label2_3.setText(str(int(infos_for['forecastday'][1]['day']['avgtemp_f'])) + '°')
                self.label2_4.setText(infos_for['forecastday'][1]['day']['condition']['text'])

                self.label3_1.setText(infos_for['forecastday'][2]['date']) 
                self.pixmap4.loadFromData(urllib.request.urlopen('http:' + infos_for['forecastday'][2]['day']['condition']['icon']).read())
                self.label3_2.setPixmap(self.pixmap4)
                self.label3_3.setText(str(int(infos_for['forecastday'][2]['day']['avgtemp_f'])) + '°')
                self.label3_4.setText(infos_for['forecastday'][2]['day']['condition']['text'])

                self.old_location = self.location

    def print_temp_f(self):
        if not self.temp_f_active:
            self.temp_label.setText(str(int(infos_curr['temp_f'])) + '°')
            self.label1_3.setText(str(int(infos_for['forecastday'][0]['day']['avgtemp_f'])) + '°')
            self.label2_3.setText(str(int(infos_for['forecastday'][1]['day']['avgtemp_f'])) + '°')
            self.label3_3.setText(str(int(infos_for['forecastday'][2]['day']['avgtemp_f'])) + '°')
            self.temp_f_active = True
            self.temp_c_active = False

    def print_temp_c(self):
        if not self.temp_c_active:
            self.temp_label.setText(str(int(infos_curr['temp_c'])) + '°')
            self.label1_3.setText(str(int(infos_for['forecastday'][0]['day']['avgtemp_c'])) + '°')
            self.label2_3.setText(str(int(infos_for['forecastday'][1]['day']['avgtemp_c'])) + '°')
            self.label3_3.setText(str(int(infos_for['forecastday'][2]['day']['avgtemp_c'])) + '°')
            self.temp_c_active = True
            self.temp_f_active = False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
