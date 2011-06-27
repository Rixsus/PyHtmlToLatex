'''
Created on Apr 26, 2011

@author: rixsus
'''
import os, sys, configparser


class ConfigPar:
    def __init__(self, args):
        self._config = None
        self._args = args
        self._args.configfile = os.path.realpath(os.path.expanduser(self._args.configfile))
        if args.noconfig:
            #load default configuration
            self._default_config()
        else:
            if os.path.isfile(args.configfile):
                self._default_config()
                self._load_file()
            else:
                #try to create config file, with default values
                self._default_config()
                file = None
                try:
                    file = open(args.configfile, "w")
                    self._config.write(file)
                except Exception:
                    #cannot save config file, write error and continue
                    sys.stderr.write("Problem with saving configuration file\n")
                finally:
                    if file:
                        file.close()
    def _load_file(self):
        try:
            file = open(self._args.configfile, "r")
            self._config.read_file(file)
        except Exception:
            #add only ioerror
            self._config = None
            sys.stderr.write("Problem with opening configuration file\n")
        finally:
            if file:
                file.close()

    def _default_config(self):
        self._config = configparser.ConfigParser()
        #section program
        self._config["PROGRAM"] = {}
        self._config["PROGRAM"]["nooverwrite"] = "0"
        self._config["PROGRAM"]["convertor"] = "convert" #we use imagemagick
        self._config["PROGRAM"]["noimages"] = "0"
        self._config["PROGRAM"]["latex"] = "pdflatex"
        self._config["PROGRAM"]["language"] = "english"
        self._config["PROGRAM"]["open"] = "0"
        self._config["PROGRAM"]["nocss"] = "0"
        self._config["PROGRAM"]["color"] = "0"
        self._config["PROGRAM"]["verbose"] = "0"
        self._config["PROGRAM"]["ascii"] = "0"
        self._config["PROGRAM"]["form"] = "0"
        self._config["PROGRAM"]["wget"] = "0"
        #section packages
        self._config["PACKAGES"] = {}
        self._config["PACKAGES"]["longtable"] = "0"
        self._config["PACKAGES"]["euro"] = "eurosym"
        self._config["PACKAGES"]["wasysym"] = "1"
        self._config["PACKAGES"]["wrapfig"] = "1"

        #TODO: add more config
    def program_config(self, item):
        """Get program configuration from configfile"""
        return self._config["PROGRAM"].get(item, "0")
    def package_config(self, item):
        """Get package configuration from configfile"""
        return self._config["PACKAGES"].get(item, "0")
