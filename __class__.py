import os
import shutil
import time
from PyQt5.QtWidgets import *


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.srcDir = 'C:\\Users\\yune8\\Downloads'
        self.word_file = 'C:\\Users\\yune8\\OneDrive\\문서\\워드자료'
        self.picture_file = 'C:\\Users\\yune8\\OneDrive\\문서\\사진'
        self.ppt_file = 'C:\\Users\\yune8\\OneDrive\\문서\\PPT'
        self.zip_file = 'C:\\Users\\yune8\\OneDrive\\문서\\압축파일'
        self.pdf_file = 'C:\\Users\\yune8\\OneDrive\\문서\\pdf'
        self.else_file = 'C:\\Users\\yune8\\OneDrive\\문서\\기타'
        self.btnClss = QPushButton("파일분류")
        self.btnDel = QPushButton("파일들 지우기")
        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)
        self.setUi()
        self.setSlot()

    def setUi(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("파일들 정리하기")

        vbox = QVBoxLayout()
        vbox.addWidget(self.btnClss, 0)
        vbox.addWidget(self.btnDel, 1)
        vbox.addWidget(self.tb, 2)
        self.setLayout(vbox)

    def setSlot(self):
        self.btnClss.clicked.connect(self.classify)
        self.btnDel.clicked.connect(self.delete)

    def classify(self):
        if os.listdir(self.srcDir):
            for file in os.listdir(self.srcDir):
                if file.endswith(".docx") or file.endswith(".hwp"):
                    if file not in os.listdir(self.word_file):
                        shutil.copy(self.srcDir + '\\' + file, self.word_file)
                        self.tb.append(file + "(이)가 \'워드파일\' 파일에 정리되었습니다." + time.strftime('%y-%m-%d %H:%M:%S'))
                    else:
                        self.tb.append(f"{file}(은)는 이미 정리되었습니다.")

                elif file.endswith(".jpg") or file.endswith(".png"):
                    if file not in os.listdir(self.picture_file):
                        shutil.copy(self.srcDir + '\\' + file, self.picture_file)
                        self.tb.append(file + "(이)가 사진 파일에 정리되었습니다." + time.strftime('%y-%m-%d %H:%M:%S'))
                    else:
                        self.tb.append(f"{file}(은)는 이미 정리되었습니다.")

                elif file.endswith(".pptx"):
                    if file not in os.listdir(self.ppt_file):
                        shutil.copy(self.srcDir + '\\' + file, self.ppt_file)
                        self.tb.append(file + "(이)가 PPT 파일에 정리되었습니다." + time.strftime('%y-%m-%d %H:%M:%S'))
                    else:
                        self.tb.append(f"{file}(은)는 이미 정리되었습니다.")

                elif file.endswith(".pdf"):
                    if file not in os.listdir(self.pdf_file):
                        shutil.copy(self.srcDir + '\\' + file, self.pdf_file)
                        self.tb.append(file + "(이)가 pdf 파일에 정리되었습니다." + time.strftime('%y-%m-%d %H:%M:%S'))
                    else:
                        self.tb.append(f"{file}(은)는 이미 정리되었습니다.")

                elif file.endswith(".zip"):
                    if file not in os.listdir(self.zip_file):
                        shutil.copy(self.srcDir + '\\' + file, self.zip_file)
                        self.tb.append(file + "(이)가 \'압축파일\' 파일에 정리되었습니다." + time.strftime('%y-%m-%d %H:%M:%S'))
                    else:
                        self.tb.append(f"{file}(은)는 이미 정리되었습니다.")

                else:
                    if file not in os.listdir(self.else_file):
                        shutil.copy(self.srcDir + '\\' + file, self.else_file)
                        self.tb.append(file + "(이)가 기타 파일에 정리되었습니다." + time.strftime('%y-%m-%d %H:%M:%S'))
                    else:
                        self.tb.append(f"{file}(은)는 이미 정리되었습니다.")
        else:
            self.tb.append("텅 비었습니다.")

    def delete(self):
        if os.listdir(self.srcDir):
            for file in os.listdir(self.srcDir):
                if os.path.isfile(self.srcDir + '\\' + file):
                    os.remove(self.srcDir + '\\' + file)
                    self.tb.append(f"{file}(을)를 삭제했습니다.")

        else:
            self.tb.append("텅 비었습니다.")




