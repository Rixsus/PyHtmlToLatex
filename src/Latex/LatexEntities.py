
import sys
import re
import os
from Latex.Constans import name2latex, code2latex
from Latex.CssEntities import CSSData
from html.entities import codepoint2name
from subprocess import Popen, PIPE
import ConfigManager








def tag_choice(entity, config):
    le = None
    if entity.tag == "p":
        le = LatexP(entity, config)
    elif entity.tag == "a":
        le = LatexA(entity, config)
    elif entity.tag == "br":
        le = LatexBr(entity, config)
    elif entity.tag == "b":
        le = LatexB(entity, config)
    elif entity.tag == "big":
        le = LatexBig(entity, config)
    elif entity.tag == "tt":
        le = LatexTt(entity, config)
    elif entity.tag == "u":
        le = LatexU(entity, config)
    elif entity.tag == "var":
        le = LatexVar(entity, config)
    elif entity.tag == "strong":
        le = LatexStrong(entity, config)
    elif entity.tag == "i":
        le = LatexI(entity, config)
    elif entity.tag == "small":
        le = LatexSmall(entity, config)
    elif entity.tag == "s":
        le = LatexS(entity, config)
    elif entity.tag == "samp":
        le = LatexSamp(entity, config)
    elif entity.tag == "strike":
        le = LatexStrike(entity, config)
    elif entity.tag == "center":
        le = LatexCenter(entity, config)
    elif entity.tag == "blockquote":
        le = LatexBlockquote(entity, config)
    elif entity.tag == "q":
        le = LatexQ(entity, config)
    elif entity.tag == "img":
        le = LatexImg(entity, config)
    elif entity.tag == "abbr":
        le = LatexAbbr(entity, config)
    elif entity.tag == "acronym":
        le = LatexAcronym(entity, config)
    elif entity.tag == "code":
        le = LatexCode(entity, config)
    elif entity.tag == "cite":
        le = LatexCite(entity, config)
    elif entity.tag == "em":
        le = LatexEm(entity, config)
    elif entity.tag == "hr":
        le = LatexHr(entity, config)
    elif entity.tag == "kbd":
        le = LatexKbd(entity, config)

    elif entity.tag == "sub":
        le = LatexSub(entity, config)
    elif entity.tag == "sup":
        le = LatexSup(entity, config)


    elif entity.tag == "dl":
        le = LatexDl(entity, config)
    elif entity.tag == "dt":
        le = LatexDt(entity, config)
    elif entity.tag == "dd":
        le = LatexDd(entity, config)
    elif entity.tag == "dfn":
        le = LatexDfn(entity, config)
    elif entity.tag == "li":
        le = LatexLi(entity, config)
    elif entity.tag == "ol":
        le = LatexOl(entity, config)
    elif entity.tag == "ul":
        le = LatexUl(entity, config)

    elif entity.tag == "h1":
        le = LatexH1(entity, config)
    elif entity.tag == "h2":
        le = LatexH2(entity, config)
    elif entity.tag == "h3":
        le = LatexH4(entity, config)
    elif entity.tag == "h4":
        le = LatexH4(entity, config)
    elif entity.tag == "h5":
        le = LatexH5(entity, config)
    elif entity.tag == "h6":
        le = LatexH6(entity, config)

    elif entity.tag == "span":
        le = LatexSpan(entity, config)
    elif entity.tag == "div":
        le = LatexDiv(entity, config)

    elif entity.tag == "del":
        #ignore tag
        pass
    elif entity.tag == "ins":
        #we just ignore tag and continue parsing
        le = LatexEntity(entity, config)
    elif entity.tag == "form":
        #ignore tag
        sys.stderr.write("Forms not yet implemented, ignoring...\n")
    elif entity.tag == "frameset":
        #TODO: implement frameset
        sys.stderr.write("Frameset not implemented, ignoring...\n")

    elif entity.tag == "dir":
        le = LatexDir(entity, config)
    elif entity.tag == "menu":
        le = LatexMenu(entity, config)

    elif entity.tag == "table":
        #le = LatexTable(entity, config)
        le = Table(entity, config)
    elif entity.tag == "font":
        le = LatexFont(entity, config)
    elif entity.tag == "pre":
        le = LatexPre(entity, config)
    elif entity.tag == "script":
        #ignore
        pass
    else:
        #ignore tag and continue parse inner elements
        le = LatexEntity(entity, config)

    return le


_LxText_special_char = re.compile(r"([\\#\$%&_\{\}~\^])")
_LxText_unicode = re.compile(r"[^\x00-\x7F]")
class LxText():
    """add escape characer to text, for latex processing"""
    def __init__(self, text):
        """Convert escape characters"""
        #TODO: compile characters
        self._text = re.sub(_LxText_special_char, self._match, text)         #match latex special characters
        config = ConfigManager.ProgConf.ProgramConfig()
        if config["ascii"]:
            self._text = re.sub(_LxText_unicode, self._unicode, self._text)     #match unicode characters

    def _match(self, matchobj):
        """replace funcion called by __init__"""
        #TODO: create dictionary
        m = matchobj.group(0)
        if m == "\\":return r"$\backslash{}$"
        elif m == "#":return r"\#"
        elif m == "$":return r"\$"
        elif m == "%":return r"\%"
        elif m == "&":return r"\&"
        elif m == "_":return r"\_"
        elif m == "{":return r"\{"
        elif m == "}":return r"\}"
        elif m == "~":return r"\textasciitilde{}"
        elif m == "^":return r"\^"
    def _unicode(self, matchobj):
        m = matchobj.group(0)
        try:
            name = codepoint2name[ord(m)]
            if name2latex[name][1]:
                return "${0}$".format(name2latex[name][0])
            else:
                return name2latex[name][0]
            #TODO:add desired package
        except KeyError:
            try:
                if code2latex[ord(m)][1]:
                    return "${0}$".format(code2latex[ord(m)][0])
                else:
                    return code2latex[ord(m)][0]
            except Exception:
                sys.stderr.write("Unknown character:{0}\n".format(m))
                return ""   # we do not know character so we just ignore it...

    def __str__(self):
        return self._text
    def __add__(self, string):
        return self._text + string
    def __radd__(self, string):
        return string + self._text


class LatexEntity():
    """Base class for htmltolatex conversion"""
    def __init__(self, html, config, preTag = False, tableTag = False):
        """Initilize children elements
        html-instance of HTMLEntity"""
        self._children = []
        self._config = config
        self._html = html
        self._parent = None
        #html and config
        if not config["nocss"]:
            self._css = CSSData(html, config)
        for i in html:
            le = None
            if not isinstance(i, str):
                if i.tag == "@htmlref":
                    try:
                        if name2latex[str(i)][1]:
                            le = "$" + name2latex[str(i)][0] + "$"
                            if preTag:
                                le = "\\(" + name2latex[str(i)][0] + "\\)"
                        else:
                            le = name2latex[str(i)][0]
                        self._config.add_package(name2latex[str(i)][2])
                    except KeyError:
                        sys.stderr.write("Entity {} not supported".format(str(i)))
                    except TypeError:
                        sys.stderr.write("Not yet implemented")
                    except IndexError:
                        #don't add package
                        pass
                    except AttributeError:
                        pass
                else:
                    le = tag_choice(i, config)
                    le._parent = self
            else:
                #add escape character to special characters in latex
                if html.tag != "pre":
                    #delete extra spaces and new li
                    #TODO: one regex
                    i = re.sub("(\n)", " ", i)
                    i = re.sub("([ ]{2,})", " ", i)
                    #i = i.rstrip()
                self._children.append(LxText(i))


            if hasattr(self, "_pre") and isinstance(le, LatexEntity) and le:
                #parse subelement in pre tag according pre rules
                le._pre = True
            if hasattr(self, "_table") and isinstance(le, LatexEntity) and le:
                le._table = True
            if le:
                self._children.append(le)
    def to_latex(self):
        """This method should be implemented in derived class"""
        return  "".join(str (x) for x in self._children)

    def pre_tag_text(self):
        def _to_pre_tag(element):
            if not isinstance(element, str):
                try:
                    return element.pre_tag_text()
                except AttributeError:
                    return str(element)
            else:
                #string
                if element[0] == "$" and element[-1] == "$":
                    #postprocessing
                    return "\\(" + element[1:-1] + "\\)"
                else:
                    return element
        if hasattr(self, "_children"):
            return  "".join(_to_pre_tag(x) for x in self._children)
        else:
            return ""

    def plain_text(self):
        """TODO:return pure text withou any formating options"""
        def _to_plain_str(element):
            """Define function for plain text"""
            if hasattr(element, "plain_text"):
                return element.plain_text()
            return str(element)
        if hasattr(self, "_children"):
            return  "".join(_to_plain_str(x) for x in self._children)
        else:
            return ""

    def __str__(self):
        if not hasattr(self, "_css") or self._css.length == 0:
            return self.to_latex()
        else:
            if self._css.replace:
                #TODO: add handling
                pass
            else:
                #we just add some beginning and ending
                return "{0}{1}{2}".format(self._css.begin, self.to_latex().lstrip(), self._css.end)






class LatexBody(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        #TODO: !!!!!!!!!
        return "\\begin{document}\n" + "".join(str (x) for x in self._children) + "\n\\end{document}"

class LatexBlockquote(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\n\\\begin{quotation}\n" + "".join(str (x) for x in self._children) + "\n\\end{quotation}"

class LatexQ(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\begin{0}quote{1}{2}\\end{0}quote{1}".format("{", "}", "".join(str(x) for x in self._children))


class LatexCenter(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\n\\begin{center}\n" + "".join(str (x) for x in self._children) + "\n\\end{center}"


class LatexBr(LatexEntity):
    def __init__(self, html, config):
        #Do nothing
        pass
    def to_latex(self):
        par = self._parent
        while par:
            if isinstance(par, TabCell):
                return "\\newline\n"
            par = par._parent
        else:
            return "\\\\\n"

class LatexHr(LatexEntity):
    def __init__(self, html, config):
        #Do nothing
        pass
    def to_latex(self):
        return "\n\n\\line(1,0){400}\n"

class LatexCite(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\textit{0}{1}{2}".format("{", "".join(str(x) for x in self._children), "}")

class LatexEm(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\emph{0}{1}{2}".format("{", "".join(str(x) for x in self._children), "}")

class LatexTt(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        if hasattr(self, "_a"):
            return "".join(str(x) for x in self._children)
        return "\\texttt{0}{1}{2}".format("{", "".join(str(x) for x in self._children), "}")

class LatexVar(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\texttt{0}{1}{2}".format("{", "".join(str(x) for x in self._children), "}")

class LatexStrong(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\textbf{0}{1}{2}".format("{", "".join(str(x) for x in self._children), "}")

class LatexI(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\textit{0}{1}{2}".format("{", "".join(str(x) for x in self._children), "}")

class LatexU(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\underline{0}{1}{2}".format("{", "".join(str(x) for x in self._children), "}")

class LatexKbd(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\texttt{0}{1}{2}".format("{", "".join(str(x) for x in self._children), "}")

class LatexDir(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\n\\begin{0}itemize{1}{2}\n\\end{0}itemize{1}".format("{", "}", "".join(str(x) for x in self._children))
class LatexMenu(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\n\\begin{0}itemize{1}{2}\n\\end{0}itemize{1}".format("{", "}", "".join(str(x) for x in self._children))


class LatexHead(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        #TODO:dorobit
        return ""#"\n\\title{" + " ".join(str (x) for x in self._children) + "}\n"

class LatexP(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\n\n" + "".join(str (x) for x in self._children)

class LatexImg(LatexEntity):
    def __init__(self, html, config):
        self._html = html
        self._config = config
        #TODO: no image
        config.add_package("graphicx")
        if self._config["wrapfig"]:
            config.add_package("wrapfig")
    def to_latex(self):
        try:
            img = self._html.attrs["src"]
            figure = "figure"
            wrapconf = ""
            if self._config["wrapfig"]:
                figure = "wrapfigure"
                flt = "l"
                try:
                    if self._html.css.css["float"][0] == "right":
                        flt = "r"
                except Exception:
                    pass
                wrapconf = "{" + flt + "}{*}"

                try:
                    ident = Popen(("identify", os.path.join(self._config.destination_dir, img)), stdout = PIPE)
                    text = ident.communicate()[0].decode()
                    matchobj = re.search("(\s\d*x\d*\s)", text)     #find image image height and width    e.g.100x100
                    height = int(matchobj.group(0).split("x")[0]) + 5
                    wrapconf = "{" + flt + "}{" + str(height) + "px}"
                    if height > 400: #really large images
                        #do not use wrapfig!
                        wrapconf = ""
                        figure = "figure"
                except Exception:
                    #we try identify tool from imagemagick
                    try:
                        import Image #try import PIL used to get image size
                        im = Image.open(os.path.join(self._config.destination_dir, img))
                        wrapconf = "{" + flt + "}{" + str(im.size[0] + 5) + "px}"
                    except Exception:
                        sys.stderr.write("Error with getting information about image file. Please install PIL or ImageMagick to support wrapfigure\n")
            #return r"\includegraphics{" + img + "}"
            #maybe convert text by LxText, need more testing
            return "\\begin{0}{1}{2}{3}\n\\includegraphics{0}{4}{2}\n\\end{0}{1}{2}".format("{", figure, "}", wrapconf, img)
        except KeyError:
            return ""

    def include_image(self):
        """return only include image statement"""
        try:
            img = self._html.attrs["src"]
            return "\\includegraphics{" + img + "}"

        except Exception:
            return ""

class LatexA(LatexEntity):
    def __init__(self, html, config):
        self._a = True
        LatexEntity.__init__(self, html, config)
        config.add_package("hyperref")
    def to_latex(self):
        try:
            link = self._html.attrs["href"]
            if link[0] == "#":
                link = link[1:]
            if link[0:7] == "mailto:" or link[0:5] == "http:":
                #link outside document
                #check for images and only add them
                imgs = ""
                for i in self._children:
                    if isinstance(i, LatexImg):
                        imgs += i.include_image()
                body = self.plain_text().strip()
                if body == "":
                    return imgs + "\\url{" + link + "} "
                return imgs + "\\href{" + link + "}{" + body + "} "
            else:
                return "\\hyperref[" + link + "]{" + self.plain_text() + "} "
        except KeyError:
            try:
                return "\\phantomsection\n\\label{0}{1}{2} {3}".format("{", self._html.attrs["name"], "}", self.plain_text())
            except KeyError:
                return ""

class LatexEnviroment(LatexEntity):
    def __init__(self, html, config, enviroment):
        LatexEntity.__init__(self, html, config)
        self._env = enviroment
    def to_latex(self):
        return "\\{0}{1}{2}{3}".format(self._env, "{", "".join(str(x) for x in self._children), "}")


class LatexAbbr(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\texttt{" + "".join(str (x) for x in self._children) + "}"

class LatexAcronym(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\texttt{" + "".join(str (x) for x in self._children) + "}"

class LatexB(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\textbf{" + "".join(str (x) for x in self._children) + "}"

class LatexS(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\sout{0}{1}{2}".format("{", "".join(str(x) for x in self._children), "}")

class LatexSamp(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\texttt{0}\n{1}\n{2}".format("{", "".join(str(x) for x in self._children), "}")

class LatexStrike(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\sout{0}{1}{2}".format("{", "".join(str(x) for x in self._children), "}")

class LatexBig(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\LARGE {0}\\normalsize{1}".format("".join(str (x) for x in self._children), "{}")

class LatexSmall(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\footnotesize {0}\\normalsize{1}".format("".join(str (x) for x in self._children), "{}")

class LatexCode(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        if hasattr(self, "_pre"):

            return "".join(str (x) for x in self._children)
        return "\\texttt{" + "".join(str (x) for x in self._children) + "}"


class LatexDl(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\n\\begin{description}" + "".join(str (x) for x in self._children) + "\n\\end{description}"
class LatexDt(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\n\t\\item[" + "".join(str (x) for x in self._children) + "]"
class LatexDd(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "".join(str (x) for x in self._children)
class LatexDfn(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\\textit{" + "".join(str (x) for x in self._children) + "}"

class LatexLi(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\n\t\\item {0}".format("".join(str(x) for x in self._children))

class LatexOl(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\n\\begin{0}enumerate{1}{2}\n\\end{0}enumerate{1}".format("{", "}", "".join(str(x) for x in self._children))

class LatexUl(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        """
        \begin{itemize}
        TEXT
        \end{itemize}
        """
        return "\n\\begin{0}itemize{1}{2}\n\\end{0}itemize{1}".format("{", "}", "".join(str(x) for x in self._children))

class LatexSpan(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "".join(str (x) for x in self._children)
class LatexDiv(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "".join(str (x) for x in self._children)

class LatexH1(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\n\n\\section*{" + "".join(str (x) for x in self._children) + "}"

class LatexH2(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\n\n\\subsection*{" + "".join(str (x) for x in self._children) + "}"

class LatexH3(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\n\n\\subsubsection*{" + "".join(str (x) for x in self._children) + "}"

class LatexH4(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\n\n\\paragraph*{" + "".join(str (x) for x in self._children) + "}"

class LatexH5(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\n\n\\subparagraph*{" + "".join(str (x) for x in self._children) + "}"

class LatexH6(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "\n\n\\subparagraph*{" + "".join(str (x) for x in self._children) + "}"

class LatexSub(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "$_{0}$".format("".join(str (x) for x in self._children))
class LatexSup(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "$^{0}$".format("".join(str (x) for x in self._children))

#TODO:
class LatexTable(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):

        rows = 0
        columns = []
        #rows
        for i in self._children:
            if isinstance(i, LatexTr):
                rows += 1
                columns.append(i.columns)

        table = "\\begin{table}[h]\n\\begin{tabular}{|" + "c|" * max(columns) + "}\n\\hline\n"
        table += "".join(str (x) for x in self._children)
        table += "\n\\end{tabular}\n\\end{table}"
        return table

class LatexTr(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
        self._col = 0
        for i in self._children:
            if isinstance(i, LatexTd):
                self._col += 1
    def to_latex(self):
        text = ""
        for i in self._children:
            if isinstance(i, LatexTd):
                text += str(i) + " & "
        return text[:-2] + "\\\\ \\hline\n"
    @property
    def columns(self):
        return self._col


class LatexTd(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        try:
            colspan = self._html.attrs["colspan"]
            if colspan == 0:
                raise KeyError
            return "\\multicolumn{" + colspan + "}{|c|}{" + "".join(str (x) for x in self._children) + "}"
        except KeyError:
            return "".join(str (x) for x in self._children)


class LatexTh(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "".join(str (x) for x in self._children)
class LatexThead(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "".join(str (x) for x in self._children)
class LatexTfoot(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "".join(str (x) for x in self._children)
class LatexTbody(LatexEntity):
    def __init__(self, html, config):
        LatexEntity.__init__(self, html, config)
    def to_latex(self):
        return "".join(str (x) for x in self._children)


class LatexFont(LatexEntity):
    def __init__(self, html, config):
        #don't duplicit!! we just use css
        if "color" in html.attrs:
            html.css.css["color"] = [html.attrs["color"]]
        if "size" in html.attrs:
            fonts = ["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"]
            fontsize = 4
            try:
                fontsize = int(html.attrs["size"])
            except IndexError:
                fontsize = 7
            except Exception:
                pass
            html.css.css["text-size"] = [fonts[fontsize - 1]]
        LatexEntity.__init__(self, html, config)

    def to_latex(self):
        return "".join(str (x) for x in self._children)

class LatexPre(LatexEntity):
    def __init__(self, html, config):
        #self._pre = True
        LatexEntity.__init__(self, html, config)
        config.add_package("alltt")
    def to_latex(self):
        text = "\n\\begin{alltt}\n" + self.pre_tag_text() + "\n\\end{alltt}\n"
        return text





class TabCell(LatexEntity):
    def __init__(self, html, config, structure = None):
        self._init_values(html, config)
        self._special = False
        self._table = True
        LatexEntity.__init__(self, html, config)
        self._text = "".join(str (x) for x in self._children)
        self._structure = None

    def _init_values(self, html, config):
        """Init common values for lates use"""
        if html.tag == "th":
            self._heading = True
        else:
            self._heading = False
        #try to get align in cell
        try:
            if html.attrs["align"][0] in ("l", "c", "r"):     #left center and right
                self._align = html.attrs["align"][0]  #firt letter from left,right,center
            else:
                self._align = "c"
        except KeyError:
            self._align = "c"
        #try to get valign in cell
        try:
            if html.attrs["valign"][0] in ("t", "m", "b"):     #top middle bottom
                if html.attrs["valign"][0] == "m":
                    self._valign = "c"  #center
                else:
                    self._align = html.attrs["align"][0]  #top or bottom
            else:
                self._valign = None
        except KeyError:
            self._valign = None

        #background color
        try:
            self._bgcolor = html.attrs["bgcolor"]
        except KeyError:
            self._bgcolor = None
        #colspan
        try:
            self._colspan = int(html.attrs["colspan"])
        except (KeyError, ValueError):
            self._colspan = None
        #rowspan
        try:
            self._rowspan = int(html.attrs["rowspan"])
            if self._rowspan > 0:
                config.add_package("multirow")
        except (KeyError, ValueError):
            self._rowspan = None

    @property
    def columnspan(self):
        if self._colspan:
            return self._colspan
        else:
            return 1
    @property
    def rowspan(self):
        if self._rowspan:
            return self._rowspan
        else:
            return 1
    @property
    def special(self):
        """Return if this cell is special, contains for example some other enviroment... for example itemize,enumerate,..."""
        return self._special
    @property
    def text(self):
        return self._text
    @property
    def align(self):
        return self._align

class RowSpanFiller():
    def __init__(self, colspan = 1):
        self._colspan = colspan
    def to_latex(self):
        return " "
    @property
    def columnspan(self):
        return self._colspan
    @property
    def rowspan(self):
        return 1
    @property
    def special(self):
        """Return if this cell is special, contains for example some other enviroment... for example itemize,enumerate,..."""
        return False
    @property
    def text(self):
        return " "
    @property
    def align(self):
        #TODO: remove
        return "c"
    def __str__(self):
        return " "

class TableRows:
    def __init__(self, table, config):
        self._config = config
        self._table = table
        self._count = 0
        self._rows = [[]]     #list of lists

    def add_row(self, html):
        #we only need only th and td tag
        for i in html:
            if not isinstance(i, str):      #we want only tags
                if i.tag == "td" or i.tag == "th":
                    self._rows[-1].append(TabCell(i, self._config))
        self._rows.append([])   #new row
        self._count += 1          #number of rows

    def row_count(self):
        return len(self._rows)

    def _add_filler(self, row, column, object):
        #j->column
        cur_column = 0
        for j in range(len(self._rows[row])):
            if cur_column >= column:
                self._rows[row].insert(cur_column, object)
                break
            else:
                cur_column += self._rows[row][j].columnspan

    def _create_square(self):
        """We just push None values to row and then complete multirow"""
        #we need to know row so 
        #i-> number of row, j->number of column, k->counter how much rows
        rows = self._rows
        for i in range(len(rows)):
            cur_pos = 0
            for j in range(len(rows[i])):
                if rows[i][j].rowspan > 1:
                    self._config.add_package("multirow")
                    try:
                        for k in range(1, rows[i][j].rowspan):
                            self._add_filler(i + k, cur_pos, RowSpanFiller(rows[i][j].columnspan))
                    except IndexError:
                        self._rows.append([])
                        #TODO:more control, just ignore
                        self._rows[-1].append(RowSpanFiller(rows[i][j].columnspan))

                cur_pos += rows[i][j].columnspan


    def _row_column(self, row):
        """Get number of columns in row"""
        return sum([x.columnspan for x in row])

    def _get_align(self, maxcol):
        def max_count(col_dict):
            if col_dict['c'] >= col_dict['l']:
                if col_dict['c'] >= col_dict['r']:
                    return 'c'
                else:
                    return 'r'
            else:
                if col_dict['l'] >= col_dict['r']:
                    return "l"
                else:
                    return "r"
        """Get optimal align based on use in columns"""
        tmpdic = {"l":0, "c":0, "r":0}
        align = []
        #get some more aligns
        for i in range(maxcol):
            align.append(dict(tmpdic))  #append copy of tmpdict

        for i in self._rows:
            #we are going for each row
            #we are on firt cell
            curpos = 0
            for j in i:
                #and each cell in row
                if j is not None:
                    #ignore none objects
                    if j.columnspan == 1:
                        #we are interested only in normal column, not multispan
                        align[curpos][j.align] += 1
                        curpos += 1
                    else:
                        curpos += j.columnspan
                else:
                    curpos += 1
        #now we have some numbers lets return it as list
        return tuple(map(max_count, align))

    def _create_table(self):
        #get maximum number of columns
        self._create_square()
        mx = max([self._row_column(row) for row in self._rows])
        self._column_count = mx
        self._align = self._get_align(mx)
        for i in self._rows:
            i.extend([None] * (mx - self._row_column(i)))
        self._table = self._rows
        self._created = True

    def create(self):
        if not hasattr(self, "_created"):
            self._create_table()

    @property
    def table(self):
            return self._table
    @property
    def align(self):
        return self._align
    @property
    def column_count(self):
        return self._column_count

class Table:
    class _Cline_concat():
        """Class for formating cline statements"""
        def __init__(self, max_column):
            self._numbers = []
            self._max_column = max_column
        def add(self, numbers):
            """Add numbers to array(list,tuple)"""
            self._numbers.extend(numbers)
        def get_cline(self):
            """Main method, which create cline command"""
            if not self._numbers:
                return "\\hline "
            else:
                ret = []
                #temporary item for storing cline numbers
                tmp_col = []
                #xor 2 lists
                for i in range(1, self._max_column + 1):
                    if i not in self._numbers:
                        tmp_col.append(i)

                beginning = tmp_col[0]
                #init item
                item = None

                for i in tmp_col:
                    if item is None or i == item + 1 :
                        item = i
                    else:
                        ret.append("\\cline{0}{1}-{2}{3} ".format("{", str(beginning), str(i), "}"))
                        item = i
                        beginning = i
                if item != beginning:
                    ret.append("\\cline{0}{1}-{2}{3} ".format("{", str(beginning), str(tmp_col[-1]), "}"))
                return "".join(ret)


    def __init__(self, html, config):
        rows = TableRows(self, config)
        self._config = config

        #border
        try:
            self._border = html.attrs["border"]
        except KeyError:
            self._border = 0    #we want default border->nothing
            #border in css
            for key, value in html.css.css.items():
                #css in table
                if key == "border":
                    if value[0] != "0":
                        self._border = 1


        #in table we have only th,td and tr tag, we ignore rest
        for i in html:
            if not isinstance(i, str):      #we want only tags
                if i.tag == "tr":
                    rows.add_row(i)  #we send only related data -> columns
                if i.tag in ("thead", "tbody", "tfoot"):
                    for j in i:
                        if not isinstance(j, str):      #we want only tags
                            if j.tag == "tr":
                                rows.add_row(j)  #we send only related data -> columns
        #create table
        rows.create()
        self._align = rows.align
        self._table = rows.table
        self._column_count = rows.column_count

    def _hline(self):
        if int(self._border) == 0:
            return ""
        else:
            return "\\hline "

    def _vert_lin(self):
        if int(self._border) == 0:
            return ""
        else:
            return "|"
    #classic definition
    #TODO: create metaclass
    def to_latex(self):
        #used table
        usedtable = "tabular"
        if self._config["longtable"]:
            usedtable = "longtable"
        beginning = "\\begin{table}[h]\n\\catcode`\\-=12 %problem with babel package \n\\begin{" + usedtable + "}"
        align = "{" + self._vert_lin() + self._vert_lin().join(self._align) + self._vert_lin() + "}\n"
        table = self._table
        body = ""
        for i in range(len(table)):
            #ignore empty row
            if not any(table[i]):
                break

            text = ""
            cline = self._Cline_concat(self._column_count)
            for j in range(len(table[i])):
                if table[i][j] is None:
                    cline.add([j + 1])
                elif isinstance(table[i][j], RowSpanFiller):
                    cline.add(range(j + 1, j + table[i][j].columnspan + 1))

                if table[i][j] is None:
                    text = text + " & "
                else:
                    if table[i][j].columnspan > 1:
                        #TODO: align
                        text = text + "\\multicolumn{" + str(table[i][j].columnspan) + "}{" + self._vert_lin() + "c" + self._vert_lin() + "}{"
                        if table[i][j].rowspan > 1:
                            text = text + "\\multirow{" + str(table[i][j].rowspan) + "}{*}{" + table[i][j].to_latex() + "}} & "
                        else:
                            text = text + table[i][j].to_latex() + "} & "
                    elif table[i][j].rowspan > 1:
                        text = text + "\\multirow{" + str(table[i][j].rowspan) + "}{*}{" + table[i][j].to_latex() + "} & "
                    else:
                        text = text + table[i][j].to_latex() + " & "
            #clines
            if int(self._border) != 0:
                body = body + cline.get_cline() + "\n" + text[:-2]
            else:
                body = body + "\n" + text[:-2]

            #new line
            body = body + " \\\\ "

            body = body + "\n"


        end = self._hline() + "\n\\end{" + usedtable + "}\\end{table}\n"
        return beginning + align + body + end
        #Don't forget add :
        #\catcode`\-=12

    def plain_text(self):
        return ""

    def __str__(self):
        return self.to_latex()

