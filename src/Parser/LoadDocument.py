
import re
import urllib.request
import os
from threading import Thread
from shutil import copyfile


def download_html(source):
    f = urllib.request.urlopen(source)
    return f.read()

def download_css(source):
    #TODO: add threads
    if source[0:5] == "http:":
        f = urllib.request.urlopen(source)
    else:
        f = open(source, "r")
    return f.read()


def copy_file(source, destination, conf):
    """Source file, destination dir, return new filename, copy or convert only images!"""
    if source == destination:
        return source
    elif source[0:5] == "http:":
        filename = source[source.rfind("/"):]
        source = urllib.request.urlretrieve(source)[0]
        file = destination + filename
    else:
        file = destination + source[source.rfind("/"):]
    if conf["nooverwrite"]:
        i = 0
        tmp = file
        while(os.path.isfile(tmp)):
            tmp = file[:file.rfind(".")] + str(i) + file[file.rfind("."):]
            i += 1
        file = tmp

    ext = file[file.rfind(".") + 1:]
    #if image is supported just copy it
    if ext in conf["images"]:
        t = Thread(target = copyfile, args = (source, file))
    else:
        #else convert it via convertor
        #TODO: better support for configparser
        #add extension to file
        file = file[:file.rfind(".")] + "." + conf["images"][0]
        t = Thread(target = os.popen, args = (conf["convertor"] + " " + source + " " + file,))
    t.start()
    return file


def detect_encoding(bytes, encoding = None):
    """
    Try to detect encoding with following precedence:
        1. Given encoding
        2. Meta tag
        3. Try to detect encoding with chardet
    """
    if encoding:
        return encoding
    #TODO: zaistit aby som nemal duplicitu dat
    text = bytes.decode("ascii", "replace")
    #TODO: vylepsit RE
    enc = re.search(r"charset=([^;\"]*)", text, re.M | re.IGNORECASE)

    if enc:
        try:
            import codecs
            codecs.lookup(enc.groups()[0])
            return enc.groups()[0]
        except LookupError:
            pass

    from Parser import chardet
    charenc = chardet.detect(bytes)
    if charenc["encoding"]:
        return charenc["encoding"]
    else:
        return "utf8"

