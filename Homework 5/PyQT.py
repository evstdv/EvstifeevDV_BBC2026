import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QFrame, QLineEdit, QPushButton, QComboBox, QMessageBox
)
from PyQt6.QtCore import Qt

class BottomPanel(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(160)
        self.setStyleSheet("""
            BottomPanel {
                background-color: #00008b;
                border-radius: 18px
            }
        """)

        label = QLabel("КАЛЕНДАРЬ", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet(
            "background: transparent;"
            "color: white;"
            "font-size: 72px;"
            "font-weight: 900;"
            "letter-spacing: 8px;"
        )

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.addWidget(label)

        self.hide()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ввод данных")
        self.setStyleSheet("background-color: #f4f6f8;")

        field_style = (
            "font-size: 18px; padding: 4px 12px;"
            "background: white; color: #333;"
            "border: 2px solid #c0c8d0; border-radius: 10px;"
        )
        combo_style = (
            "QComboBox {"
            "  font-size: 18px; padding: 4px 12px;"
            "  background: white; color: #333;"
            "  border: 2px solid #c0c8d0; border-radius: 10px;"
            "}"
            "QComboBox::drop-down {"
            "  width: 30px; border: none;"
            "}"
            "QComboBox QAbstractItemView {"
            "  font-size: 16px;"
            "  background: white; color: #333;"
            "}"
        )

        # 1) Поле для ввода 1
        self.field_top = QLineEdit(self)
        self.field_top.setPlaceholderText("Введите номер карты")
        self.field_top.setFixedHeight(50)
        self.field_top.setStyleSheet(field_style)

        # 2) Выпадающий список 1
        self.combo_left = QComboBox(self)
        self.combo_left.addItems([str(i) if i >= 10 else '0' + str(i) for i in range(1, 32)])
        self.combo_left.setFixedHeight(50)
        self.combo_left.setStyleSheet(combo_style)
        # 3) Выпадающий список 2
        self.combo_right = QComboBox(self)
        self.combo_right.addItems([str(i) if i >= 10 else '0' + str(i) for i in range(0, 31)])
        self.combo_right.setFixedHeight(50)
        self.combo_right.setStyleSheet(combo_style)

        spin_row = QHBoxLayout()
        spin_row.setSpacing(20)
        spin_row.addWidget(QLabel("Месяц:"), 0)
        spin_row.addWidget(self.combo_left, 1)
        spin_row.addWidget(QLabel("Год:"), 0)
        spin_row.addWidget(self.combo_right, 1)

        # 3) Поле ввола 2
        self.field_mid = QLineEdit(self)
        self.field_mid.setPlaceholderText("Введите код CVC")
        self.field_mid.setFixedHeight(50)
        self.field_mid.setStyleSheet(field_style)

        # 4) Кнопка проверки
        self.btn = QPushButton("Ввести", self)
        self.btn.setFixedHeight(50)
        self.btn.setFixedWidth(200)
        self.btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn.setStyleSheet("""
            QPushButton {
                font-size: 18px;
                font-weight: 700;
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 10px;
            }
        """)
        self.btn.clicked.connect(self.on_submit)

        btn_row = QHBoxLayout()
        btn_row.addStretch(1)
        btn_row.addWidget(self.btn)
        btn_row.addStretch(1)

        # --- Нижняя панель ---
        self.bottom_panel = BottomPanel(self)


        v = QVBoxLayout(self)
        v.setContentsMargins(60, 40, 60, 40)
        v.setSpacing(18)
        v.addWidget(self.field_top)
        v.addLayout(spin_row)
        v.addWidget(self.field_mid)
        v.addSpacing(10)
        v.addLayout(btn_row)
        v.addSpacing(10)
        v.addWidget(self.bottom_panel)  
        v.addStretch(1)                  

    def on_submit(self):
        if len(self.field_top.text()) != 16:
            QMessageBox.warning(self, "Ошибка", "Номер карты набран неверно - количество символов не равно 16")
        elif not (self.field_top.text()).isdigit():
            QMessageBox.warning(self, "Ошибка","Номер карты набран неверно - не все символы являются цифрами")
        elif len(self.field_mid.text()) != 3:
            QMessageBox.warning(self, "Ошибка","Код CVC набран неверно - количество символов не равно 3")
        elif not (self.field_mid.text()).isdigit():
            QMessageBox.warning(self, "Ошибка","Код CVC набран неверно - не все символы являются цифрами")
        else:
            self.bottom_panel.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec())
