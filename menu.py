import os
import sys
from music import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QToolButton
from PyQt5.QtGui import QPixmap, QFont, QIcon


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.background = QLabel(self)
        self.im_background = QPixmap("sw_pic/menu/menu.png")

        # запуск игры

        self.btn_play = QToolButton(self)

        # звук

        self.btn_vol_plus = QToolButton(self)
        self.btn_vol_minus = QToolButton(self)

        self.s_lvl_volume = [[0, 'sw_pic/menu/vol_lvl_0'],
                             [2, 'sw_pic/menu/vol_lvl_1'],
                             [4, 'sw_pic/menu/vol_lvl_2'],
                             [6, 'sw_pic/menu/vol_lvl_3'],
                             [8, 'sw_pic/menu/vol_lvl_4'],
                             [10, 'sw_pic/menu/vol_lvl_5']]
        self.lvl_volume = 6

        self.volume = QLabel(self)

        # управление

        self.text_settings = QLabel(self)

        self.initUI()

    def initUI(self):

        pygame.mixer.music.play()

        # окно

        self.setGeometry(500, 500, 768, 432)
        self.setWindowTitle('SW game menu')

        # фон

        self.background.move(0, 0)
        self.background.resize(768, 432)
        self.background.setPixmap(self.im_background)

        # кнопки
        # играть

        self.btn_play.setIcon(QIcon('sw_pic/menu/but_play.png'))
        self.btn_play.setAutoRaise(True)
        self.btn_play.setMinimumSize(113, 43)
        self.btn_play.setIconSize(self.btn_play.minimumSize())
        self.btn_play.adjustSize()
        self.btn_play.move(325, 227)
        self.btn_play.clicked.connect(self.startPlay)

        # звук

        self.btn_vol_plus.setIcon(QIcon('sw_pic/menu/vol_plus.png'))
        self.btn_vol_plus.setAutoRaise(True)
        self.btn_vol_plus.setMinimumSize(55, 50)
        self.btn_vol_plus.setIconSize(self.btn_vol_plus.minimumSize())
        self.btn_vol_plus.adjustSize()
        self.btn_vol_plus.move(172, 180)
        self.btn_vol_plus.clicked.connect(self.vol_plus)

        #

        self.btn_vol_minus.setIcon(QIcon('sw_pic/menu/vol_minus.png'))
        self.btn_vol_minus.setAutoRaise(True)
        self.btn_vol_minus.setMinimumSize(71, 77)
        self.btn_vol_minus.setIconSize(self.btn_vol_minus.minimumSize())
        self.btn_vol_minus.adjustSize()
        self.btn_vol_minus.move(95, 167)
        self.btn_vol_minus.clicked.connect(self.vol_minus)

        # текст управления / правил

        self.text_settings.move(535, 190)
        self.text_settings.setText("Как играть:\n\n [w][a][s][d] - движение\n\n[mouse left] - взаимодействие")
        self.text_settings.setStyleSheet("""
            font: times;
            color: white;
            background-color: none;
        """)
        self.text_settings.adjustSize()

        self.level_volume()

    # перенос настроек в игру + закрытие меню и запуск игры
    def startPlay(self):

        pygame.mixer.music.stop()
        os.system('python glav.py')
        #sys.exit()

        pass

    # работа со звуком

    def level_volume(self):

        pygame.mixer.music.set_volume(self.lvl_volume / 10)

        for i in range(6):
            if self.s_lvl_volume[i][0] == self.lvl_volume:
                self.im_volume = QPixmap(self.s_lvl_volume[i][1])
                self.volume.move(107, 235)
                self.volume.resize(122, 30)
                self.volume.setPixmap(self.im_volume)

    def vol_plus(self):
        if self.lvl_volume < 10:
            self.lvl_volume += 2

        self.level_volume()

    def vol_minus(self):
        if self.lvl_volume > 0:
            self.lvl_volume -= 2

        self.level_volume()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec())
