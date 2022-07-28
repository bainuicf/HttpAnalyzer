'''
@文件    :main.py
@说明    :
@时间    :2022/07/20 15:31:02
@作者    :ShellC
@版本    :1.0.0.220726
'''

#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import json
import sys
from urllib import response
import requests
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
# 1.调用UI.py
from UI import *


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'
}


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 两种方式调用ui界面
        # ******
        # 1.调用UI.py
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 2.调用UI.ui
        # self.ui = QUiLoader().load('UI.ui')

        self.ui.buttonAnylast.clicked.connect(self.buttonAnylast_click)

    def buttonAnylast_click(self):
        url = self.ui.inputURL.text()
        method = self.ui.inputMethod.currentText()
        options = self.ui.inputOpt.toPlainText()
        if options!="":
            headers= formatOpts(options)
            HEADERS.update(headers)
        response= httpAnalyst(url, method, HEADERS)
        self.ui.inputResult.setPlainText(response)


# 发起http请求函数
def httpAnalyst(url, method, headers):
    if method == "GET":
        result = requests.get(url, headers)
    elif method == "POST":
        result = requests.post(url, headers)
    result.encoding= 'UTF-8'
    return(result.text)

def formatOpts(option):
    header={}
    a= option.split('\n')
    for i in a:
        if i!= '':
            b= i.split(':', 1)
            header[b[0]]=[1]
    return(header)

if __name__ == '__main__':

    app = QApplication([])
    gui = MainWidget()

    # 1.调用UI.py
    gui.show()

    # 2.调用UI.ui
    # gui.ui.show()

    sys.exit(app.exec())
