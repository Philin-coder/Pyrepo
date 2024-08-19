import ctypes
import time

ctypes.windll.winmm.mciSendStringW("set cdaudio door closed",
                                   None, 0, None)
