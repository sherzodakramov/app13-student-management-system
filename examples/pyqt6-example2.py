import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, \
    QGridLayout, QLineEdit, QPushButton, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance: ")
        self.distance_input = QLineEdit()

        time_label = QLabel("Time (hours): ")
        self.time_input = QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(['Metric (km)', 'Imperial (miles)'])

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_avg_speed)
        self.result_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_input, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_input, 1, 1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.result_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_avg_speed(self):
        distance = float(self.distance_input.text())
        time = float(self.time_input.text())

        avg_speed = distance / time

        if self.unit_combo.currentText() == 'Metric (km)':
            avg_speed = round(avg_speed, 2)
            unit = "km/h"
        if self.unit_combo.currentText() == 'Imperial (miles)':
            avg_speed = round(avg_speed * 0.621371, 2)
            unit = "mph"

        self.result_label.setText(f"Average Speed: {avg_speed} {unit}")


app = QApplication(sys.argv)
calculator = SpeedCalculator()
calculator.show()
sys.exit(app.exec())
