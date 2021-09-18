# -*- encoding: utf-8 -*-
# Now works in python 3 aswell as 2
import sys, threading, time, os, datetime, time, inspect, subprocess, socket
from subprocess import PIPE, STDOUT
from wsgiref.simple_server import make_server


class Webshite():

    def __init__(self):
        self.hostname = socket.getfqdn()
        self.header = """
        <html>
        <header>
        <style>
        body {
            background-color:#6C7A89;
        }
        p {
            color:white;
            font-family:Consolas;
        }
        </style>
        </header>
        <body>
        """
        self.shite = "<p>" + str(self.hostname) + "</p>"

        self.footer = """
        </body>
        </html>
        """

    def grains(self, environ, start_response):
        self.environ = environ
        self.start = start_response
        status = '200 OK'
        response_headers = [('Content-type', 'text/html; charset=utf-8')]
        self.start(status, response_headers)
        fullsite = self.header + self.shite + self.footer
        fullsite = [fullsite.encode('utf-8')]  # in python 3, this needed to be a list, and encoded
        return fullsite

    def run(self):
        srv = make_server('127.0.0.1', 8080, self.grains)

        while True:
            try:
                threading.Thread(target=srv.handle_request()).start()
            except KeyboardInterrupt:
                exit()


# ------------------ terrible daemon code for windows -------------------
if __name__ == '__main__':
    webshite = Webshite()

    Windows = sys.platform == 'win32'
    ProcessFileName = os.path.realpath(__file__)
    pidName = ProcessFileName.split('\\')[-1].replace('.py', '')

    if Windows:
        pidFile = 'c:\\Windows\\Temp\\' + pidName + '.pid'
    else:
        pidFile = '/tmp' + pidName + '.pid'


    def start(pidfile, pidname):
        """ Create process file, and save process ID of detached process """
        pid = ""
        if Windows:
            # start child process in detached state
            DETACHED_PROCESS = 0x00000008
            p = subprocess.Popen([sys.executable, ProcessFileName, "child"],
                                 creationflags=DETACHED_PROCESS)
            pid = p.pid

        else:
            p = subprocess.Popen([sys.executable, ProcessFileName, "child"],
                                 stdout=PIPE, stderr=PIPE)
            pid = p.pid

        print("Service", pidname, pid, "started")
        # create processfile to signify process has started
        with open(pidfile, 'w') as f:
            f.write(str(pid))
        f.close()
        os._exit(0)


    def stop(pidfile, pidname):
        """ Kill the process and delete the process file """
        procID = ""
        try:
            with open(pidfile, "r") as f:
                procID = f.readline()
            f.close()
        except IOError:
            print("process file does not exist, but that's ok <3 I still love you")

        if procID:
            if Windows:
                try:
                    killprocess = subprocess.Popen(['taskkill.exe', '/PID', procID, '/F'],
                                                   stdout=PIPE, stderr=PIPE)
                    killoutput = killprocess.communicate()

                except Exception as e:
                    print(e)
                    print("could not kill ", procID)
                else:
                    print("Service", pidname, procID, "stopped")

            else:
                try:
                    subprocess.Popen(['kill', '-SIGTERM', procID])
                except Exception as e:
                    print(e)
                    print("could not kill " + procID)
                else:
                    print("Service " + procID + " stopped")

            # remove the pid file to signify the process has ended
            os.remove(pidfile)


    if len(sys.argv) == 2:

        if sys.argv[1] == "start":

            if os.path.isfile(pidFile) == False:
                start(pidFile, pidName)
            else:
                print("process is already started")

        elif sys.argv[1] == "stop":

            if os.path.isfile(pidFile) == True:
                stop(pidFile, pidName)
            else:
                print("process is already stopped")

        elif sys.argv[1] == "restart":
            stop(pidFile, pidName)
            start(pidFile, pidName)

        # This is only run on windows in the detached child process
        elif sys.argv[1] == "child":
            webshite.run()
    else:
        print("usage: python " + pidName + ".py start|stop|restart")

# kill main
os._exit(0)
