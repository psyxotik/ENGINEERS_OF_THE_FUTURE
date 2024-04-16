from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MathQuizApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('math_question.ui', self)
        self.setWindowTitle('Пример')
        self.pushButton.clicked.connect(self.check_answer)
        self.difficulty = 0
        self.generate_question()
        self.ammo = 0


    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def generate_question(self):
        # Генерируем два случайных числа
        print('check')
        if self.difficulty % 3 == 0:
            print('easy')
            digits = ['+', '-']
            digit = randint(0, 1)
            cur_digit = digits[digit]
            if cur_digit == '+':
                self.num1 = randint(1, 100)
                self.num2 = randint(1, 10)
                self.correct_answer = self.num1 + self.num2
            elif cur_digit == '-':
                self.num1 = randint(1, 100)
                self.num2 = randint(1, 10)
                self.correct_answer = self.num1 - self.num2
        elif self.difficulty % 3 == 1:
            print('medium')
            digits = ['+', '-', '+', '-']
            digit = randint(0, 3)
            cur_digit = digits[digit]
            if cur_digit == '+':
                self.num1 = randint(1, 100)
                self.num2 = randint(1, 100)
                self.correct_answer = self.num1 + self.num2
            elif cur_digit == '-':
                self.num1 = randint(1, 100)
                self.num2 = randint(1, 100)
                self.correct_answer = self.num1 - self.num2
            elif cur_digit == ':':
                self.num1 = randint(1, 100)
                self.num2 = randint(1, 10)
                while self.num1 % self.num2 != 0:
                    self.num1 = randint(1, 100)
                    self.num2 = randint(1, 10)
                self.correct_answer = self.num1 // self.num2
            elif cur_digit == '*':
                self.num1 = randint(1, 10)
                self.num2 = randint(1, 10)
                self.correct_answer = self.num1 * self.num2
        else:
            print('hard')
            digits = ['+', '-', '+', '-']
            digit = randint(0, 3)
            cur_digit = digits[digit]
            if cur_digit == '+':
                self.num1 = randint(100, 1000)
                self.num2 = randint(100, 1000)
                self.correct_answer = self.num1 + self.num2
            elif cur_digit == '-':
                self.num1 = randint(100, 1000)
                self.num2 = randint(100, 1000)
                self.correct_answer = self.num1 - self.num2
            elif cur_digit == ':':
                self.num1 = randint(10, 100)
                self.num2 = randint(1, 10)
                while self.num1 % self.num2 != 0:
                    self.num1 = randint(1, 100)
                    self.num2 = randint(1, 10)
                self.correct_answer = self.num1 // self.num2
            elif cur_digit == '*':
                self.num1 = randint(1, 100)
                self.num2 = randint(1, 10)
                self.correct_answer = self.num1 * self.num2

        question = f"{self.num1} {cur_digit} {self.num2} = ?"
        self.label.setText(question)

        # Запоминаем правильный ответ

    def check_answer(self):
        # Получаем ответ пользователя
        user_answer = self.spinBox.value()

        # Проверяем ответ
        if user_answer == self.correct_answer:
            print("Правильно!")
            self.ammo = 10
            self.close()
        else:
            print("Неправильно. Попробуйте еще раз.")
            # Генерируем новый вопрос
            self.label_2.setText('Неправильно')
            self.generate_question()
            self.ammo = 0


def math_quiz(difficulty):
    app = QApplication(sys.argv)
    quiz_app = MathQuizApp()
    quiz_app.set_difficulty(difficulty)
    quiz_app.show()
    app.exec_()
    return quiz_app.ammo



