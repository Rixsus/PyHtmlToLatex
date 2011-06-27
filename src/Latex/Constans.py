


#copied characters from html.entities, and edited to use with html2latex->latex equivalent,math mode
name2latex = {
    'AElig':    (r"\AE{}", False), # latin capital letter AE = latin capital ligature AE, U+00C6 ISOlat1
    'Aacute':   (r"\'{A}", False), # latin capital letter A with acute, U+00C1 ISOlat1
    'Acirc':    (r"\^{A}", False), # latin capital letter A with circumflex, U+00C2 ISOlat1
    'Agrave':   (r"\`{A}", False), # latin capital letter A with grave = latin capital letter A grave, U+00C0 ISOlat1
    'Alpha':    (r"A", True), # greek capital letter alpha, U+0391
    'Aring':    (r"\r{A}", False), # latin capital letter A with ring above = latin capital letter A ring, U+00C5 ISOlat1
    'Atilde':   (r"\~{A}", False), # latin capital letter A with tilde, U+00C3 ISOlat1
    'Auml':     (r'\"{A}', False), # latin capital letter A with diaeresis, U+00C4 ISOlat1
    'Beta':     (r"B", True), # greek capital letter beta, U+0392
    'Ccedil':   (r"\c{C}", False), # latin capital letter C with cedilla, U+00C7 ISOlat1
    'Chi':      (r"X", True), # greek capital letter chi, U+03A7
    'Dagger':   (r"\ddagger{}", True), # double dagger, U+2021 ISOpub
    'Delta':    (r"\Delta{}", True), # greek capital letter delta, U+0394 ISOgrk3
    'ETH':      (r"\DJ{}", False), # latin capital letter ETH, U+00D0 ISOlat1
    'Eacute':   (r"\'{E}", False), # latin capital letter E with acute, U+00C9 ISOlat1
    'Ecirc':    (r"\^{E}", False), # latin capital letter E with circumflex, U+00CA ISOlat1
    'Egrave':   (r"\`{E}", False), # latin capital letter E with grave, U+00C8 ISOlat1
    'Epsilon':  (r"E", True), # greek capital letter epsilon, U+0395
    'Eta':      (r"H", True), # greek capital letter eta, U+0397
    'Euml':     (r'\"{E}', False), # latin capital letter E with diaeresis, U+00CB ISOlat1
    'Gamma':    (r"\Gamma{}", True), # greek capital letter gamma, U+0393 ISOgrk3
    'Iacute':   (r"\'{I}", False), # latin capital letter I with acute, U+00CD ISOlat1
    'Icirc':    (r"\^{I}", False), # latin capital letter I with circumflex, U+00CE ISOlat1
    'Igrave':   (r"\`{I}", False), # latin capital letter I with grave, U+00CC ISOlat1
    'Iota':     (r"I", True), # greek capital letter iota, U+0399
    'Iuml':     (r'\"{I}', False), # latin capital letter I with diaeresis, U+00CF ISOlat1
    'Kappa':    (r"K", True), # greek capital letter kappa, U+039A
    'Lambda':   (r"\Lambda{}", True), # greek capital letter lambda, U+039B ISOgrk3
    'Mu':       (r"M", True), # greek capital letter mu, U+039C
    'Ntilde':   (r"\~{N}", False), # latin capital letter N with tilde, U+00D1 ISOlat1
    'Nu':       (r"N", True), # greek capital letter nu, U+039D
    'OElig':    (r"\OE{}", False), # latin capital ligature OE, U+0152 ISOlat2
    'Oacute':   (r"\'{O}", False), # latin capital letter O with acute, U+00D3 ISOlat1
    'Ocirc':    (r"\^{O}", False), # latin capital letter O with circumflex, U+00D4 ISOlat1
    'Ograve':   (r"\`{O}", False), # latin capital letter O with grave, U+00D2 ISOlat1
    'Omega':    (r"\Omega{}", True), # greek capital letter omega, U+03A9 ISOgrk3
    'Omicron':  (r"O", True), # greek capital letter omicron, U+039F
    'Oslash':   (r"\O{}", False), # latin capital letter O with stroke = latin capital letter O slash, U+00D8 ISOlat1
    'Otilde':   (r"\~{O}", False), # latin capital letter O with tilde, U+00D5 ISOlat1
    'Ouml':     (r'\"{O}', False), # latin capital letter O with diaeresis, U+00D6 ISOlat1
    'Phi':      (r"\Phi{}", True), # greek capital letter phi, U+03A6 ISOgrk3
    'Pi':       (r"\Pi{}", True), # greek capital letter pi, U+03A0 ISOgrk3
    'Prime':    (r"''", True), # double prime = seconds = inches, U+2033 ISOtech
    'Psi':      (r"\Psi", True), # greek capital letter psi, U+03A8 ISOgrk3
    'Rho':      (r"R", True), # greek capital letter rho, U+03A1
    'Scaron':   (r"\v{S}", False), # latin capital letter S with caron, U+0160 ISOlat2
    'Sigma':    (r"\Sigma{}", True), # greek capital letter sigma, U+03A3 ISOgrk3
    'THORN':    (r"\TH{}", False), # latin capital letter THORN, U+00DE ISOlat1
    'Tau':      (r"T", True), # greek capital letter tau, U+03A4
    'Theta':    (r"\Theta{}", True), # greek capital letter theta, U+0398 ISOgrk3
    'Uacute':   (r"\'{U}", False), # latin capital letter U with acute, U+00DA ISOlat1
    'Ucirc':    (r"\^{U}", False), # latin capital letter U with circumflex, U+00DB ISOlat1
    'Ugrave':   (r"\`{U}", False), # latin capital letter U with grave, U+00D9 ISOlat1
    'Upsilon':  (r"Y", True), # greek capital letter upsilon, U+03A5 ISOgrk3
    'Uuml':     (r'\"{U}', False), # latin capital letter U with diaeresis, U+00DC ISOlat1
    'Xi':       (r"\Xi{}", True), # greek capital letter xi, U+039E ISOgrk3
    'Yacute':   (r"\'{Y}", False), # latin capital letter Y with acute, U+00DD ISOlat1
    'Yuml':     (r'\"{Y}', False), # latin capital letter Y with diaeresis, U+0178 ISOlat2
    'Zeta':     (r"Z", True), # greek capital letter zeta, U+0396
    'aacute':   (r"\'{a}", False), # latin small letter a with acute, U+00E1 ISOlat1
    'acirc':    (r"\^{a}", False), # latin small letter a with circumflex, U+00E2 ISOlat1
    'acute':    (r"'", False), # acute accent = spacing acute, U+00B4 ISOdia
    'aelig':    (r"\ae{}", False), # latin small letter ae = latin small ligature ae, U+00E6 ISOlat1
    'agrave':   (r"\`{a}", False), # latin small letter a with grave = latin small letter a grave, U+00E0 ISOlat1
    'alefsym':  (r"\aleph{}", True), # alef symbol = first transfinite cardinal, U+2135 NEW
    'alpha':    (r"\alpha{}", True), # greek small letter alpha, U+03B1 ISOgrk3
    'amp':      (r"\&", False), # ampersand, U+0026 ISOnum
    'and':      (r"\wedge{}", True), # logical and = wedge, U+2227 ISOtech
    'ang':      (r"\angle{}", True), # angle, U+2220 ISOamso
    'aring':    (r"\r{a}", False), # latin small letter a with ring above = latin small letter a ring, U+00E5 ISOlat1
    'asymp':    (r"\approx{}", True), # almost equal to = asymptotic to, U+2248 ISOamsr
    'atilde':   (r"\~{a}", False), # latin small letter a with tilde, U+00E3 ISOlat1
    'auml':     (r'\"{a}', False), # latin small letter a with diaeresis, U+00E4 ISOlat1
    'bdquo':    (r'\clqq', False), # double low-9 quotation mark, U+201E NEW
    'beta':     (r"\beta{}", True), # greek small letter beta, U+03B2 ISOgrk3
    'brvbar':   (r"\brokenvert{}", False, "wasysym"), # broken bar = broken vertical bar, U+00A6 ISOnum
    'bull':     (r"\bullet{}", True), # bullet = black small circle, U+2022 ISOpub
    'cap':      (r"\cap{}", True), # intersection = cap, U+2229 ISOtech
    'ccedil':   (r"\c{c}", False), # latin small letter c with cedilla, U+00E7 ISOlat1
    'cedil':    (r"\c{}", False), # cedilla = spacing cedilla, U+00B8 ISOdia
    'cent':     (r"\cent{}", False, "wasysym"), # cent sign, U+00A2 ISOnum
    'chi':      (r"\chi{}", True), # greek small letter chi, U+03C7 ISOgrk3
    'circ':     (r"\^{}", False), # modifier letter circumflex accent, U+02C6 ISOpub
    'clubs':    (r"\clubsuit{}", True), # black club suit = shamrock, U+2663 ISOpub
    'cong':     (r"\cong{}", True), # approximately equal to, U+2245 ISOtech
    'copy':     (r"\copyright{}", True), # copyright sign, U+00A9 ISOnum
    'crarr':    (r"\hookleftarrow{}", True), # downwards arrow with corner leftwards = carriage return, U+21B5 NEW
    'cup':      (r"\cup{}", True), # union = cup, U+222A ISOtech
    'curren':   (r"\currency{}", False, "wasysym"), # currency sign, U+00A4 ISOnum
    'dArr':     (r"\Downarrow{}", True), # downwards double arrow, U+21D3 ISOamsa
    'dagger':   (r"\dager{}", True), # dagger, U+2020 ISOpub
    'darr':     (r"\downarrow{}", True), # downwards arrow, U+2193 ISOnum
    'deg':      (r"\,^{\circ}", True), # degree sign, U+00B0 ISOnum
    'delta':    (r"\delta{}", True), # greek small letter delta, U+03B4 ISOgrk3
    'diams':    (r"\Diamondblack{}", True, "txfonts"), # black diamond suit, U+2666 ISOpub
    'divide':   (r"\div{}", True), # division sign, U+00F7 ISOnum
    'eacute':   (r'\'{e}', False), # latin small letter e with acute, U+00E9 ISOlat1
    'ecirc':    (r'\^{e}', False), # latin small letter e with circumflex, U+00EA ISOlat1
    'egrave':   (r'\^{e}', False), # latin small letter e with grave, U+00E8 ISOlat1
    'empty':    (r"\emptyset", True), # empty set = null set = diameter, U+2205 ISOamso
    'emsp':     (r"\hspace{1em}", False), # em space, U+2003 ISOpub
    'ensp':     (r"\hspace{.5em}", False), # en space, U+2002 ISOpub
    'epsilon':  (r"\epsilon{}", True), # greek small letter epsilon, U+03B5 ISOgrk3
    'equiv':    (r"\equiv{}", True), # identical to, U+2261 ISOtech
    'eta':      (r"\eta{}", True), # greek small letter eta, U+03B7 ISOgrk3
    'eth':      (r"\eth{}", True, "amssymb"), # latin small letter eth, U+00F0 ISOlat1
    'euml':     (r'\"{e}', False), # latin small letter e with diaeresis, U+00EB ISOlat1
    'euro':     (r"\euro{}", False, "eurosym"), # euro sign, U+20AC NEW
    'exist':    (r"\exists{}", True), # there exists, U+2203 ISOtech
    'fnof':     (r"\textflorin{}", False, "textcomp"), # latin small f with hook = function = florin, U+0192 ISOtech
    'forall':   (r"\forall{}", True), # for all, U+2200 ISOtech
    'frac12':   (r"\frac{1}{2}", True), # vulgar fraction one half = fraction one half, U+00BD ISOnum
    'frac14':   (r"\frac{1}{4}", True), # vulgar fraction one quarter = fraction one quarter, U+00BC ISOnum
    'frac34':   (r"\frac{3}{4}", True), # vulgar fraction three quarters = fraction three quarters, U+00BE ISOnum
    'frasl':    (r"\slash{}", True), # fraction slash, U+2044 NEW
    'gamma':    (r"\gamma{}", True), # greek small letter gamma, U+03B3 ISOgrk3
    'ge':       (r"\geq", True), # greater-than or equal to, U+2265 ISOtech
    'gt':       (r">", True), # greater-than sign, U+003E ISOnum
    'hArr':     (r"\Leftrightarrow{}", True), # left right double arrow, U+21D4 ISOamsa
    'harr':     (r"\leftrightarrow{}", True), # left right arrow, U+2194 ISOamsa
    'hearts':   (r"\varheartsuit{}", True, "txfonts"), # black heart suit = valentine, U+2665 ISOpub
    'hellip':   (r"\ldots", False), # horizontal ellipsis = three dot leader, U+2026 ISOpub
    'iacute':   (r'\'{i}', False), # latin small letter i with acute, U+00ED ISOlat1
    'icirc':    (r'\^{i}', False), # latin small letter i with circumflex, U+00EE ISOlat1
    'iexcl':    (r"\textexclamdown{}", False), # inverted exclamation mark, U+00A1 ISOnum
    'igrave':   (r'\`{i}', False), # latin small letter i with grave, U+00EC ISOlat1
    'image':    (r"\Im{}", True), # blackletter capital I = imaginary part, U+2111 ISOamso
    'infin':    (r"\infty{}", True), # infinity, U+221E ISOtech
    'int':      (r"\int{}", True), # integral, U+222B ISOtech
    'iota':     (r"\iota{}", True), # greek small letter iota, U+03B9 ISOgrk3
    'iquest':   (r"?`", False), # inverted question mark = turned question mark, U+00BF ISOnum
    'isin':     (r"\in{}", True), # element of, U+2208 ISOtech
    'iuml':     (r'\"{i}', False), # latin small letter i with diaeresis, U+00EF ISOlat1
    'kappa':    (r"\kappa{}", True), # greek small letter kappa, U+03BA ISOgrk3
    'lArr':     (r"\Leftarrow{}", True), # leftwards double arrow, U+21D0 ISOtech
    'lambda':   (r"\lambda{}", True), # greek small letter lambda, U+03BB ISOgrk3
    'lang':     (r"\langle{}", True), # left-pointing angle bracket = bra, U+2329 ISOtech
    'laquo':    (r"\guillemotleft", False), # left-pointing double angle quotation mark = left pointing guillemet, U+00AB ISOnum
    'larr':     (r"\leftarrow{}", True), # leftwards arrow, U+2190 ISOnum
    'lceil':    (r"\lceil{}", True), # left ceiling = apl upstile, U+2308 ISOamsc
    'ldquo':    (r"``", False), # left double quotation mark, U+201C ISOnum
    'le':       (r"\leq{}", True), # less-than or equal to, U+2264 ISOtech
    'lfloor':   (r"\lfloor{}", True), # left floor = apl downstile, U+230A ISOamsc
    'lowast':   (r"\ast{}", True), # asterisk operator, U+2217 ISOtech
    'loz':      (r"\lozenge{}", True), # lozenge, U+25CA ISOpub
    'lrm':      (r"", False), # left-to-right mark, U+200E NEW RFC 2070
    'lsaquo':   (r"\guilsinglleft", False), # single left-pointing angle quotation mark, U+2039 ISO proposed
    'lsquo':    (r"`", False), # left single quotation mark, U+2018 ISOnum
    'lt':       (r"<", True), # less-than sign, U+003C ISOnum
    'macr':     (r"\bar{ }", True), # macron = spacing macron = overline = APL overbar, U+00AF ISOdia
    'mdash':    (r"---", False), # em dash, U+2014 ISOpub
    'micro':    (r"\mu{}", True), # micro sign, U+00B5 ISOnum
    'middot':   (r"\cdot{}", True), # middle dot = Georgian comma = Greek middle dot, U+00B7 ISOnum
    'minus':    (r"-", True), # minus sign, U+2212 ISOtech
    'mu':       (r"\mu{}", True), # greek small letter mu, U+03BC ISOgrk3
    'nabla':    (r"\nabla{}", True), # nabla = backward difference, U+2207 ISOtech
    'nbsp':     (r"~", False), # no-break space = non-breaking space, U+00A0 ISOnum
    'ndash':    (r"--", False), # en dash, U+2013 ISOpub
    'ne':       (r"\neq{}", True), # not equal to, U+2260 ISOtech
    'ni':       (r"\ni{}", True), # contains as member, U+220B ISOtech
    'not':      (r"\neg{}", True), # not sign, U+00AC ISOnum
    'notin':    (r"\notin{}", True), # not an element of, U+2209 ISOtech
    'nsub':     (r"\nsubset{}", True), # not a subset of, U+2284 ISOamsn
    'ntilde':   (r'\~{n}', False), # latin small letter n with tilde, U+00F1 ISOlat1
    'nu':       (r"\nu{}", True), # greek small letter nu, U+03BD ISOgrk3
    'oacute':   (r'\'{o}', False), # latin small letter o with acute, U+00F3 ISOlat1
    'ocirc':    (r'\^{o}', False), # latin small letter o with circumflex, U+00F4 ISOlat1
    'oelig':    (r'\oe{}', False), # latin small ligature oe, U+0153 ISOlat2
    'ograve':   (r'\`{o}', False), # latin small letter o with grave, U+00F2 ISOlat1
    'oline':    (r"^-", True), # overline = spacing overscore, U+203E NEW
    'omega':    (r"\omega{}", True), # greek small letter omega, U+03C9 ISOgrk3
    'omicron':  (r"o", True), # greek small letter omicron, U+03BF NEW
    'oplus':    (r"\oplus{}", True), # circled plus = direct sum, U+2295 ISOamsb
    'or':       (r"\vee{}", True), # logical or = vee, U+2228 ISOtech
    'ordf':     (r"\textordfeminine{}", False), # feminine ordinal indicator, U+00AA ISOnum
    'ordm':     (r"\textordmasculine{}", False), # masculine ordinal indicator, U+00BA ISOnum
    'oslash':   (r"\o{}", False), # latin small letter o with stroke, = latin small letter o slash, U+00F8 ISOlat1
    'otilde':   (r"\~{o}", False), # latin small letter o with tilde, U+00F5 ISOlat1
    'otimes':   (r"\otimes{}", True), # circled times = vector product, U+2297 ISOamsb
    'ouml':     (r'\"{o}', False), # latin small letter o with diaeresis, U+00F6 ISOlat1
    'para':     (r"\P{}", False), # pilcrow sign = paragraph sign, U+00B6 ISOnum
    'part':     (r"\partial{}", True), # partial differential, U+2202 ISOtech
    'permil':   (r"\permil{}", False, "wasysym"), # per mille sign, U+2030 ISOtech
    'perp':     (r"\perp{}", True), # up tack = orthogonal to = perpendicular, U+22A5 ISOtech
    'phi':      (r"\phi{}", True), # greek small letter phi, U+03C6 ISOgrk3
    'pi':       (r"\pi{}", True), # greek small letter pi, U+03C0 ISOgrk3
    'piv':      (r"\varpi{}", True), # greek pi symbol, U+03D6 ISOgrk3
    'plusmn':   (r"\pm{}", True), # plus-minus sign = plus-or-minus sign, U+00B1 ISOnum
    'pound':    (r"\pounds{}", False), # pound sign, U+00A3 ISOnum
    'prime':    (r"\prime{}", True), # prime = minutes = feet, U+2032 ISOtech
    'prod':     (r"\prod{}", True), # n-ary product = product sign, U+220F ISOamsb
    'prop':     (r"\propto{}", True), # proportional to, U+221D ISOtech
    'psi':      (r"\psi{}", True), # greek small letter psi, U+03C8 ISOgrk3
    'quot':     (r"''", False), # quotation mark = APL quote, U+0022 ISOnum
    'rArr':     (r"\Rightarrow{}", True), # rightwards double arrow, U+21D2 ISOtech
    'radic':    (r"\surd{}", True), # square root = radical sign, U+221A ISOtech
    'rang':     (r"\rangle{}", True), # right-pointing angle bracket = ket, U+232A ISOtech
    'raquo':    (r"\guillemotright{}", False), # right-pointing double angle quotation mark = right pointing guillemet, U+00BB ISOnum
    'rarr':     (r"\rightarrow{}", True), # rightwards arrow, U+2192 ISOnum
    'rceil':    (r"\rceil{}", True), # right ceiling, U+2309 ISOamsc
    'rdquo':    (r"''", False), # right double quotation mark, U+201D ISOnum
    'real':     (r"\Re{}", True), # blackletter capital R = real part symbol, U+211C ISOamso
    'reg':      (r"\textregistered", False), # registered sign = registered trade mark sign, U+00AE ISOnum
    'rfloor':   (r"\rfloor", True), # right floor, U+230B ISOamsc
    'rho':      (r"\rho{}", True), # greek small letter rho, U+03C1 ISOgrk3
    'rlm':      (r"", False), # right-to-left mark, U+200F NEW RFC 2070
    'rsaquo':   (r"\guilsinglright", False), # single right-pointing angle quotation mark, U+203A ISO proposed
    'rsquo':    (r"'", False), # right single quotation mark, U+2019 ISOnum
    'sbquo':    (r"'", False), # single low-9 quotation mark, U+201A NEW
    'scaron':   (r"\v{s}", False), # latin small letter s with caron, U+0161 ISOlat2
    'sdot':     (r"\cdot", True), # dot operator, U+22C5 ISOamsb
    'sect':     (r"\S", False), # section sign, U+00A7 ISOnum
    'shy':      (r"\-", False), # soft hyphen = discretionary hyphen, U+00AD ISOnum
    'sigma':    (r"\sigma{}", True), # greek small letter sigma, U+03C3 ISOgrk3
    'sigmaf':   (r"\varsigma{}", True), # greek small letter final sigma, U+03C2 ISOgrk3
    'sim':      (r"\sim", True), # tilde operator = varies with = similar to, U+223C ISOtech
    'spades':   (r"\spadesuit{}", True), # black spade suit, U+2660 ISOpub
    'sub':      (r"\subset{}", True), # subset of, U+2282 ISOtech
    'sube':     (r"\subseteq{}", True), # subset of or equal to, U+2286 ISOtech
    'sum':      (r"\sum{}", True), # n-ary sumation, U+2211 ISOamsb
    'sup':      (r"\supset{}", True), # superset of, U+2283 ISOtech
    'sup1':     (r"^{1}", True), # superscript one = superscript digit one, U+00B9 ISOnum
    'sup2':     (r"^{2}", True), # superscript two = superscript digit two = squared, U+00B2 ISOnum
    'sup3':     (r"^{3}", True), # superscript three = superscript digit three = cubed, U+00B3 ISOnum
    'supe':     (r"\supseteq{}", True), # superset of or equal to, U+2287 ISOtech
    'szlig':    (r"\ss{}", False), # latin small letter sharp s = ess-zed, U+00DF ISOlat1
    'tau':      (r"\tau{}", True), # greek small letter tau, U+03C4 ISOgrk3
    'there4':   (r"\therefore{}", True, "amssymb"), # therefore, U+2234 ISOtech
    'theta':    (r"\theta{}", True), # greek small letter theta, U+03B8 ISOgrk3
    'thetasym': (r"\vartheta{}", True), # greek small letter theta symbol, U+03D1 NEW
    'thinsp':   (r" ", False), # thin space, U+2009 ISOpub
    'thorn':    (r"\th{}", False), # latin small letter thorn with, U+00FE ISOlat1
    'tilde':    (r"\textasciitilde{}", False), # small tilde, U+02DC ISOdia
    'times':    (r"\times{}", True), # multiplication sign, U+00D7 ISOnum
    'trade':    (r"\texttrademark{}", False), # trade mark sign, U+2122 ISOnum
    'uArr':     (r"\Uparrow{}", True), # upwards double arrow, U+21D1 ISOamsa
    'uacute':   (r'\'{u}', False), # latin small letter u with acute, U+00FA ISOlat1
    'uarr':     (r"\uparrow{}", True), # upwards arrow, U+2191 ISOnum
    'ucirc':    (r'\^{u}', False), # latin small letter u with circumflex, U+00FB ISOlat1
    'ugrave':   (r'\`{u}', False), # latin small letter u with grave, U+00F9 ISOlat1
    'uml':      (r'\"{}', False), # diaeresis = spacing diaeresis, U+00A8 ISOdia
    'upsih':    (r"\Upsilon{}", True), # greek upsilon with hook symbol, U+03D2 NEW
    'upsilon':  (r"\upsilon{}", True), # greek small letter upsilon, U+03C5 ISOgrk3
    'uuml':     (r'\"{u}', False), # latin small letter u with diaeresis, U+00FC ISOlat1
    'weierp':   (r"\wp{}", True), # script capital P = power set = Weierstrass p, U+2118 ISOamso
    'xi':       (r"\xi{}", True), # greek small letter xi, U+03BE ISOgrk3
    'yacute':   (r"\'{y}", False), # latin small letter y with acute, U+00FD ISOlat1
    'yen':      (r"\textyen{}", False, "textcomp"), # yen sign = yuan sign, U+00A5 ISOnum
    'yuml':     (r'\"{y}', False), # latin small letter y with diaeresis, U+00FF ISOlat1
    'zeta':     (r"\zeta{}", True), # greek small letter zeta, U+03B6 ISOgrk3
    'zwj':      (r"", False), # zero width joiner, U+200D NEW RFC 2070
    'zwnj':     (r"", False), # zero width non-joiner, U+200C NEW RFC 2070
}
#used only for unicode character not found in name2latex
code2latex = {
    133:(r"\ldots", False), # horizontal ellipsis 
    149:(r"\bullet{}", True), # bullet 
    153:(r"\texttrademark{}", False), # trade mark sign
    225:(r"\'{a}", False), #á
    228:(r'\"{a}', False), #ä
    269:(r"\v{c}", False), #č
    271:(r"\v{d}", False), #ď
    233:(r"\'{e}", False), #é
    237:(r"\'{i}", False), #í
    314:(r"\'{l}", False), #ĺ
    318:(r"\v{l}", False), #ĺ
    243:(r"\'{o}", False), #ó
    244:(r"\^{o}", False), #ô
    341:(r"\'{r}", False), #ŕ
    353:(r"\v{s}", False), #š
    357:(r"\v{t}", False), #ť
    250:(r"\'{u}", False), #ú
    253:(r"\'{y}", False), #ý
    382:(r"\v{z}", False), #ž
    193:(r"\'{A}", False), #Á
    268:(r"\v{C}", False), #Č
    270:(r"\v{D}", False), #Ď
    201:(r"\'{E}", False), #É
    205:(r"\'{I}", False), #Í
    313:(r"\'{L}", False), #Ĺ
    317:(r"\v{L}", False), #Ľ
    211:(r"\'{O}", False), #Ó
    340:(r"\'{R}", False), #Ŕ
    352:(r"\v{S}", False), #Š
    356:(r"\v{T}", False), #Ť
    218:(r"\'{U}", False), #Ú
    221:(r"\'{Y}", False), #Ý
    381:(r"\v{Z}", False)  #Ž
            }


color_name = ('black', 'navy', 'darkblue', 'mediumblue', 'blue', 'darkgreen', 'green', 'teal', 'darkcyan', 'deepskyblue', 'darkturquoise', 'mediumspringgreen', 'lime', 'springgreen', 'aqua', 'cyan', 'midnightblue', 'dodgerblue', 'lightseagreen', 'forestgreen', 'seagreen', 'darkslategray', 'limegreen', 'mediumseagreen', 'turquoise', 'royalblue', 'steelblue', 'darkslateblue', 'mediumturquoise', 'indigo', 'darkolivegreen', 'cadetblue', 'cornflowerblue', 'mediumaquamarine', 'dimgray', 'slateblue', 'olivedrab', 'slategray', 'lightslategray', 'mediumslateblue', 'lawngreen', 'chartreuse', 'aquamarine', 'maroon', 'purple', 'olive', 'gray', 'skyblue', 'lightskyblue', 'blueviolet', 'darkred', 'darkmagenta', 'saddlebrown', 'darkseagreen', 'lightgreen', 'mediumpurple', 'darkviolet', 'palegreen', 'darkorchid', 'yellowgreen', 'sienna', 'brown', 'darkgray', 'lightblue', 'greenyellow', 'paleturquoise', 'lightsteelblue', 'powderblue', 'firebrick', 'darkgoldenrod', 'mediumorchid', 'rosybrown', 'darkkhaki', 'silver', 'mediumvioletred', 'indianred', 'peru', 'chocolate', 'tan', 'lightgrey', 'palevioletred', 'thistle', 'orchid', 'goldenrod', 'crimson', 'gainsboro', 'plum', 'burlywood', 'lightcyan', 'lavender', 'darksalmon', 'violet', 'palegoldenrod', 'lightcoral', 'khaki', 'aliceblue', 'honeydew', 'azure', 'sandybrown', 'wheat', 'beige', 'whitesmoke', 'mintcream', 'ghostwhite', 'salmon', 'antiquewhite', 'linen', 'lightgoldenrodyellow', 'oldlace', 'red', 'fuchsia', 'magenta', 'deeppink', 'orangered', 'tomato', 'hotpink', 'coral', 'darkorange', 'lightsalmon', 'orange', 'lightpink', 'pink', 'gold', 'peachpuff', 'navajowhite', 'moccasin', 'bisque', 'mistyrose', 'blanchedalmond', 'papayawhip', 'lavenderblush', 'seashell', 'cornsilk', 'lemonchiffon', 'floralwhite', 'snow', 'yellow', 'lightyellow', 'ivory', 'white')
color_code = ("#000000", "#000080", "#00008B", "#0000CD", "#0000FF", "#006400", "#008000", "#008080", "#008B8B", "#00BFFF", "#00CED1", "#00FA9A", "#00FF00", "#00FF7F", "#00FFFF", "#00FFFF", "#191970", "#1E90FF", "#20B2AA", "#228B22", "#2E8B57", "#2F4F4F", "#32CD32", "#3CB371", "#40E0D0", "#4169E1", "#4682B4", "#483D8B", "#48D1CC", "#4B0082", "#556B2F", "#5F9EA0", "#6495ED", "#66CDAA", "#696969", "#6A5ACD", "#6B8E23", "#708090", "#778899", "#7B68EE", "#7CFC00", "#7FFF00", "#7FFFD4", "#800000", "#800080", "#808000", "#808080", "#87CEEB", "#87CEFA", "#8A2BE2", "#8B0000", "#8B008B", "#8B4513", "#8FBC8F", "#90EE90", "#9370D8", "#9400D3", "#98FB98", "#9932CC", "#9ACD32", "#A0522D", "#A52A2A", "#A9A9A9", "#ADD8E6", "#ADFF2F", "#AFEEEE", "#B0C4DE", "#B0E0E6", "#B22222", "#B8860B", "#BA55D3", "#BC8F8F", "#BDB76B", "#C0C0C0", "#C71585", "#CD5C5C", "#CD853F", "#D2691E", "#D2B48C", "#D3D3D3", "#D87093", "#D8BFD8", "#DA70D6", "#DAA520", "#DC143C", "#DCDCDC", "#DDA0DD", "#DEB887", "#E0FFFF", "#E6E6FA", "#E9967A", "#EE82EE", "#EEE8AA", "#F08080", "#F0E68C", "#F0F8FF", "#F0FFF0", "#F0FFFF", "#F4A460", "#F5DEB3", "#F5F5DC", "#F5F5F5", "#F5FFFA", "#F8F8FF", "#FA8072", "#FAEBD7", "#FAF0E6", "#FAFAD2", "#FDF5E6", "#FF0000", "#FF00FF", "#FF00FF", "#FF1493", "#FF4500", "#FF6347", "#FF69B4", "#FF7F50", "#FF8C00", "#FFA07A", "#FFA500", "#FFB6C1", "#FFC0CB", "#FFD700", "#FFDAB9", "#FFDEAD", "#FFE4B5", "#FFE4C4", "#FFE4E1", "#FFEBCD", "#FFEFD5", "#FFF0F5", "#FFF5EE", "#FFF8DC", "#FFFACD", "#FFFAF0", "#FFFAFA", "#FFFF00", "#FFFFE0", "#FFFFF0", "#FFFFFF")
color2code = {color_name[i]:color_code[i] for i in range(len(color_name) - 1)}
code2color = {color_code[i]:color_name[i] for i in range(len(color_name) - 1)}

#supported languages by babel
babel_lang = ('afrikaans', 'bahasa', 'basque', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech', 'danish', 'dutch', 'english', 'USenglish', 'american', 'UKenglish', 'british', 'canadian', 'australian', 'newzealand', 'esperanto', 'estonian', 'finnish', 'french', 'francais', 'canadien', 'acadian', 'galician', 'austrian', 'german', 'germanb', 'greek', 'polutonikogreek', 'hebrew', 'magyar', 'hungarian', 'icelandic', 'interlingua', 'irish', 'italian', 'latin', 'lowersorbian', 'samin', 'norsk', 'nynorsk', 'polish', 'portuges', 'portuguese', 'brazilian', 'brazil', 'romanian', 'russian', 'scottish', 'spanish', 'slovak', 'slovene', 'swedish', 'serbian', 'turkish', 'ukrainian', 'uppersorbian', 'welsh')
