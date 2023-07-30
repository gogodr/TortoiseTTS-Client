
from PySide6.QtWidgets import QWidget, QHBoxLayout, QSlider, QToolButton, QLabel
from PySide6.QtGui import QIcon, QFont
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QSize, QTime, QUrl, Qt


class MusicPlayer(QWidget):
    play_icon = None
    pause_icon = None
    autorenew_icon = None
    skip_next_icon = None
    skip_previous_icon = None
    stop_icon = None
    playing = False

    def __init__(self):
        super().__init__()

        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)

        self.main_layout = QHBoxLayout()
        self.layout_actions = QHBoxLayout()
        self.horizontalSliderPlay = QSlider(self)
        self.horizontalSliderPlay.setOrientation(Qt.Horizontal)
        self.horizontalSliderPlay.setDisabled(True)

        self.load_icons()

        self.playBtn = QToolButton(self)
        self.playBtn.setIcon(self.play_icon)
        self.playBtn.setIconSize(QSize(32, 32))
        self.playBtn.setDisabled(True)

        self.skipPrevBtn = QToolButton(self)
        self.skipPrevBtn.setIcon(self.skip_previous_icon)
        self.skipPrevBtn.setIconSize(QSize(24, 24))
        self.skipPrevBtn.setDisabled(True)
        self.stopBtn = QToolButton(self)
        self.stopBtn.setIcon(self.stop_icon)
        self.stopBtn.setIconSize(QSize(24, 24))
        self.stopBtn.setDisabled(True)

        self.labelTimer = QLabel(self)
        font = QFont()
        font.setPointSize(14)
        self.labelTimer.setFont(font)
        self.labelTimer.setText("--:--:--")

        self.main_layout.addWidget(self.playBtn)
        self.layout_actions.addWidget(self.skipPrevBtn)
        self.layout_actions.addWidget(self.stopBtn)
        self.main_layout.addLayout(self.layout_actions)
        self.main_layout.addWidget(self.horizontalSliderPlay)
        self.main_layout.addWidget(self.labelTimer)

        self.setLayout(self.main_layout)

        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)

        self.playBtn.clicked.connect(self.play_audio)
        self.horizontalSliderPlay.sliderMoved.connect(self.play_slider_changed)
        self.stopBtn.clicked.connect(self.stop_audio)
        self.skipPrevBtn.clicked.connect(self.skip_previous)

    def play_slider_changed(self, position):
        self.player.setPosition(position)

    def load_audio(self, path):
        self.player.setSource(QUrl.fromLocalFile(path))

        seconds = (self.player.duration() / 1000) % 60
        minutes = (self.player.duration() / 60000)
        time = QTime(0, minutes, seconds)
        self.durationText = time.toString('mm:ss')
        self.labelTimer.setText(f"00:00 / {self.durationText}")
        self.horizontalSliderPlay.setDisabled(False)
        self.playBtn.setDisabled(False)
        self.skipPrevBtn.setDisabled(False)
        self.stopBtn.setDisabled(False)

    def position_changed(self, position):
        if (self.horizontalSliderPlay.maximum() != self.player.duration()):
            self.horizontalSliderPlay.setMaximum(self.player.duration())

        self.horizontalSliderPlay.setValue(position)

        seconds = (position / 1000) % 60
        minutes = (position / 60000)

        time = QTime(0, minutes, seconds)
        self.labelTimer.setText(
            f"{time.toString('mm:ss')} / {self.durationText}")

        if position == self.player.duration():
            self.stop_audio()

    def duration_changed(self, duration):
        self.horizontalSliderPlay.setRange(0, duration)

    def play_audio(self):
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
            self.playBtn.setIcon(self.play_icon)
        else:
            self.player.play()
            self.playBtn.setIcon(self.pause_icon)

    def stop_audio(self):
        self.player.stop()
        self.player.setPosition(0)
        self.playBtn.setIcon(self.play_icon)

    def skip_previous(self):
        self.player.setPosition(0)

    def load_icons(self):
        self.play_icon = QIcon()
        self.play_icon.addFile(u":/icons/play_arrow.png",
                               QSize(), QIcon.Normal, QIcon.Off)

        self.pause_icon = QIcon()
        self.pause_icon.addFile(u":/icons/pause.png",
                                QSize(), QIcon.Normal, QIcon.Off)

        self.skip_previous_icon = QIcon()
        self.skip_previous_icon.addFile(
            u":/icons/skip_previous.png", QSize(), QIcon.Normal, QIcon.Off)

        self.stop_icon = QIcon()
        self.stop_icon.addFile(u":/icons/stop.png",
                               QSize(), QIcon.Normal, QIcon.Off)
