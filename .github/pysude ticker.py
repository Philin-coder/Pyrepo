import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QRunnable, QThreadPool, QObject, pyqtSignal

MAX_ITER = 1000000


class ProcessorWorker(QObject):
    iteration_passed = pyqtSignal(int)
    status_changed = pyqtSignal(bool)
    finished = pyqtSignal()


class Processor(QRunnable):
    def __init__(self, parent):
        super().__init__()
        # we need parent to protect worker
        # from being deleted before Processor
        self.signals = ProcessorWorker(parent)

    def run(self):
        self.signals.status_changed.emit(True)
        with open("out.txt", "w") as f:
            i = 0
            while i < MAX_ITER:
                f.write("{}\n".format(i))
                i += 1
                self.signals.iteration_passed.emit(i + 1)
        self.signals.status_changed.emit(False)
        self.signals.finished.emit()
        # now we ask application do delete worker
        # since we don't need it anymore
        self.signals.deleteLater()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__(flags=Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        vlayout = QtWidgets.QVBoxLayout()
        widget = QtWidgets.QWidget()
        widget.setLayout(vlayout)
        self.setCentralWidget(widget)
        self.bar = QtWidgets.QProgressBar()
        self.bar.setMinimum(0)
        self.bar.setMaximum(MAX_ITER)
        self.bar.setValue(0)
        vlayout.addWidget(self.bar)
        self.button = QtWidgets.QPushButton("Start")
        self.button.pressed.connect(self.process)
        vlayout.addWidget(self.button)
        button = QtWidgets.QPushButton("About")
        button.pressed.connect(app.aboutQt)
        vlayout.addWidget(button)
        self.thread_pool = QThreadPool(self)
        self.destroyed.connect(lambda: self.cleanup())

    def process(self):
        processor = Processor(self)
        processor.signals.iteration_passed.connect(self.bar.setValue, Qt.DirectConnection)
        processor.signals.status_changed.connect(self.button.setDisabled)
        processor.signals.finished.connect(lambda: self.bar.setValue(0))
        self.thread_pool.start(processor)

    def cleanup(self):
        self.thread_pool.waitForDone()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow()
    w.setFixedSize(300, 150)
    w.show()

    sys.exit(app.exec_())
