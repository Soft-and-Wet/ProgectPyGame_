import sys


from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QFont, QIcon

# некоторые комментарии разумно было бы оставить, все равно подписывать потом
# ЕСЛИ ЭТО СРАБОТАЕТ БЕЗ СБОЯ ОСТАЛЬНЫХ НАСТРОЕК (ЦВЕТ ШРИФТА НАПРИМЕР) ТО ПОПРОБУЙ:
# self.btn_кнопка.setFont(QFont("Times", 12)) попробуй таймс убрать. а еще лучше посмотри
# как менять размер с .setStyleSheet(""" """)


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.background = QLabel(self)
        self.im_background = QPixmap("sw_pic/menu/menu.png")

        # запуск игры

        self.btn_play = QPushButton('', self)

        # звук

        self.btn_vol_plus = QPushButton('', self)
        self.btn_vol_minus = QPushButton('', self)

        # наверное в зависимости от уровня звука будет меняться картинка (или просто цифры красиво выведи)

        self.text_volume = QLabel(self)

        self.lvl_volume = [0, 0.25, 0.5, 0.75, 1]

        # управление

        self.text_settings = QLabel(self)

        self.initUI()

    def initUI(self):

        # окно

        self.setGeometry(500, 500, 768, 432)
        self.setWindowTitle('SW game menu')

        # фон

        self.background.move(0, 0)
        self.background.resize(768, 432)
        self.background.setPixmap(self.im_background)

        # кнопки
        # играть

        self.btn_play.setIcon(QIcon('sw_pic/menu/16119774.png'))
        self.btn_play.setIconSize(QSize(75, 75))
        # РАЗМЕР ЗАМЕНИТЬ НА РАЗМЕР КАРТИНКИ
        self.btn_play.adjustSize()
        self.btn_play.setStyleSheet("""
            QPushButton {background-color: rgb(51,122,183);}
        """)
        # СКАЗАТЬ МНЕ СКАЗАТЬ ТЕБЕ ЦВЕТ ФОНА!!!!!!!!!!!!! ВСТАВИТЬ ВЫШЕ (и в дальнейшем)
        self.btn_play.move(350, 250)
        self.btn_play.clicked.connect(self.startPlay)

        # звук

        self.btn_vol_plus.setIcon(QIcon('sw_pic/menu/16119774.png'))
        self.btn_vol_plus.setIconSize(QSize(15, 15))
        # РАЗМЕР ЗАМЕНИТЬ НА РАЗМЕР КАРТИНКИ
        self.btn_vol_plus.adjustSize()
        self.btn_vol_plus.setStyleSheet("""
                    QPushButton {background-color: rgb(51,122,183);}
                """)
        # СКАЗАТЬ МНЕ СКАЗАТЬ ТЕБЕ ЦВЕТ ФОНА!!!!!!!!!!!!! ВСТАВИТЬ ВЫШЕ (и в дальнейшем)
        self.btn_vol_plus.move(100, 225)
        self.btn_vol_plus.clicked.connect(self.startPlay)

        #

        self.btn_vol_minus.setIcon(QIcon('sw_pic/menu/16119774.png'))
        self.btn_vol_minus.setIconSize(QSize(15, 15))
        # РАЗМЕР ЗАМЕНИТЬ НА РАЗМЕР КАРТИНКИ
        self.btn_vol_minus.adjustSize()
        self.btn_vol_minus.setStyleSheet("""
                            QPushButton {background-color: rgb(51,122,183);}
                        """)
        # СКАЗАТЬ МНЕ СКАЗАТЬ ТЕБЕ ЦВЕТ ФОНА!!!!!!!!!!!!! ВСТАВИТЬ ВЫШЕ (и в дальнейшем)
        self.btn_vol_minus.move(150, 225)
        self.btn_vol_minus.clicked.connect(self.startPlay)

        # текст управления / правил

        self.text_settings.move(600, 200)
        self.text_settings.setText("Инструкция:\nкаво\nчево")
        self.text_settings.setStyleSheet("""
            font: times;
            color: white;
            background-color: none;
        """)
        # НАЙДИ КАК ЭТОЙ ХРЕНЬЮ РАЗМЕР ШРИФТА МЕНЯТЬ А ТО Я БОЧОНОК
        self.text_settings.adjustSize()

        # возможно заменить картинкой а может и нет..

        self.text_volume.move(100, 200)
        self.text_volume.setText("Громкость:")
        self.text_volume.setStyleSheet("""
                    font: times;
                    color: white;
                    background-color: none;
                """)
        # НАЙДИ КАК ЭТОЙ ХРЕНЬЮ РАЗМЕР ШРИФТА МЕНЯТЬ А ТО Я БОЧОНОК (и жирность не момешает)
        self.text_volume.adjustSize()

    # перенос настроек в игру + закрытие меню и запуск игры
    def startPlay(self):

        pass

    # работа со звуком

    def vol_plus(self):

        pass

    def vol_minus(self):

        pass

    # НАВЕРНОЕ РАЗУМНО БУДЕТ ЕСЛИ КАЖДАЯ ФУНКЦИЯ ВЫЗЫВАТЬ функцию ДЛЯ СОХРАНЕНИЯ РЕЗУЛЬТАТОВ,
    # НО КАК ТЫ предпочтешь сделать Я НЕ ЗНАЮ


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec())