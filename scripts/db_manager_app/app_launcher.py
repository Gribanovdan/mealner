from PyQt5.QtWidgets import *
import sys
import pyautogui as pgui
from PyQt5.QtCore import pyqtSlot, QTimer
from time import sleep

import scripts.db.dblauncher as db
import scripts.db.dbfiller as filler
import scripts.entities.main_entities as ent
import scripts.logs.log_manager as lg


class MainWindow(QMainWindow):  # главное окно
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Mealner DB Manager")  # заголовок окна
        screen_width = pgui.size().width
        screen_height = pgui.size().height
        width = 1000
        height = 500
        self.move(screen_width // 2 - width // 2, screen_height // 2 - height // 2)
        self.setFixedSize(width, height)

        # ---------------------------------[1]---------------------------------------

        # первая колонка (+30)
        h1 = 10
        self.lbl1 = QLabel('<b>Добавить продукт</b>', self)
        self.lbl1.adjustSize()
        self.lbl1.move(1 * width // 8 - self.lbl1.width() // 2, h1)

        h1 += 30
        self.lbl11 = QLabel('Название продукта', self)
        self.lbl11.adjustSize()
        self.lbl11.move(1 * width // 8 - self.lbl11.width() // 2, h1)
        self.txtbox11 = QLineEdit(self)
        self.txtbox11.resize(150, 25)
        h1 += 20
        self.txtbox11.move(1 * width // 8 - self.txtbox11.width() // 2, h1)

        h1 += 30
        self.lbl12 = QLabel('Цена', self)
        self.lbl12.adjustSize()
        self.lbl12.move(1 * width // 8 - self.lbl12.width() // 2, h1)
        self.txtbox12 = QLineEdit(self)
        self.txtbox12.resize(150, 25)
        h1 += 20
        self.txtbox12.move(1 * width // 8 - self.txtbox12.width() // 2, h1)

        h1 += 30
        self.lbl13 = QLabel('Ккалории', self)
        self.lbl13.adjustSize()
        self.lbl13.move(1 * width // 8 - self.lbl13.width() // 2, h1)
        self.txtbox13 = QLineEdit(self)
        self.txtbox13.resize(150, 25)
        h1 += 20
        self.txtbox13.move(1 * width // 8 - self.txtbox13.width() // 2, h1)

        h1 += 30
        self.lbl14 = QLabel('Белки', self)
        self.lbl14.adjustSize()
        self.lbl14.move(1 * width // 8 - self.lbl14.width() // 2, h1)
        self.txtbox14 = QLineEdit(self)
        self.txtbox14.resize(150, 25)
        h1 += 20
        self.txtbox14.move(1 * width // 8 - self.txtbox14.width() // 2, h1)

        h1 += 30
        self.lbl15 = QLabel('Жиры', self)
        self.lbl15.adjustSize()
        self.lbl15.move(1 * width // 8 - self.lbl15.width() // 2, h1)
        self.txtbox15 = QLineEdit(self)
        self.txtbox15.resize(150, 25)
        h1 += 20
        self.txtbox15.move(1 * width // 8 - self.txtbox15.width() // 2, h1)

        h1 += 30
        self.lbl16 = QLabel('Углеводы', self)
        self.lbl16.adjustSize()
        self.lbl16.move(1 * width // 8 - self.lbl16.width() // 2, h1)
        self.txtbox16 = QLineEdit(self)
        self.txtbox16.resize(150, 25)
        h1 += 20
        self.txtbox16.move(1 * width // 8 - self.txtbox16.width() // 2, h1)

        h1 += 30
        self.lbl17 = QLabel('Тип измерения', self)
        self.lbl17.adjustSize()
        self.lbl17.move(1 * width // 8 - self.lbl17.width() // 2, h1)
        self.combobox1 = QComboBox(self)
        self.combobox1.addItems(['100 гр', '1 литр', '1 шт'])
        h1 += 20
        self.combobox1.move(1 * width // 8 - self.combobox1.width() // 2, h1)

        h1 += 50
        self.btn1 = QPushButton(self)
        self.btn1.setText('Отправить')
        self.btn1.move(1 * width // 8 - self.btn1.width() // 2, h1)
        self.btn1.clicked.connect(self.btn1_click)

        h1 += 50
        self.status_lbl1 = QLabel('', self)
        self.status_lbl1.move(1 * width // 8 - self.btn1.width() // 2, h1)

        # ------------------------------[2]----------------------------------

        # вторая колонка
        h2 = 10

        self.lbl2 = QLabel('<b>Обновить продукт</b>', self)
        self.lbl2.adjustSize()
        self.lbl2.move(3 * width // 8 - self.lbl2.width() // 2, h2)

        h2 += 30
        self.btn21 = QPushButton(self)
        self.btn21.setText('Подключиться к бд')
        self.btn21.adjustSize()
        self.btn21.move(3 * width // 8 - self.btn21.width() // 2, h2)
        self.btn21.clicked.connect(self.btn21_click)

        h2 += 30
        self.cmbbx21 = QComboBox(self)
        self.cmbbx21.addItem('...', -1)
        self.cmbbx21.move(3 * width // 8 - self.cmbbx21.width() // 2, h2)
        self.cmbbx21.currentTextChanged.connect(self.cmbbox21_choice)

        h2 += 40
        self.lbl21 = QLabel('Продукт', self)
        self.lbl21.adjustSize()
        self.lbl21.move(5 * width // 16 - self.lbl21.width() // 2, h2)

        self.lbl22 = QLabel('Цена', self)
        self.lbl22.adjustSize()
        self.lbl22.move(7 * width // 16 - self.lbl22.width() // 2, h2)

        h2 += 20
        self.txtbox21 = QLineEdit(self)
        self.txtbox21.resize(100, 25)
        self.txtbox21.move(5 * width // 16 - self.txtbox21.width() // 2, h2)

        self.txtbox22 = QLineEdit(self)
        self.txtbox22.resize(100, 25)
        self.txtbox22.move(7 * width // 16 - self.txtbox22.width() // 2, h2)

        h2 += 30
        self.lbl23 = QLabel('Ккалории', self)
        self.lbl23.adjustSize()
        self.lbl23.move(5 * width // 16 - self.lbl23.width() // 2, h2)

        self.lbl24 = QLabel('Белки', self)
        self.lbl24.adjustSize()
        self.lbl24.move(7 * width // 16 - self.lbl24.width() // 2, h2)

        h2 += 20
        self.txtbox23 = QLineEdit(self)
        self.txtbox23.resize(100, 25)
        self.txtbox23.move(5 * width // 16 - self.txtbox23.width() // 2, h2)

        self.txtbox24 = QLineEdit(self)
        self.txtbox24.resize(100, 25)
        self.txtbox24.move(7 * width // 16 - self.txtbox24.width() // 2, h2)

        h2 += 30
        self.lbl25 = QLabel('Жиры', self)
        self.lbl25.adjustSize()
        self.lbl25.move(5 * width // 16 - self.lbl25.width() // 2, h2)

        self.lbl26 = QLabel('Углеводы', self)
        self.lbl26.adjustSize()
        self.lbl26.move(7 * width // 16 - self.lbl26.width() // 2, h2)

        h2 += 20
        self.txtbox25 = QLineEdit(self)
        self.txtbox25.resize(100, 25)
        self.txtbox25.move(5 * width // 16 - self.txtbox25.width() // 2, h2)

        self.txtbox26 = QLineEdit(self)
        self.txtbox26.resize(100, 25)
        self.txtbox26.move(7 * width // 16 - self.txtbox26.width() // 2, h2)

        h2 += 30
        self.lbl27 = QLabel('Тип измерения', self)
        self.lbl27.adjustSize()
        self.lbl27.move(3 * width // 8 - self.lbl27.width() // 2, h2)
        h2 += 20
        self.cmbbx22 = QComboBox(self)
        self.cmbbx22.move(3 * width // 8 - self.cmbbx21.width() // 2, h2)
        self.cmbbx22.addItems(['100 гр', '1 литр', '1 шт'])

        h2 += 50
        self.btn22 = QPushButton('Обновить', self)
        self.btn22.adjustSize()
        self.btn22.move(3 * width // 8 - self.btn22.width() // 2, h2)
        self.btn22.clicked.connect(self.btn22_click)

        h2 += 50
        self.btn23 = QPushButton('Удалить', self)
        self.btn23.adjustSize()
        self.btn23.move(3 * width // 8 - self.btn23.width() // 2, h2)
        self.btn23.clicked.connect(self.btn23_click)
        self.btn23.setStyleSheet('background-color: #ff7a66')

        # ----------------------------[3]---------------------------

        # третья колонка
        self.lbl3 = QLabel('<b>Добавить блюдо</b>', self)
        self.lbl3.adjustSize()
        self.lbl3.move(5 * width // 8 - self.lbl3.width() // 2, 10)

        # четвертая колонка
        self.lbl4 = QLabel('<b>Обновить блюдо</b>', self)
        self.lbl4.adjustSize()
        self.lbl4.move(7 * width // 8 - self.lbl4.width() // 2, 10)

    @pyqtSlot()
    def btn1_click(self):
        name = self.txtbox11.text()
        price = self.txtbox12.text()
        kkalories = self.txtbox13.text()
        protein = self.txtbox14.text()
        fats = self.txtbox15.text()
        carbohydrates = self.txtbox16.text()
        measure = self.combobox1.currentText()

        def check(obj, clas):
            try:
                clas(obj)
            except:
                return False
            return True

        ok = True
        if name == '':
            ok = False
        if not check(price, int) or price == '':
            ok = False
        if not check(kkalories, int) or kkalories == '':
            ok = False
        if not check(protein, float) or protein == '':
            ok = False
        if not check(fats, float) or fats == '':
            ok = False
        if not check(carbohydrates, float) or carbohydrates == '':
            ok = False
        if measure == '':
            ok = False
        if not ok:
            self.status_lbl1.setText('Ошибка ввода')
            self.status_lbl1.adjustSize()
            return
        else:
            self.status_lbl1.setText('Ввод успешно')
            self.status_lbl1.adjustSize()

        try:
            db.launch()
        except:
            self.status_lbl1.setText('Ошибка подключения к бд')
            self.status_lbl1.adjustSize()
            return
        conn = db.DBInfo.connection

        product = ent.Creator.create_product(name, int(price), int(kkalories), float(protein), float(fats),
                                             float(carbohydrates), ent.MeasureType.get_measure_type(measure))
        lg.log(f'{product.name} product created. sending...', 20)
        # TODO проверка на совпадение имени продукта в базе данных

        code = filler.insert_product(product)
        lg.log('insert_product finished with' + 'error' if code is None else 'success', 20)

        if code is None:
            self.status_lbl1.setText('Ошибка во время отправки запроса')
            self.status_lbl1.adjustSize()
            return

        self.status_lbl1.setText('Успешно!')
        self.status_lbl1.adjustSize()
        self.status_lbl1.show()

        def on_timeout():
            self.txtbox11.setText('')
            self.txtbox12.setText('')
            self.txtbox13.setText('')
            self.txtbox14.setText('')
            self.txtbox15.setText('')
            self.txtbox16.setText('')
            self.status_lbl1.setText('')

        timer = QTimer(self)
        timer.timeout.connect(on_timeout)
        timer.start(1000)

    def errormsg(self):
        dlg = QDialog(self)
        dlg.setWindowTitle('Ошибка')
        dlg.label = QLabel(dlg)
        dlg.label.setText('Ошибка!')
        dlg.label.move(70, 40)
        dlg.setFixedSize(200, 100)
        dlg.exec()

    @pyqtSlot()
    def btn21_click(self):
        try:
            db.launch()
        except:
            self.errormsg()
            return

        conn = db.DBInfo.connection
        cur = conn.cursor()

        try:
            q = 'select * from main.product;'
            cur.execute(q)
            res = cur.fetchall()
        except Exception as err:
            self.errormsg()
            lg.log(str(err), 40)
            return
        lg.log('connection succeeded (update product route)', 20)

        self.products = {}
        for info in res:
            pr = ent.Creator.create_product(*(info[1:]))
            self.products[info[0]] = pr
        lg.log('products added to local db', 20)

        self.cmbbx21.clear()
        for id, pr in self.products.items():
            self.cmbbx21.addItem(f'{pr.name}', id)

        lg.log('products added to combobox', 20)

        return True

    @pyqtSlot()
    def btn22_click(self):
        id = self.cmbbx21.currentData()
        name = self.txtbox21.text()
        price = self.txtbox22.text()
        kkalories = self.txtbox23.text()
        protein = self.txtbox24.text()
        fats = self.txtbox25.text()
        carbohydrates = self.txtbox26.text()
        measure = self.cmbbx22.currentText()

        def check(obj, clas):
            try:
                clas(obj)
            except:
                return False
            return True

        ok = True
        if not check(id, int) or id == '':
            ok = False
        if name == '':
            ok = False
        if not check(price, int) or price == '':
            ok = False
        if not check(kkalories, int) or kkalories == '':
            ok = False
        if not check(protein, float) or protein == '':
            ok = False
        if not check(fats, float) or fats == '':
            ok = False
        if not check(carbohydrates, float) or carbohydrates == '':
            ok = False
        if measure == '':
            ok = False
        if not ok:
            lg.log('wrong type', 30)
            self.errormsg()
            return
        # TODO подключение к бд, обновление

    @pyqtSlot()
    def btn23_click(self):
        print('удалить')
        # TODO
        pass

    @pyqtSlot()
    def cmbbox21_choice(self):
        if self.cmbbx21.currentText() == '':
            return
        try:
            id = self.cmbbx21.currentData()
            pr = self.products[id]

            self.txtbox21.setText(pr.name)
            self.txtbox22.setText(str(pr.cost))
            self.txtbox23.setText(str(pr.kkalories))
            self.txtbox24.setText(str(pr.protein))
            self.txtbox25.setText(str(pr.fats))
            self.txtbox26.setText(str(pr.carbohydrates))
            self.cmbbx22.setCurrentText(str(pr.measure))
        except Exception as err:
            lg.log(str(err), 40)
            self.errormsg()
            return None
        lg.log('item selected', 20)
        return True

def launch():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    launch()
