

import os
import sys
import Latex.Constans
from ConfigManager.ConfigPar import ConfigPar
from ConfigManager.ConfPackage import ConfPackage
from urllib.parse import urlsplit



class PathException(Exception):pass
class PathNotFound(PathException):pass
class ImageNotSupported(Exception):pass

#TODO: more exceptions



class ProgramConfig:
    """Singlton Class
    Store all configuration data used in program, singlton instance"""
    def __init__(self, args = None):
        """Inicialize one and only instance of config (singlton)"""
        #initialize private members
        if args is None:
            return
        self._encoding = args.encoding
        self._config = {}
        #initialize configuration
        self._conf_parser = ConfigPar(args)

        #curent working dir or destination
        if args.output_file:
            #destiantion
            self._dest = os.path.realpath(os.path.expanduser(args.output_file))

            #TODO: new exception
            if not os.path.basename(self._dest):
                raise PathException()
        else:
            #join CWD and name of source with .tex extension
            self._dest = os.path.join(os.getcwd(), os.path.basename(args.input_file) + ".tex")


        if args.input_file[0:5] == "http:":
            self._source = args.input_file
            self._internet = True
        else:
            self._source = os.path.realpath(os.path.expanduser(args.input_file))
            self._internet = False
            if not os.path.isfile(self._source):
                raise PathException()

        #create configuration
        self._create_config(args)

        #other definitions
        self._other = []
        #package config
        self._packages = []
        self._packages.append(ConfPackage("a4wide"))
        self._packages.append(ConfPackage("inputenc", "utf8"))
        #add country specific packages -> babel,fontenc
        self._packages.extend(self._country_settings(args.lang))
        self._added_packages = []

        #used colors
        self._defined_colors = dict()   #color_name:color_code



    def add_package(self, package, *opt):
        #TODO: add case sensitivity, control if exists
        #TODO: add forbidden packages
        for i in self._packages:
            if i.package == package:
                #we found package so we add missing options
                if not opt:
                    return True
                for j in opt:
                    if not i.has_option(j):
                        i.add_option(j)
                return True
        if opt:
            self._packages.append(ConfPackage(package, *opt))
        else:
            self._packages.append(ConfPackage(package))
        return True

    def add_color(self, html_color, name):
        """Add color to used color, if there is no name for color, method will generate some name"""
        self.add_package("color")
        #hex->dec
        if len(html_color) == 4:  #triple color code
            color = (int(html_color[1], 16), int(html_color[2], 16), int(html_color[3], 16))
        else:
            color = (int(html_color[1:3], 16), int(html_color[3:5], 16), int(html_color[5:7], 16))
        #get name
        if name:
            if name in self._defined_colors and self._defined_colors[name] == color:
                return name         #we have already defined this color
            if name in self._defined_colors and not self._defined_colors[name] == color:
                #we have same name but different color codes, so we create new name by adding number to it
                i = 1
                while name + str(i) in self._defined_colors:
                    i += 1
                self._defined_colors[name + str(i)] = color
                self._other.append("\\definecolor{" + name + str(i) + "}{RGB}{" + ",".join((str(x) for x in color)) + "}")
                return name + str(i)
            #we have unique name so we just add it
            self._defined_colors[name] = color
            self._other.append("\\definecolor{" + name + "}{RGB}{" + ",".join((str(x) for x in color)) + "}")
            return name
        else:
            sys.stderr("Invalid name for color")

    def _create_config(self, args):
        """SETTING GLOBAL OPTIONS"""
        self._init_item("compile", args.compile)            #run pdflatex/latex after complete?
        self._init_item("nooverwrite", args.nooverwrite)    #overwrite existing files in directory?
        self._init_item("convertor", "convert")             #use imagemagick to convert images
        self._init_item("noimages", args.noimage)           #ignore images in html
        self._init_item("open", args.open)                  #open file after compilation
        self._init_item("nocss", args.nocss)                #don't parse css
        self._init_item("color", args.color)                #do non use color
        self._init_item("verbose", args.verbose)                #do non use color
        self._init_item("ascii", args.ascii)                #ascii characters

        #package settings
        self._init_package("longtable", args.longtable)        #use longtable enviroment
        self._init_package("euro", args.euro)
        self._init_package("wasysym", args.nowasysym)
        self._init_package("wrapfig", args.nowrapfig)
        #change constants:
        if self["euro"] != "eurosym":
            if self["euro"] == "":
                Latex.Constans.name2latex["euro"] = (r"", False)
            else:
                Latex.Constans.name2latex["euro"] = (r"\euro", False, self["euro"])


        if args.latex is None:
            #get data from config parser
            self._config["latex"] = "pdflatex"
            if args.image is None:
                #all supported format
                self._config["images"] = ["jpg", "png", "pdf"]
            else:
                #selected option
                self._config["images"] = [args.image]
        else:
            self._config["latex"] = "latex"
            self._config["images"] = ["eps"]
            if args.image is not None:
                raise ImageNotSupported()

    def _country_settings(self, lang):
        """return list of country settings package(babel,fontenc,..)"""
        ret = []
        if lang is None:
            lang = self._conf_parser.program_config("language")
        if lang in Latex.Constans.babel_lang:
            ret.append(ConfPackage("babel", lang))  #add babel package
        if lang == "slovak":
            ret.append(ConfPackage("fontenc", "T1"))
            self._other.append("\n\\chardef\\clqq=18 \\sfcode18=0\n\\chardef\\crqq=16 \\sfcode16=0\n\\def\\uv#1{\\clqq#1\\crqq}")
        elif lang == "czech":
            ret.append(ConfPackage("fontenc", "T1"))
        elif lang == "finnish":
            ret.append(ConfPackage("ae"))
        elif lang == "german":
            ret.append(ConfPackage("fontenc", "T1"))
        elif lang == "polish":
            ret.append(ConfPackage("polski"))
            #add dot after numbers in section, subsection, subssubsection
            self._other.append("\\renewcommand\\thesection{\\arabic{section}.}\n\\renewcommand\\thesubsection{\\arabic{section}.\\arabic{subsection}.}\n\\renewcommand\\thesubsubsection{\\arabic{section}.\\arabic{subsection}.\\arabic{subsubsection}.}")
        #TODO:add more languages

        return ret

    def _init_item(self, item, value):
        """Set value to item"""
        if value is None:
            #load data from config parser
            val = self._conf_parser.program_config(item)
            if val == "0":
                val = False
            elif val == "1":
                val = True
            self._config[item] = val
        else:
            self._config[item] = value

    def _init_package(self, item, value):
        """Set value to item"""
        if value is None:
            #load data from config parser
            val = self._conf_parser.package_config(item)
            if val == "0":
                val = False
            elif val == "1":
                val = True
            self._config[item] = val
        else:
            self._config[item] = value

    @property
    def latex_beginning(self):
        """Propery used for defining used packages and other configs"""
        return "{0}\n{1}\n".format("\n".join((str(x) for x in self._packages)), "\n".join((str(x) for x in self._other)))


    @property
    def destination_dir(self):
        return os.path.dirname(self._dest)
    @property
    def destination_file(self):
        return os.path.basename(self._dest)
    @property
    def destination(self):
        return self._dest
    @property
    def source_dir(self):
        if self.internet:
            splurl = urlsplit(self._source)
            return os.path.join(splurl.netloc, os.path.dirname(splurl.path)[1:])
        else:
            return os.path.dirname(self._source)
    @property
    def source(self):
        return self._source
    @property
    def encoding(self):
        return self._encoding
    @property
    def decoding(self):
        return self._decoding
    @property
    def internet(self):
        return self._internet

    def __setitem__(self, option, value):
        self._config[option] = value
    def __getitem__(self, option):
        if option in self._config:
            return self._config[option]
        else:
            return None

    #Implementation for singlton pattern
    __singl = None
    def __new__(cls, *args, **kwargs):
        if cls != type(cls.__singl):
            cls.__singl = object.__new__(cls, *args, **kwargs)
        return cls.__singl



