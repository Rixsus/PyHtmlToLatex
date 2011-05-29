

class ConfPackage:
    def __init__(self, package, *options):
        self._pack = package
        self._opt = options
    def has_option(self, option):
        """Get if option is set"""
        return option in self._opt
    def add_option(self, option):
        #called very very rarely
        self._opt = tuple(list(self._opt).append(option))
    def __str__(self):
        opt = ""
        if len(self._opt) > 0:
            opt = "[{0}]".format(",".join(self._opt))
        return "\\usepackage{0}{1}{2}{3}".format(opt, "{", self._pack, "}")
    @property
    def package(self):
        return self._pack
