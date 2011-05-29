

import re
from Latex.LatexEntities import LatexBody




class LatexDocument():
    def __init__(self, html, config):
        self._config = config
        #TODO:more config
        self._latex = []
        for i in html:
            if not isinstance(i, str) and i.tag == "html":
                for j in i:
                    if not isinstance(j, str):
                        #if j.tag == "head":
                            #self._latex.append(LatexHead(j, config))
                        if j.tag == "body":
                            self._latex.append(LatexBody(j, config))

    def add_html(self, html):
        for i in html:
            if not isinstance(i, str) and i.tag == "html":
                for j in i:
                    if not isinstance(j, str):
                        if j.tag == "body":
                            self._latex.append(LatexBody(j, self._config))


    def data(self):
        #return("".join(str (x) for x in self._latex))
        #TODO optimalise
        #try:
        text = "{0}\n{1}\n{2}\n".format("\\documentclass{article}\n", self._config.latex_beginning, "".join(str (x) for x in self._latex))
        #TODO: optimalization!!!
        text = re.sub(r"(\\\\\n\s*\\\\){1,}", r"\\\\", text, flags = re.MULTILINE)       #remove duplicit \\
        text = re.sub(r"(\\end\{\w*\})(?:\s*\\\\){1,}", r"\1", text, flags = re.MULTILINE)       #remove new line(\\) after \end{something}
        text = re.sub(r"(\\\\\n)(?:\s*)", r"\1", text, flags = re.MULTILINE)    #remove new line after \\
        text = re.sub(r"(\s*\\\\\s*)(?:\n)", r"\1", text)    #remove new line after \\
        text = re.sub(r"\$\$", "$ $", text)
        return text
        #except Exception as e:
            #sys.stderr.write("Problem with converting document:\n{0}".format(e))
            #sys.exit(1)
