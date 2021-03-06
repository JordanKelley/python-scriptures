from __future__ import unicode_literals
from .base import Text


class Deuterocanon(Text):
    """
    Deuterocanonical Books
    """
    books = {
        'tob': ('Tobit', 'Tob', 'Tob(?:it)?',
                [22, 14, 17, 21, 22, 17, 18, 21, 6, 12, 19, 22, 18, 15], "DC"),

        'jdt': ('Judith', 'Jdt', 'Jud(?:ith)?',
                [
                    16, 28, 10, 15, 24, 21, 32, 35, 14,
                    23, 23, 20, 20, 19, 13, 25
                ], "DC"),

        'addesth': ('Additions to Esther', 'AddEsth',
            '(?:AddEsth|(?:Additions to|Rest of) Esther|Esther \\(Greek\\))',
                    [
                        39, 23, 22, 47, 28, 14, 10, 41, 32, 13
                    ], "DC"),

        'wis': ('Wisdom', 'Wis',
                '(?:The )?Wis(?:dom(?: of Solomon)?)?',
                [
                    16, 24, 19, 20, 23, 25, 30, 20, 18,
                    21, 26, 27, 19, 31, 19, 29, 21,
                    25, 22
                ], "DC"),

        'sir': ('Sirach', 'Sir',
            'Sir(?:ach)?|Ecclesiasticus',
                [
                    29, 18, 30, 31, 17, 37, 36, 19, 18,
                    30, 34, 18, 25, 27, 20, 28, 27, 33,
                    26, 30, 28, 27, 27, 31, 25, 20, 30,
                    26, 28, 25, 31, 24, 33, 26, 24, 27,
                    30, 34, 35, 30, 24, 25, 35, 23, 26,
                    20, 25, 25, 16, 29, 30
                ], "DC"),

        'bar': ('Baruch', 'Bar', 'Bar(?:uch)?',
                [
                    21, 35, 37, 37, 9
                ], "DC"),

        'epjer': ('Letter of Jeremiah', 'EpJer',
            'EpJer|Letter of Jeremiah',
                [73], "DC"),

        'prazar': ('Prayer of Azariah', 'prazar',
            '(?:prayer of |Pr)?Azar(?:iah)?|Song of (?:the )?Three Children',
                        [68], "DC"),

        'sus': ('Susanna', 'susanna',
            '(?:Story of )?sus(?:anna)?',
                [64], "DC"),

        'bel': ('Bel and the Dragon', 'bel',
                      'bel(?:(?: and the)? dragon)?',
                      [42], "DC"),

        '1macc': ('I Maccabees', '1Macc', '(?:1|I) ?Macc(?:abees)?',
                  [
                      64, 70, 60, 61, 68, 63, 50, 32, 73,
                      89, 74, 53, 53, 49, 41, 24
                  ], "DC"),

        '2macc': ('II Maccabees', '2Macc', '(?:2|II) ?Macc(?:abees)?',
                  [
                      36, 32, 40, 50, 27, 31, 42, 36, 29,
                      38, 38, 45, 26, 46, 39
                  ], "DC"),
    }
