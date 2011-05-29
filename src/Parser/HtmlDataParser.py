
from html.parser import HTMLParser
from Parser.LoadDocument import detect_encoding, download_html, copy_file, download_css
from Parser.HtmlDocument  import CSSEntity, HTMLDocument, HTMLEntity, HTMLRef
from html.entities import codepoint2name
import os
import sys




class HtmlDataParser(HTMLParser):
    '''
    classdocs
    '''
    def __init__(self, config):
        '''
        Constructor
        '''
        HTMLParser.__init__(self, strict = True) #cakal som na strcit=False preto prave python 3.2, nejde opravit!!!
        #main data
        self._data = HTMLDocument()

        #config
        self._config = config

        #opened tags, begin with openned htmldocument
        self._opened_tags = [self._data]
        #recently closed tag
        self._recently_closed = None
        #invalid tags
        self._invalid_tags = []

        #used for internal CSS
        self._inter_css = False
        self._css = CSSEntity()

        #detect emcoding 
        #TODO: divide class into download and decode
        #internet download source
        if config.internet:
            bytes = download_html(config.source)
            self._enc = detect_encoding(bytes, config.encoding)
        #local source
        else:
            f = open(config.source, "rb")
            bytes = f.read()
            self._enc = detect_encoding(bytes, config.encoding)
            f.close()
        self.feed(bytes.decode(self._enc))
        self.close()


    def handle_starttag(self, tag, attrs):
        if tag == "pre":
            self.nofill = True
        if tag == "style":
            self._inter_css = True
        elif tag == "link":
            #TODO: do something -> download,open,load,parse css
            self._link_tag(attrs)

        elif tag == "img":
            #TODO: download from internet, change address
            if self._handle_img(attrs):
                Ent = HTMLEntity(tag, attrs)
                self._parse_css(Ent)
                self._opened_tags[-1].append(Ent) #add child
        else:
            Ent = HTMLEntity(tag, attrs)
            self._parse_css(Ent)
            for name, value in attrs:
                if name == "style":
                    Ent.add_css(value)


            if self._should_close_tag(tag):
                self._close_tag(tag)
            self._opened_tags[-1].append(Ent) #add child

            if not tag in ("br", "meta", "hr"):
                self._opened_tags.append(Ent) #add open tag


    def _should_close_tag(self, tag):
        """Function determine if we should close tag"""
        if tag in ("tr", "td", "th"):     #tables
            if tag == "tr":
                for i in reversed(self._opened_tags):
                    #TODO: add more tags
                    if str(i) in ("tr",):
                        self._invalid_tags.append(tag)
                        return True
                else:
                    return False
            else: #td or th
                for i in reversed(self._opened_tags):
                    if str(i) in ("td", "tr", "th"):
                        self._invalid_tags.append(tag)
                        return True
                else:
                    return False
        elif tag == "li": #TODO add tags for lists
            for i in reversed(self._opened_tags):
                if str(i) == "li":
                    self._invalid_tags.append(tag)
                    return True
                elif str(i) in ("ul", "ol"):
                    return False
            else:
                return False
        elif tag in ("dt", "dd"):
            for i in reversed(self._opened_tags):
                if str(i) in ("dt", "dd"):
                    self._invalid_tags.append(tag)
                    return True
                elif str(i) == "dl":
                    return False
            else:
                return False
        return False

    def _parse_css(self, html_entity):
        #TODO: works only class id and multiple definition
        #name of taf : th:{...;}

        for key, value in self._css.css.items():
            if key == html_entity.tag:
                html_entity._css.add_css(value)
            if "," in key:      #h1,h2 {...}
                csstag = key.split(",")
                if html_entity.tag in csstag:
                    #h1,h2,h3...
                    html_entity._css.add_css(value)
            if " " in key:      #h1 em {...}
                lasttag = key.split(" ")[-1]
                if html_entity.tag in lasttag:
                    #we have matched tag, now search opened tags for 
                    should_be_in = lasttag = key.split(" ")[0]
                    try:
                        for i in reversed(self._opened_tags):
                            if should_be_in == str(i):
                                #we found tag in desired tag
                                html_entity._css.add_css(value)
                                break
                    except Exception:
                        pass


        if "class" in html_entity.attrs:
            #search in global css
            #TODO: split for more classes
            cl = html_entity.attrs["class"]
            for key, value in self._css.css.items():
                if cl in key:
                    #if we have some common character, we should test it
                    if key[0] == "." and key[1:] == cl:
                        #we have desired class so we just add it
                        html_entity._css.add_css(value)
                    if key[0] != "." and "." in key:
                        tag = key.split(".")[0]
                        #todo: add class
                        if tag == html_entity.tag and cl == key.split(".")[1]:
                            #we have what we wanted
                            html_entity._css.add_css(value)

        if "id" in html_entity.attrs:
            #search in global css
            #TODO: split for more classes
            cl = html_entity.attrs["id"]
            for key, value in self._css.css.items():
                if cl in key:
                    #if we have some common character, we should test it
                    if key[0] == "#" and key[1:] == cl:
                        #we have desired class so we just add it
                        html_entity._css.add_css(value)
                    if key[0] != "#" and "#" in key:
                        tag = key.split("#")[0]
                        #todo: add class
                        if tag == html_entity.tag and cl == key.split("#")[1]:
                            #we have what we wanted
                            html_entity._css.add_css(value)


    def _link_tag(self, attrs):
        dicattr = dict(attrs)
        try:
            if dicattr["type"] == "text/css":
                css = download_css(os.path.join(self._config.source_dir, dicattr["href"]))
                if isinstance(css, str):
                    self._css.add_css(download_css(os.path.join(self._config.source_dir, dicattr["href"])))
                else:
                    self._css.add_css(download_css(os.path.join(self._config.source_dir, dicattr["href"])).decode())
        except KeyError:
            sys.stderr.write("Problem with link tag\n")
        except IOError:
            sys.stderr.write("Problem with opening css file\n")

    def _close_tag(self, tag):
        if self._opened_tags[-1].tag == "body":
            #DONT CLOSE BODY TAG!
            return
        if self._opened_tags[-1].tag == tag:
            self._recently_closed = self._opened_tags.pop()
        #generator object
        elif tag in (str(x) for x in self._opened_tags):
            while True:
                self._recently_closed = self._opened_tags.pop()
                invalid = str(self._recently_closed)
                if invalid == tag:
                    break
            self._invalid_tags.append(invalid)
        elif tag in self._invalid_tags:
            #remove invalid tag
            self._invalid_tags.remove(tag)
        else:
            #Invalid closed tag
            #TODO: do something about it
            #write error
            sys.stderr.write("Malformed HTML tag:{0}, ignoring\n".format(tag))
            pass

    def handle_endtag(self, tag):
        if tag == "pre":
            self.nofill = False
        #style and link tags
        if tag == "style" or tag == "link":
            self._inter_css = False
            return
        #best way to close tag
        self._close_tag(tag)

    def handle_startendtag(self, tag, attrs):
        Ent = None
        if tag == "img":
            if self._handle_img(attrs):
                Ent = HTMLEntity(tag, attrs)
                self._parse_css(Ent)
        elif tag == "link":
            self._link_tag(attrs)
            return
        else:
            Ent = HTMLEntity(tag, attrs)
            for name, value in attrs:
                if name == "style":
                    Ent.add_css(value)
        if Ent:
            self._opened_tags[-1].append(Ent) #add child

    def handle_data(self, data):
        #TODO:Handle charref and entityref
        if self._inter_css:
            self._css.add_css(data)
        else:
            self._opened_tags[-1].append(data)



    """TODO:Handle special data"""
    def handle_charref(self, cp):
        #TODO: Exception handling
        try:

            name = codepoint2name[int(cp)]
            self._opened_tags[-1].append(HTMLRef(name))
        except KeyError:
            #TODO: handle keyerror
            pass
    def handle_entityref(self, name):
        self._opened_tags[-1].append(HTMLRef(name))


    def _handle_img(self, attrs):
        if self._config["noimages"]:
            #we don't want any images so we simply exit this function
            return False
        img = None
        for i in attrs:
            if i[0] == "src":
                img = i
                break
        if not img:
            return False
        elif img[1][0:5] == "http:":
            file = img[1]

        elif self._config.internet:
            if self._config["verbose"]:
                print("Downloading:" + file)
            if img[1][0] == "/":
                file = "http://" + os.path.normpath(os.path.join(self._config.source_dir, img[1][1:]))
            else:
                file = "http://" + os.path.normpath(os.path.join(self._config.source_dir, img[1]))
            if self._config["verbose"]:
                print(file)
        else:
            file = os.path.join(self._config.source_dir, img[1])
        attrs.remove(img)

        #CONFIG
        file = copy_file(file, self._config.destination_dir, self._config)
        if not file:
            #if we could retrive file, we ignore tag
            return False
        attrs.append(("src", file))
        return True

    @property
    def HTMLDocument(self):
        """Return HTMLDocument"""
        #TODO: add css from global style
        return self._data


