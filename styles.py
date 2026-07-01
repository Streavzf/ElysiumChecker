# ── Elysium Server Color Palette ──────────────────────────────────────
# Dark green-black base, bright cyan/green accent, teal secondary

BG_MAIN        = "#041612"   # very dark cyan-black
BG_SIDEBAR     = "#02100d"   # even darker sidebar
BG_CARD        = "#07201b"   # card background
BG_CARD_HOVER  = "#0a2a24"
ACCENT         = "#2ae895"   # bright green-cyan (primary CTA)
ACCENT_HOVER   = "#4cf5aa"   # brighter on hover
ACCENT_LIGHT   = "#8fffd0"   # lighter for icons/highlights
SECONDARY      = "#0abfbc"   # teal secondary
TEXT_PRIMARY   = "#e0f8f1"   # near-white with slight cyan
TEXT_SECONDARY = "#7bc8b4"   # muted cyan
TEXT_MUTED     = "#357a66"   # very muted cyan
COLOR_GREEN    = "#2ec27e"
COLOR_RED      = "#e05252"
COLOR_YELLOW   = "#e0a050"
BORDER         = "#0e4034"   # subtle green border
NAV_ACTIVE_BG  = "#0c3026"   # active nav highlight
NAV_HOVER_BG   = "#08261e"

MAIN_STYLE = f"""
QMainWindow, QWidget {{
    background-color: {BG_MAIN};
    color: {TEXT_PRIMARY};
    font-family: 'Segoe UI', Arial, sans-serif;
}}

QScrollBar:vertical {{
    background: {BG_CARD};
    width: 6px;
    margin: 0;
    border-radius: 3px;
}}
QScrollBar::handle:vertical {{
    background: {ACCENT};
    min-height: 20px;
    border-radius: 3px;
}}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0; }}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{ background: none; }}

QScrollBar:horizontal {{
    background: {BG_CARD};
    height: 6px;
    border-radius: 3px;
}}
QScrollBar::handle:horizontal {{
    background: {ACCENT};
    min-width: 20px;
    border-radius: 3px;
}}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{ width: 0; }}

QTableWidget {{
    background-color: {BG_CARD};
    border: none;
    gridline-color: {BORDER};
    color: {TEXT_PRIMARY};
    font-size: 13px;
    selection-background-color: {NAV_ACTIVE_BG};
    outline: none;
}}
QTableWidget::item {{
    padding: 6px 10px;
    border-bottom: 1px solid {BORDER};
}}
QTableWidget::item:selected {{
    background-color: {NAV_ACTIVE_BG};
    color: {TEXT_PRIMARY};
}}
QHeaderView::section {{
    background-color: {BG_CARD};
    color: {ACCENT_LIGHT};
    padding: 8px 10px;
    border: none;
    border-bottom: 2px solid {ACCENT};
    font-size: 12px;
    font-weight: 600;
}}
QHeaderView {{ background-color: {BG_CARD}; }}

QLabel {{
    color: {TEXT_PRIMARY};
    background: transparent;
}}

QLineEdit {{
    background-color: {BG_CARD};
    border: 1px solid {BORDER};
    border-radius: 6px;
    padding: 8px 12px;
    color: {TEXT_PRIMARY};
    font-size: 13px;
}}
QLineEdit:focus {{ border: 1px solid {ACCENT}; }}

QTextEdit, QPlainTextEdit {{
    background-color: {BG_CARD};
    border: 1px solid {BORDER};
    border-radius: 6px;
    padding: 8px;
    color: {TEXT_PRIMARY};
    font-size: 13px;
}}

QToolTip {{
    background-color: {BG_CARD};
    color: {TEXT_PRIMARY};
    border: 1px solid {ACCENT};
    padding: 4px 8px;
    border-radius: 4px;
}}

QMessageBox {{
    background-color: {BG_MAIN};
    color: {TEXT_PRIMARY};
}}
QMessageBox QLabel {{ color: {TEXT_PRIMARY}; }}
QMessageBox QPushButton {{
    background-color: {ACCENT};
    color: white;
    border: none;
    border-radius: 6px;
    padding: 6px 16px;
    min-width: 80px;
}}
QMessageBox QPushButton:hover {{ background-color: {ACCENT_HOVER}; }}
"""

SIDEBAR_STYLE = f"""
QWidget#sidebar {{
    background-color: {BG_SIDEBAR};
    border-right: 1px solid {BORDER};
}}
"""

NAV_BUTTON_STYLE = f"""
QPushButton {{
    background-color: transparent;
    color: {TEXT_SECONDARY};
    border: none;
    border-radius: 8px;
    padding: 10px 16px;
    text-align: left;
    font-size: 14px;
    font-weight: 500;
}}
QPushButton:hover {{
    background-color: {NAV_HOVER_BG};
    color: {TEXT_PRIMARY};
}}
"""

NAV_BUTTON_ACTIVE_STYLE = f"""
QPushButton {{
    background-color: {NAV_ACTIVE_BG};
    color: {ACCENT_LIGHT};
    border: none;
    border-left: 3px solid {ACCENT};
    border-radius: 8px;
    padding: 10px 16px;
    text-align: left;
    font-size: 14px;
    font-weight: 600;
}}
"""

ACCENT_BUTTON_STYLE = f"""
QPushButton {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #09a6a3, stop:1 #1dbf7d);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 22px;
    font-size: 14px;
    font-weight: 600;
}}
QPushButton:hover {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #0cc2bf, stop:1 #23d98f);
}}
QPushButton:pressed {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #068280, stop:1 #149c63);
}}
QPushButton:disabled {{
    background: #0b2e25;
    color: {TEXT_MUTED};
}}
"""

TOOL_BUTTON_STYLE = f"""
QPushButton {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #09a6a3, stop:1 #1dbf7d);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 14px 10px;
    font-size: 13px;
    font-weight: 600;
    text-align: center;
}}
QPushButton:hover {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #0cc2bf, stop:1 #23d98f);
}}
QPushButton:pressed {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #068280, stop:1 #149c63);
}}
"""

CARD_STYLE = f"""
QWidget#card {{
    background-color: {BG_CARD};
    border-radius: 10px;
    border: 1px solid {BORDER};
}}
"""

STATUS_BAR_STYLE = f"""
QWidget#statusbar {{
    background-color: {BG_SIDEBAR};
    border-top: 1px solid {BORDER};
}}
"""
