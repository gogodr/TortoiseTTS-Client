import os
import re
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from modules.main_form import MainForm
from modules.music_player import MusicPlayer
from tortoise.utils.audio import load_voice
from modules.ttsgen import LoadTTSThread, TTSGeneratorThread

from assets.resource.resource_rc import *


class TortoiseApp(QApplication):
    def __init__(self, *args, **kwargs):
        QApplication.__init__(self, *args, **kwargs)
        self.main_window = MainForm()
        self.main_window.show()
        self.main_window.ui.generate_btn.setText("Loading TTS...")
        self.main_window.ui.generate_btn.setEnabled(False)
        self.load_voices()
        self.load_tts_thread = LoadTTSThread()
        self.load_tts_thread.start()
        self.load_tts_thread.signals.finished.connect(
            self.on_load_tts_finished)
        self.load_tts_thread.signals.error.connect(self.on_load_tts_error)
        self.main_window.ui.generate_btn.clicked.connect(self.generate_audio)

        self.main_window.ui.prompt_txt.setText("This is a test\nwith 2 lines, and 2 candidates")
        self.main_window.ui.samples_spin_box.setValue(2)
        self.main_window.ui.voices_reload_btn.clicked.connect(self.load_voices)

    def on_load_tts_finished(self):
        print("Finished loading TTS models.")
        self.main_window.ui.generate_btn.setText("Generate")
        self.main_window.ui.generate_btn.setEnabled(True)

    def on_load_tts_error(self):
        print("Error loading TTS models.")
        self.main_window.ui.generate_btn.setText("Error")
        self.main_window.ui.generate_btn.setEnabled(False)

    def folder_has_wav_file(self, folder_path):
        if not os.path.exists(folder_path):
            print("Error: The provided folder path does not exist.")
            return False

        if not os.path.isdir(folder_path):
            print("Error: The provided path is not a folder.")
            return False

        for file_name in os.listdir(folder_path):
            if file_name.lower().endswith(".wav"):
                return True

        return False

    def load_voices(self):
        voices_folder_path = os.fspath(
            Path(__file__).resolve().parent / "voices")
        if not os.path.exists(voices_folder_path):
            print("Error: The 'voices' folder does not exist.")
            return

        if not os.path.isdir(voices_folder_path):
            print("Error: The provided path is not a folder.")
            return

        folders_inside_voices = [name for name in os.listdir(
            voices_folder_path) if os.path.isdir(os.path.join(voices_folder_path, name)) and self.folder_has_wav_file(os.path.join(voices_folder_path, name))]
        if not folders_inside_voices:
            print("No folders found inside the 'voices' folder.")
            return

        self.main_window.ui.voices_list.clear()
        self.main_window.ui.voices_list.addItems(folders_inside_voices)
        self.main_window.ui.voices_list.setCurrentRow(0)

        self.main_window.ui.output_btn.clicked.connect(self.open_output_folder)
    
    def open_output_folder(self):
        output_folder_path = os.fspath(
            Path(__file__).resolve().parent / "output")
        if not os.path.exists(output_folder_path):
            print("Error: The 'output' folder does not exist.")
            return

        if not os.path.isdir(output_folder_path):
            print("Error: The provided path is not a folder.")
            return

        os.startfile(output_folder_path)

    def generate_audio(self):
        print("Generate Audio")
        voice = self.main_window.ui.voices_list.currentItem().text()
        candidates = self.main_window.ui.samples_spin_box.value()
        preset = self.main_window.ui.quality_combo_box.currentText()
        full_text = self.main_window.ui.prompt_txt.toPlainText()
        self.gen_thread = TTSGeneratorThread(full_text, voice, preset, candidates)
        self.gen_thread.signals.finished.connect(self.on_generate_finished)
        self.gen_thread.signals.progress.connect(self.on_generate_progress)
        self.main_window.ui.generate_btn.setEnabled(False)
        self.main_window.ui.generate_btn.setText("0%")
        self.gen_thread.start()

    def on_generate_finished(self, audio_results):
        self.main_window.ui.generate_btn.setText("Generate")
        self.main_window.ui.generate_btn.setEnabled(True)

        for i in reversed(range(self.main_window.ui.result_layout.count())): 
            self.main_window.ui.result_layout.itemAt(i).widget().setParent(None)
        for audio_result in audio_results:
            audio_sample = MusicPlayer()
            audio_sample.load_audio(audio_result)
            self.main_window.ui.result_layout.addWidget(audio_sample)
    
    def on_generate_progress(self, progress):
        self.main_window.ui.generate_btn.setText(f"{progress}%")
        self.main_window.ui.generate_btn.setEnabled(False)

if __name__ == "__main__":
    app = TortoiseApp([])
    path = os.fspath(Path(__file__).resolve().parent / "assets/ui/style.qss")
    with open(path, "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    sys.exit(app.exec())
