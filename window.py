
from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MathQuizApp(QMainWindow):
    def __init__(self, ammo):
        super().__init__()
        uic.loadUi('math_question.ui', self)
        self.setWindowTitle('Пример')
        self.ammo = ammo
        self.pushButton.clicked.connect(self.check_answer)
        self.generate_question()


    def generate_question(self):
        # Генерируем два случайных числа
        digits = ['+', '-', ':', '*']
        digit = randint(0, 3)
        cur_digit = digits[digit]
        if cur_digit == '+':
            num1 = randint(1, 1000)
            num2 = randint(1, 1000)
            self.correct_answer = num1 + num2
        elif cur_digit == '-':
            num1 = randint(1, 1000)
            num2 = randint(1, 1000)
            self.correct_answer = num1 - num2
        elif cur_digit == ':':
            num1 = randint(1, 100)
            num2 = randint(1, 10)
            while num1 % num2 != 0:
                num1 = randint(1, 100)
                num2 = randint(1, 10)
            self.correct_answer = num1 // num2
        elif cur_digit == '*':
            num1 = randint(1, 20)
            num2 = randint(1, 20)
            self.correct_answer = num1 * num2

        question = f"{num1} {cur_digit} {num2} = ?"
        self.label.setText(question)

        # Запоминаем правильный ответ


    def check_answer(self):
        # Получаем ответ пользователя
        user_answer = self.spinBox.value()

        # Проверяем ответ
        if user_answer == self.correct_answer:
            print("Правильно!")
            self.ammo = 3
            self.close()
        else:
            print("Неправильно. Попробуйте еще раз.")
            # Генерируем новый вопрос
            self.generate_question()


def math_quiz(ammo):
    app = QApplication(sys.argv)
    quiz_app = MathQuizApp(ammo)
    quiz_app.show()
    app.exec_()