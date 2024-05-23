import sys

from PyQt6.QtWidgets import (QApplication, QVBoxLayout,QWidget,
                            QMainWindow, QStatusBar,QFileDialog,QTextEdit,QFontDialog)
from PyQt6.QtCore import QStandardPaths
from PyQt6.QtGui import  QPixmap, QAction, QKeySequence,QIcon

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
        self.setGeometry(300, 300, 500, 500)
        self.setContentsMargins(30, 10, 30, 10)
        self.generate_window()
        self.show()
        
    def generate_window(self): 
        self.create_action()
        self.create_menu()
        self.create_content()
        
    def create_content(self):
        layout = QVBoxLayout()
        self.editor_text = QTextEdit()
        layout.addWidget(self.editor_text)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def create_action(self):
        self.open_window = QAction("Abrir", self)
        self.open_window.setShortcut(QKeySequence("Ctrl+o"))
        self.open_window.setStatusTip("Abrir Archivos")
        self.open_window.triggered.connect(self.open_main_window)
        
        self.save_window = QAction("Guardar", self)
        self.save_window.setShortcut(QKeySequence("Ctrl+s"))
        self.save_window.setStatusTip("Guardar Archivos")
        self.save_window.triggered.connect(self.save_main_window)
        
        self.export_window = QAction("Exportar", self)
        self.export_window.setShortcut(QKeySequence("Ctrl+E"))
        self.export_window.setStatusTip("Exportar Archivos")
        self.export_window.triggered.connect(self.export_main_window)
        
        self.font_window = QAction("Fuente", self)
        self.font_window.setShortcut(QKeySequence("Ctrl+f"))
        self.font_window.setStatusTip("Cambiar Fuentes")
        self.font_window.triggered.connect(self.font_main_window)
        
        self.undo_window = QAction("Deshacer", self)
        self.undo_window.setShortcut(QKeySequence("Ctrl+Z"))
        self.undo_window.setStatusTip("Deshacer Cambios")
        self.undo_window.triggered.connect(self.undo_main_window)
        
        self.redo_window = QAction("Rehacer", self)
        self.redo_window.setShortcut(QKeySequence("Ctrl+y"))
        self.redo_window.setStatusTip("Rehacer Cambios")
        self.redo_window.triggered.connect(self.redo_main_window)
        
    def create_menu(self):
        menu_archive = self.menuBar().addMenu("Archivo")
        menu_archive.addAction(self.open_window)
        menu_archive.addAction(self.save_window)
        menu_archive.addAction(self.export_window)
        
        menu_edit = self.menuBar().addMenu("Editar")
        menu_edit.addAction(self.undo_window)
        menu_edit.addAction(self.redo_window)
        menu_edit.addAction(self.font_window)
        
        
    def open_main_window(self):
        options = (QFileDialog.Option.DontUseNativeDialog)
        initial_value = QStandardPaths.writableLocation(
            QStandardPaths.StandardLocation.DocumentsLocation)
        file_types = "Texts Files (*.txt);;Images (*.png);;All Files (*)"
        self.file, _ =QFileDialog.getOpenFileName(self, "Open File", initial_value,
                                  file_types)
        if self.file:
            file_extension = os.path.splitext(self.file)[1].lower()
            if file_extension in ['.txt']:
                try:
                    with open(self.file, "r", encoding='utf-8') as file:
                        self.editor_text.setText(file.read())
                        self.setWindowTitle(self.file)
                        self.setContentsMargins(30, 10, 30, 10)
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
        #Most files
        """with open(self.file, "r") as file:
            self.editor_text.setText(file.read())
            self.statusBar.showMessage("Archivo Abierto")
            self.setWindowTitle(self.file)
            self.setContentsMargins(30, 30, 30, 30)
            self.setWindowIcon(QIcon(QPixmap(self.file))) 
            #self.setFixedSize(300, 200)"""
        
        
        print ("Abriendo Archivos ...")
    
    def save_main_window(self):
        print ("Guardar Archivos ...")
    
    def font_main_window(self):
        selected_text_cursor = self.editor_text.textCursor()
        
        font , ok =QFontDialog.getFont(
            self.editor_text.currentFont(), self
        )
        
        if ok :
            if selected_text_cursor.hasSelection():
                format = self.editor_text.currentCharFormat()
                format.setFont(font)
                selected_text_cursor.mergeCharFormat(format)
                
            else: 
                self.editor_text.setCurrentFont(font)
                
    
    def export_main_window(self):
        print ("Exportar Archivos ...")
    
    def undo_main_window(self):
        print ("Deshacer Cambios ...")
        
    def redo_main_window(self):
        print ("Rehacer Cambios ...")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())