import unicodedata

class Utils:

    @classmethod
    def strip_accents(cls, txt):
        return ''.join(
            c for c in unicodedata.normalize('NFD', txt) if unicodedata.category(c) != 'Mn')
