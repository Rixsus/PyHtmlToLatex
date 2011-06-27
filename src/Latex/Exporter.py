

from subprocess import Popen, PIPE
import os
import sys


class Export:
    def __init__(self, latex, conf):
        self._latex = latex
        self._conf = conf

    def write(self):
        file = None
        try:
            #make dirs 
            if not os.path.isdir(os.path.dirname(self._conf.destination)):
                os.makedirs(os.path.dirname(self._conf.destination), exist_ok = True)
            #create file
            file = open(self._conf.destination, "w",encoding="utf8")    #ascii encoding is valid utf8 encoding :)
            writedata = self._latex.data()
            #write data
            file.write(writedata)
        except IOError:
            sys.stderr.write("Problem with saving file, please check saving path and it's permission")
            sys.exit(1)
        finally:
            if file:
                #close even after errors
                file.close()

        if self._conf["compile"]:
            LaTeX = Popen((self._conf["latex"] , self._conf.destination), stdout = PIPE, stderr = PIPE, cwd = self._conf.destination_dir).wait()
            if self._conf["open"]:

                dest = self._conf.destination[:self._conf.destination.rfind(".")]
                if self._conf["latex"] == "latex":
                    dest += ".dvi"
                else:
                    dest += ".pdf"
                viewer = Popen(("/usr/bin/xdg-open", dest))
