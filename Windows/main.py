import sys
from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QWidget, QMainWindow, QStatusBar, QFileDialog, QTextEdit, QFontDialog, QColorDialog)
from PyQt6.QtCore import QStandardPaths
from PyQt6.QtGui import QPixmap, QAction, QKeySequence, QGuiApplication, QIcon, QTextCharFormat
from PyQt6.QtPrintSupport import QPrinter
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.setStyleSheet("background-color: rgb(36, 113, 163);")
        
    def initUI(self):
        self.setWindowTitle("Formulario")
        self.setGeometry(280, 200, 400, 500)
        self.setContentsMargins(30, 10, 30, 10)
        self.generate_window()
        self.show()
        
    def generate_window(self): 
        self.create_content()
        self.create_action()
        self.create_menu()
        
    def create_content(self):
        layout = QVBoxLayout()
        self.editor_text = QTextEdit()
        layout.addWidget(self.editor_text)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
       
    def create_action(self):
        self.open_window = QAction("Abrir", self)
        self.open_window.setShortcut(QKeySequence("Ctrl+O"))
        self.open_window.setStatusTip("Abrir Archivos")
        self.open_window.triggered.connect(self.open_main_window)
        
        self.save_window = QAction("Guardar", self)
        self.save_window.setShortcut(QKeySequence("Ctrl+S"))
        self.save_window.setStatusTip("Guardar Archivos")
        self.save_window.triggered.connect(self.save_main_window)
        
        self.export_window = QAction("Exportar", self)
        self.export_window.setShortcut(QKeySequence("Ctrl+E"))
        self.export_window.setStatusTip("Exportar Archivos")
        self.export_window.triggered.connect(self.export_main_window)
        
        self.font_window = QAction("Fuente", self)
        self.font_window.setShortcut(QKeySequence("Ctrl+F"))
        self.font_window.setStatusTip("Cambiar Fuentes")
        self.font_window.triggered.connect(self.font_main_window)
        
        self.color_window = QAction("Color", self)
        self.color_window.setShortcut(QKeySequence("Ctrl+K"))
        self.color_window.setStatusTip("Cambiar color")
        self.color_window.triggered.connect(self.color_main_window)
        
        self.undo_window = QAction("Deshacer", self)
        self.undo_window.setShortcut(QKeySequence("Ctrl+Z"))
        self.undo_window.setStatusTip("Deshacer Cambios")
        self.undo_window.triggered.connect(self.editor_text.undo)
        
        self.redo_window = QAction("Rehacer", self)
        self.redo_window.setShortcut(QKeySequence("Ctrl+Y"))
        self.redo_window.setStatusTip("Rehacer Cambios")
        self.redo_window.triggered.connect(self.editor_text.redo)
        
    def create_menu(self):
        menu_archive = self.menuBar().addMenu("Archivo")
        menu_archive.addAction(self.open_window)
        menu_archive.addAction(self.save_window)
        menu_archive.addAction(self.export_window)
        
        menu_edit = self.menuBar().addMenu("Editar")
        menu_edit.addAction(self.font_window)
        menu_edit.addAction(self.color_window)
        menu_edit.addAction(self.undo_window)
        menu_edit.addAction(self.redo_window)

    def open_main_window(self):
        initial_value = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DesktopLocation)
        file_types = "Texts Files (*.txt);;Images (*.png);;All Files (*)"
        self.file, _ = QFileDialog.getOpenFileName(self, "Open File", initial_value, file_types)
        
        if self.file:
            file_extension = os.path.splitext(self.file)[1].lower()
            if file_extension == '.txt':
                try:
                    with open(self.file, "r", encoding='utf-8') as file:
                        self.editor_text.setText(file.read())
                        self.setWindowTitle(self.file)
                        self.statusBar.showMessage("Archivo de texto abierto")
                except UnicodeDecodeError:
                    self.statusBar.showMessage("Error al decodificar el archivo de texto")
            elif file_extension in ['.png', '.jpg', '.bmp']:
                pixmap = QPixmap(self.file)
                if not pixmap.isNull():
                    self.setWindowIcon(QIcon(pixmap))
                    self.editor_text.setText(f"Imagen cargada: {self.file}")
                    self.statusBar.showMessage("Archivo de imagen abierto")
                else:
                    self.statusBar.showMessage("Error al cargar la imagen")
            else:
                self.statusBar.showMessage("Tipo de archivo no soportado")
        print("Abriendo Archivos ...")
    
    def save_main_window(self):
        initial_value = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DownloadLocation)
        file_name, _ = QFileDialog.getSaveFileName(self, "Guardar Archivos", initial_value, "Archivos de textos (*.txt);; HTML (*.html)")
        
        if file_name:
            if file_name.endswith(".txt"):
                text = self.editor_text.toPlainText()
                with open(file_name, "w", encoding='utf-8') as file:
                    file.write(text)
                    self.statusBar.showMessage(f"Archivo de texto guardado en: {file_name}")
            elif file_name.endswith(".html"):
                text_html = self.editor_text.toHtml()
                with open(file_name, "w", encoding='utf-8') as file:
                    file.write(text_html)
                    self.statusBar.showMessage(f"Archivo HTML guardado en: {file_name}")
            else:
                self.statusBar.showMessage("Tipo de archivo no soportado para guardar")
        print("Guardando Archivo ...")
    
    def font_main_window(self):
        selected_text_cursor = self.editor_text.textCursor()
        font, ok = QFontDialog.getFont(self.editor_text.currentFont(), self)
        
        if ok:
            if selected_text_cursor.hasSelection():
                format = QTextCharFormat()
                format.setFont(font)
                selected_text_cursor.mergeCharFormat(format)
            else:
                self.editor_text.setCurrentFont(font)
                
    def color_main_window(self):
        selected_text_cursor = self.editor_text.textCursor()
        color = QColorDialog.getColor(self.editor_text.textColor(), self)
        
        if color.isValid():
            if selected_text_cursor.hasSelection():
                format = QTextCharFormat()
                format.setForeground(color)
                selected_text_cursor.mergeCharFormat(format)
            else:
                self.editor_text.setTextColor(color)
                
    def export_main_window(self):
        initial_value = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DownloadLocation)
        file_name, _ = QFileDialog.getSaveFileName(self, "Exportar Archivos", initial_value, "PDF (*.pdf);; PNG (*.png);; JPEG (*.jpeg);; WORD (*.docx);")
        
        if file_name:
            if file_name.endswith(".pdf"):
                printer = QPrinter(QPrinter.PrinterMode.HighResolution)
                printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
                printer.setOutputFileName(file_name)
                self.editor_text.document().print(printer)
                self.statusBar.showMessage(f"Archivo PDF exportado en: {file_name}")
                
            elif file_name.endswith(".docx"):
                doc = doc.Document()
                doc.add_paragraph(self.editor_text.toPlainText())
                doc.save(file_name)
                self.statusBar.showMessage(f"Archivo DOCX exportado en: {file_name}")
                
            else:
                screen = QGuiApplication.primaryScreen()
                pixmap = screen.grabWindow(self.editor_text.winId())
                pixmap.save(file_name)
                self.statusBar.showMessage(f"Archivo de imagen exportado en: {file_name}")
        
    print("Exportar Archivos ...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
