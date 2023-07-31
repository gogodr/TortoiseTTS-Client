from datetime import datetime
import re
import torch
import torchaudio
from modules.singleton import Singleton
from PySide6.QtCore import QThread, Signal, QObject
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_voice


class TTSGen(metaclass=Singleton):
    tts: TextToSpeech = None

    def __init__(self):
        self.tts = TextToSpeech()

    def generate_audio(self, text, voice, preset, folder, candidates=1):
        self.thread = TTSGeneratorThread(
            text, voice, preset, folder, candidates)
        self.thread.signals.progress.connect(self.on_progress)
        self.thread.signals.finished.connect(self.on_finished)
        self.thread.start()


class TTSGeneratorSignals(QObject):
    progress = Signal(int)
    finished = Signal(list)


class TTSGeneratorThread(QThread):
    def __init__(self, text, voice, preset, candidates=1,  parent=None):
        QThread.__init__(self, parent)
        self.text = text
        self.voice = voice
        self.preset = preset
        self.candidates = candidates
        self.signals = TTSGeneratorSignals()
        print("TTSGeneratorThread Initialized")

    def break_text_into_array(self, text):
        split_text = re.split(r'[\n,.;]+', text)
        split_text = [line.strip() for line in split_text if line.strip()]
        return split_text

    def clean_and_trim_text(self, input_string):
        cleaned_string = re.sub(r'[^\w\s]', '', input_string)
        cleaned_string = cleaned_string.replace('\n', ' ').strip()
        trimmed_string = cleaned_string[:100]
        return trimmed_string.lower()

    def run(self):
        print("TTSGeneratorThread Started")
        voice_samples, conditioning_latents = load_voice(self.voice)
        texts = self.break_text_into_array(self.text)
        audios = {}
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

        for text_idx, text in enumerate(texts):
            gen = TTSGen().tts.tts_with_preset(
                text, k=self.candidates, voice_samples=voice_samples,
                conditioning_latents=conditioning_latents, preset=self.preset)

            self.signals.progress.emit(((text_idx+1) / len(texts))*100)

            for candidate_idx, audio in enumerate(gen):
                if (str(candidate_idx) in audios) is False:
                    audios[str(candidate_idx)] = []
                audio = audio.squeeze(0).cpu()
                audios[str(candidate_idx)].append(audio)

        output = []
        for candidate_idx in audios:
            audio = torch.cat(audios[candidate_idx], dim=-1)
            filename = self.clean_and_trim_text(self.text)
            filepath = f'output/{timestamp}-{candidate_idx}-{filename}.wav'
            torchaudio.save(filepath, audio, 24000)
            output.append(filepath)
        self.signals.finished.emit(output)


class LoadTTSSignals(QObject):
    finished = Signal()
    error = Signal()


class LoadTTSThread(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.signals = LoadTTSSignals()
        print("LoadTTSThread Initialized")

    def run(self):
        try:
            print("LoadTTSThread Started")
            TTSGen()
            self.signals.finished.emit()
        except Exception as e:
            print(e)
            self.signals.error.emit()
