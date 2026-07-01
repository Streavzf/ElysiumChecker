import os
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QGridLayout, QMessageBox
)
from PyQt5.QtCore import Qt
import styles
from utils.launcher import launch_exe
from utils.paths import tool_path

SECONDARY_TOOLS = [
    ("WinPrefetchView",      "WinPrefetchView.exe"),
    ("ExecutedProgramsList", "ExecutedProgramsList.exe"),
    ("RecentFilesView",     "RecentFilesView.exe"),
    ("RegistryExplorer",    "RegistryExplorer\\RegistryExplorer.exe"),
    ("JumpListExplorer",    "JumpListExplorer\\JumpListExplorer.exe"),
    ("SimpleUnlocker",      "SimpleUnlocker\\SU.exe"),
]


class SecondaryCheckPage(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 16)
        layout.setSpacing(14)

        header = QHBoxLayout()
        icon = QLabel("💬")
        icon.setStyleSheet(f"color: {styles.ACCENT_LIGHT}; font-size: 24px; padding-right: 6px;")
        title = QLabel("Вторичная проверка")
        title.setStyleSheet(f"color: {styles.TEXT_PRIMARY}; font-size: 26px; font-weight: 700;")
        header.addWidget(icon)
        header.addWidget(title)
        header.addStretch()
        layout.addLayout(header)

        card = QWidget()
        card.setObjectName("card")
        card.setStyleSheet(styles.CARD_STYLE)
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(20, 16, 20, 20)
        card_layout.setSpacing(16)

        hint = QLabel("Нажмите на инструмент, чтобы запустить его")
        hint.setAlignment(Qt.AlignCenter)
        hint.setStyleSheet(f"color: {styles.TEXT_SECONDARY}; font-size: 13px;")
        card_layout.addWidget(hint)

        grid = QGridLayout()
        grid.setSpacing(10)
        for idx, (name, exe) in enumerate(SECONDARY_TOOLS):
            row, col = divmod(idx, 3)
            btn = QPushButton(f"{idx + 1}.  {name}")
            btn.setFixedHeight(52)
            btn.setStyleSheet(styles.TOOL_BUTTON_STYLE)
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, e=exe, n=name: self._launch(e, n))
            grid.addWidget(btn, row, col)

        card_layout.addLayout(grid)
        layout.addWidget(card)
        layout.addStretch()

    def _launch(self, exe: str, name: str):
        path = tool_path(exe)
        if not os.path.isfile(path):
            QMessageBox.warning(
                self,
                "Утилита не найдена",
                f"Файл не найден:\n{path}\n\nПоместите .exe в папку tools\\",
            )
            return
        try:
            launch_exe(path)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка запуска", str(e))
