
import os
from pathlib import Path
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

from modules.music_player import MusicPlayer


class MainForm(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainForm, self).__init__(*args, **kwargs)
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent /
                         "../assets/ui/main.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        self.setCentralWidget(self.ui.main_container)

        audio_sample = MusicPlayer()
        self.ui.result_layout.addWidget(audio_sample)
        self.autorenew_icon = QIcon()
        self.autorenew_icon.addFile(u":/icons/autorenew.png",
                                    QSize(), QIcon.Normal, QIcon.Off)
        self.ui.voices_reload_btn.setIcon(self.autorenew_icon)
        self.ui.voices_reload_btn.setIconSize(QSize(16, 16))

        
        self.folder_icon = QIcon()
        self.folder_icon.addFile(u":/icons/folder.png",
                                    QSize(), QIcon.Normal, QIcon.Off)
        self.ui.output_btn.setIcon(self.folder_icon)
        self.ui.output_btn.setIconSize(QSize(24, 24))


        