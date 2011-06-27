#!/usr/bin/python


from Parser.HtmlDataParser import HtmlDataParser
from Latex.Convertor import LatexDocument
from ConfigManager.ProgConf import ProgramConfig, ImageNotSupported,\
    InternetPathException
import argparse
import sys
from Latex.Exporter import Export




if __name__ == '__main__':
    argpar = argparse.ArgumentParser(description = "Convert HTML/XHTML file to LaTeX")

    #argumenets and options
    #
    argpar.add_argument("input_file", help = "Input html file", metavar = "InputFile")
    #argpar.add_argument("output_file", help = "Output LaTeX file", metavar = "OutputFile")
    argpar.add_argument("--output", help = "Output LaTeX file", metavar = "OutputFile")
    argpar.add_argument("--encoding", help = "Encoding of html file")
    argpar.add_argument("--lang", help = "Custom language configuration")
    argpar.add_argument("--utf8x", help = "Use utf8x package instead utf8", action = "store_const", const = True)
    argpar.add_argument("--ascii", help = "Use only ASCII encoding for latex file", action = "store_const", const = True)
    argpar.add_argument("--nooverwrite", help = "Don't overwrite files in directory", action = "store_const", const = True)
    argpar.add_argument("--noimage", help = "Ignore images in html", action = "store_const", const = True)
    argpar.add_argument("--latex", help = "Compile document with latex instead pdflatex", action = "store_const", const = True)
    argpar.add_argument("--compile", help = "Complile document", action = "store_const", const = True)
    argpar.add_argument("--image", help = "Prefered image format for pdflatex", choices = ("jpg", "png"))        #TODO: add pdf and eps
    argpar.add_argument("--noconfig", help = "Do not load configuration file", action = "store_true")           #don'l load or create config file
    argpar.add_argument("--configfile", help = "Use custom config file", default = "~/.PyHtmlToLatex.cfg")           #don'l load or create config file
    argpar.add_argument("--open", help = "Open document after compilation", action = "store_true")
    argpar.add_argument("--nocss", help = "Do not try parse css files", action = "store_const", const = True)
    argpar.add_argument("--longtable", help = "Use longtable package instead tabular", action = "store_const", const = True)
    argpar.add_argument("--euro", help = "Use custom package for euro symbol", choices = ("eurosym", "eurofont", "eurosans", ""))
    argpar.add_argument("--nowasysym", help = "Do not use wasysym package, ignore all charactests used from it", action = "store_const", const = False)
    argpar.add_argument("--nowrapfig", help = "Do not wrap text around images", action = "store_const", const = False)
    argpar.add_argument("--color", help = "Use color", action = "store_const", const = True)
    argpar.add_argument("--stdout", help = "Use color", action = "store_const", const = True)
    argpar.add_argument("--verbose", help = "Be verbose", action = "store_const", const = True)
    argpar.add_argument("--form", help = "Try parse HTML forms", action = "store_const", const = True)
    argpar.add_argument("--wget", help = "Download internet page via wget", action = "store_const", const = True)
    
    args = argpar.parse_args()
    if args.open:
        args.compile = True
    #only for reaaaly big pages
    sys.setrecursionlimit(10000)

    try:
        conf = ProgramConfig(args)
    except ImageNotSupported:
        print("Image not supported with latex\n")
        argpar.print_help()
        sys.exit(1)
    except InternetPathException:
        print("Please specificate output file\n")
        argpar.print_help()
        sys.exit(1)
    except:
        print("Path does not exist\n")
        argpar.print_help()
        sys.exit(1)

    htmlPar = HtmlDataParser(conf)
    latex = LatexDocument(htmlPar.HTMLDocument, conf)
    exp = Export(latex, conf)
    exp.write()
