
import sys
from Latex.Constans import code2color, color2code



class css_base_class():
    def __init__(self, css, config):
        self._css = css
        self._config = config
        self._replace = False
    def _begin(self):
        """MUST override"""
        return ""
    def _end(self):
        """MUST override"""
        return ""
    @property
    def begin(self):
        return self._begin()
    @property
    def end(self):
        return self._end()


class css_color(css_base_class):
    """class for defining text color"""
    def __init__(self, css, config):
        css_base_class.__init__(self, css, config)
        self._replace = False
        self._color = css #we can have defined only 1 color

        name = ""
        code = ""
        if css[0] == "#":
            #we have hex interpretation
            name = code2color.get(css.upper(), "color")
            code = css
        else:
            #we have color name
            name = css
            try:
                code = color2code[name]
            except KeyError:
                sys.stderr.write("Undefined color\n")
        #add color
        self._color_name = config.add_color(code, name)
    def _begin(self):
        return "\\textcolor{" + self._color_name + "}{"
    def _end(self):
        return "}"

class css_text_size(css_base_class):
    """Class for handling font size"""
    def __init__(self, css, config):
        css_base_class.__init__(self, css, config)
        self._replace = False
        fonts = {"xx-small":"tiny", "x-small":"scriptsize", "small":"small", "medium":"normalsize", "large":"large", "x-large":"Large", "xx-large":"LARGE"}
        if css in fonts:
            self._font = fonts[css]
        else:
            sys.stderr.write("Unsupported format, Not yet implement\n")
    def _begin(self):
        return "{\\" + self._font + " "
    def _end(self):
        return "}"

class css_text_align(css_base_class):
    """Class for handling font align"""
    def __init__(self, css, config):
        css_base_class.__init__(self, css, config)
        self._align_env = ""
        if css == "left":
            self._align_env = "flushleft"
        elif css == "right":
            self._align_env = "flushright"
        elif css == "center":
            self._align_env = "center"
    def _begin(self):
        return "\n\\begin{" + self._align_env + "}\n"
    def _end(self):
        return "\n\\end{" + self._align_env + "}"


class css_text_decoration(css_base_class):
    """Class for handling font decoration"""
    def __init__(self, css, config):
        css_base_class.__init__(self, css, config)
        self._decoration = ""
        self._math_mode = False
        if css == "line-through":
            self._decoration = "sout"
        elif css == "underline":
            self._decoration = "underline"
        elif css == "overline":
            self._decoration = "overline"
            self._math_mode = True
        else:
            raise NotImplemented()
    def _begin(self):
        if self._math_mode:
            return "$\\" + self._decoration + "{"
        else:
            return "\\" + self._decoration + "{"
    def _end(self):
        if self._math_mode:
            return "}$"
        else:
            return "}"

class css_font_weight(css_base_class):
    """Class for handling font decoration"""
    def __init__(self, css, config):
        css_base_class.__init__(self, css, config)
        self._env = ""
        if css == "bold" or css == "bolder":
            self._env = "textbf"
        elif css == "normal" or css == "lighter":
            self._env = "textnormal"
        else:
            try:
                number = int(css)
                #100-400->normal    500-900->bold
                if number <= 400:
                    self._env = "textnormal"
                else:
                    self._env = "textbf"
            except Exception:
                raise NotImplemented()
    def _begin(self):
        return "\\" + self._env + "{"
    def _end(self):
        return "}"

class css_font_style(css_base_class):
    """Class for handling font decoration"""
    def __init__(self, css, config):
        css_base_class.__init__(self, css, config)
        self._env = ""
        if css == "normal":
            self._env = "textnormal"
        elif css == "italic":
            self._env = "textit"
        elif css == "oblique":
            self._env = "textsl"
    def _begin(self):
        return "\\" + self._env + "{"
    def _end(self):
        return "}"


class CSSData:
    def __init__(self, entity, config):
        self._replace_tag = False
        self._css_items = []
        #html entity->css enity->method of css entity->method of dict where are css stored
        for key, value in entity.css.css.items():
            try:
                if key == "color":
                    if config["color"]:
                        ent = css_color(value[0], config)   #only one value
                        self._css_items.append(ent)
                elif key == "text-size":
                    ent = css_text_size(value[0], config)
                    self._css_items.append(ent)
                elif key == "text-align":
                    ent = css_text_align(value[0], config)
                    self._css_items.append(ent)
                elif key == "text-decoration":
                    ent = css_text_decoration(value[0], config)
                    self._css_items.append(ent)
                elif key == "font-weight":
                    ent = css_font_weight(value[0], config)
                    self._css_items.append(ent)
                elif key == "font-weight":
                    ent = css_font_style(value[0], config)
                    self._css_items.append(ent)
            except Exception as e:
                if config["verbose"]:
                    sys.stderr.write(e.message)
    @property
    def begin(self):
        return "".join([x.begin for x in self._css_items])
    @property
    def end(self):
        return "".join([x.end for x in reversed(self._css_items)])
    @property
    def replace(self):
        return self._replace_tag
    @property
    def length(self):
        return len(self._css_items)
