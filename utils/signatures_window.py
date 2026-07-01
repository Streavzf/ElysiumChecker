import sys
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QApplication, QFrame, QTextBrowser
)
from PyQt5.QtCore import Qt, QTimer
import styles
from utils.signatures_html import SECTIONS

class SignaturesWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElysiumChecker — База сигнатур")
        self.setMinimumSize(700, 600)
        self.setWindowFlags(Qt.Window)
        self.setStyleSheet(styles.MAIN_STYLE)
        
        self._build_ui()
        self._set_dark_titlebar()

    def _set_dark_titlebar(self):
        try:
            import ctypes
            import sys
            if sys.platform != "win32":
                return
            hwnd = int(self.winId())
            set_window_attribute = ctypes.windll.dwmapi.DwmSetWindowAttribute
            res = set_window_attribute(hwnd, 20, ctypes.byref(ctypes.c_int(1)), ctypes.sizeof(ctypes.c_int))
            if res != 0:
                set_window_attribute(hwnd, 19, ctypes.byref(ctypes.c_int(1)), ctypes.sizeof(ctypes.c_int))
        except Exception:
            pass

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Header
        header = QWidget()
        header.setStyleSheet(f"background-color: {styles.BG_SIDEBAR}; border-bottom: 1px solid {styles.BORDER};")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(24, 16, 24, 16)
        
        title_lbl = QLabel("ElysiumChecker")
        title_lbl.setStyleSheet(f"color: {styles.ACCENT_LIGHT}; font-size: 16px; font-weight: bold; border: none;")
        sub_lbl = QLabel("База сигнатур для проверки на читы")
        sub_lbl.setStyleSheet(f"color: {styles.TEXT_MUTED}; font-size: 12px; border: none;")
        
        titles_v = QVBoxLayout()
        titles_v.addWidget(title_lbl)
        titles_v.addWidget(sub_lbl)
        header_layout.addLayout(titles_v)
        header_layout.addStretch()
        layout.addWidget(header)
        
        # Scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setStyleSheet("QScrollArea { background: transparent; border: none; }")
        
        content_w = QWidget()
        content_w.setStyleSheet("background: transparent;")
        content_layout = QVBoxLayout(content_w)
        content_layout.setContentsMargins(24, 24, 24, 24)
        content_layout.setSpacing(20)
        
        current_group = None
        for sec in SECTIONS:
            group = sec["title"]
            if group != current_group:
                current_group = group
                group_lbl = QLabel(group.upper())
                group_lbl.setStyleSheet(f"color: {styles.TEXT_MUTED}; font-size: 11px; font-weight: bold; margin-top: 10px;")
                content_layout.addWidget(group_lbl)
            
            # Card widget
            card = QWidget()
            card.setStyleSheet(f"QWidget {{ background-color: {styles.BG_CARD}; border: 1px solid {styles.BORDER}; border-radius: 10px; }}")
            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(16, 16, 16, 16)
            card_layout.setSpacing(10)
            
            # Card header (Title, Subtitle, Copy btn)
            c_header = QHBoxLayout()
            c_header.setSpacing(10)
            
            text_v = QVBoxLayout()
            title_color = styles.ACCENT if group == "Everything" else styles.SECONDARY
            c_title = QLabel(sec['title'])
            c_title.setStyleSheet(f"color: {title_color}; font-size: 14px; font-weight: bold; border: none; background: transparent;")
            c_sub = QLabel(sec['subtitle'])
            c_sub.setStyleSheet(f"color: {styles.TEXT_MUTED}; font-size: 12px; border: none; background: transparent;")
            text_v.addWidget(c_title)
            text_v.addWidget(c_sub)
            
            copy_btn = QPushButton("Копировать")
            copy_btn.setStyleSheet(styles.ACCENT_BUTTON_STYLE)
            copy_btn.setFixedHeight(30)
            copy_btn.setCursor(Qt.PointingHandCursor)
            
            c_header.addLayout(text_v)
            c_header.addStretch()
            c_header.addWidget(copy_btn)
            
            card_layout.addLayout(c_header)
            
            # Query text
            query_box = QTextBrowser()
            query_box.setPlainText(sec['query'])
            query_box.setStyleSheet(f"background-color: {styles.BG_MAIN}; border: 1px solid {styles.BORDER}; border-radius: 6px; padding: 10px; color: {styles.TEXT_PRIMARY}; font-family: Consolas, monospace; font-size: 12px;")
            
            # calculate height roughly based on length
            doc_height = 40 + (len(sec['query']) // 80) * 16
            query_box.setFixedHeight(max(50, min(150, doc_height)))
            
            card_layout.addWidget(query_box)
            
            # Wire up copy button
            copy_btn.clicked.connect(lambda checked, q=sec['query'], btn=copy_btn: self._copy_text(q, btn))
            
            content_layout.addWidget(card)
            
        content_layout.addStretch()
        scroll.setWidget(content_w)
        layout.addWidget(scroll)

    def _copy_text(self, text, btn):
        QApplication.clipboard().setText(text)
        orig_text = btn.text()
        btn.setText("Скопировано")
        btn.setStyleSheet(f"background-color: {styles.COLOR_GREEN}; color: white; border: none; border-radius: 8px; font-size: 14px; font-weight: bold; padding: 0 16px;")
        
        QTimer.singleShot(1500, lambda: self._reset_btn(btn, orig_text))

    def _reset_btn(self, btn, orig_text):
        btn.setText(orig_text)
        btn.setStyleSheet(styles.ACCENT_BUTTON_STYLE)
