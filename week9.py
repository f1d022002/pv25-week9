import sys
from PyQt5.QtWidgets import *

class ItemPickerDialog(QDialog):
    def __init__(self, choices, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pilih Item")
        self.layout = QFormLayout()

        self.dropdown = QComboBox()
        self.dropdown.addItems(choices)
        self.layout.addRow("Pilih Bahasa Pemrograman:", self.dropdown)

        self.button_layout = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_layout.accepted.connect(self.accept)
        self.button_layout.rejected.connect(self.reject)
        self.layout.addRow(self.button_layout)

        self.setLayout(self.layout)

    def get_selected_item(self):
        return self.dropdown.currentText()

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week-9 Input Dialog Application")
        self.setGeometry(150, 150, 600, 300)
        main_layout = QVBoxLayout()

        # First section: Choose from a list
        section_one = QHBoxLayout()
        pick_button = QPushButton("Silakan Pilih")
        pick_button.clicked.connect(self.launch_picker)
        self.result_display = QLineEdit()
        section_one.addWidget(pick_button)
        section_one.addWidget(self.result_display)

        # Second section: Input Name
        section_two = QHBoxLayout()
        name_button = QPushButton("Masukkan Nama")
        name_button.clicked.connect(self.capture_name)
        self.name_input = QLineEdit()
        section_two.addWidget(name_button)
        section_two.addWidget(self.name_input)

        # Third section: Input Number
        section_three = QHBoxLayout()
        number_button = QPushButton("Masukkan Angka")
        number_button.clicked.connect(self.capture_number)
        self.number_input = QLineEdit()
        section_three.addWidget(number_button)
        section_three.addWidget(self.number_input)

        
        identity_layout = QVBoxLayout()
        identity_layout.addWidget(QLabel("Nama : Andi Sibwayiq"))
        identity_layout.addWidget(QLabel("NIM  : F1D022002"))
        identity_layout.addWidget(QLabel("Kelas: C"))
        
        
        identity_layout.setSpacing(5)
        identity_layout.setContentsMargins(0, 0, 0, 0)

        
        main_layout.addLayout(section_one)
        main_layout.addLayout(section_two)
        main_layout.addLayout(section_three)
        main_layout.addLayout(identity_layout)

        self.setLayout(main_layout)

    def launch_picker(self):
        options = ["C++", "Python", "Java", "JavaScript", "php", "Ruby", "Swift"]
        picker_dialog = ItemPickerDialog(options, self)
        if picker_dialog.exec_() == QDialog.Accepted:
            selected_item = picker_dialog.get_selected_item()
            self.result_display.setText(selected_item)

    def capture_name(self):
        full_name, confirmed = QInputDialog.getText(self, "Nama Lengkap", "Mohon Masukan Nama Lengkap:")
        if confirmed and full_name.strip():
            self.name_input.setText(full_name)

    def capture_number(self):
        number, confirmed = QInputDialog.getInt(self, "Angka", "Mohon Masukan Sebuah Angka:")
        if confirmed:
            self.number_input.setText(str(number))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())