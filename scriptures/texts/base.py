from __future__ import unicode_literals
import re


class InvalidReferenceException(Exception):
    """
    Invalid Reference Exception
    """
    pass


class Text:
    def __init__(self):
        # Check for books
        if hasattr(self, 'books'):
            # make sure it is a dictionary
            if not isinstance(self.books, dict):
                raise Exception(
                    '"books" should be a dictionary, who\'s values are four valued tuples (Book Name, Abbreviation, Regex, [ch1_verse_count, ch2_verse_count, ...])')

            # set the regex instance variables
            self.book_re_string = '|'.join(b[2] for b in self.books.values())
            self.book_re = re.compile(self.book_re_string, re.IGNORECASE | re.UNICODE)

            # set instance compiled scripture reference regex
            self.scripture_re = re.compile(
                r'\b(?P<BookTitle>%s)\s*' \
                '(?P<ChapterNumber>\d{1,3})' \
                '(?:\s*:\s*(?P<VerseNumber>\d{1,3}))?' \
                '(?:\s*[a-zA-Z]\s*)?' \
                '(?:\s*[-\u2013\u2014]\s*' \
                '(?P<EndChapterNumber>\d{1,3}(?=\s*:\s*))?' \
                '(?:\s*:\s*)?' \
                '(?P<EndVerseNumber>\d{1,3}|end)?' \
                ')?'

                '(?:\s*[,;]\s*)?' \
                '(?P<ChapterNumber2>\d{1,3}(?=\s*:\s*))?' \
                '(?:\s*:*\s*(?P<VerseNumber2>\d{1,3}))?' \
                '(?:\s*[a-zA-Z]\s*)?' \
                '(?:\s*[-\u2013\u2014]\s*' \
                '(?P<EndChapterNumber2>\d{1,3}(?=\s*:\s*))?' \
                '(?:\s*:\s*)?' \
                '(?P<EndVerseNumber2>\d{1,3}|end)?' \
                ')?'

                '(?:\s*[,;]\s*)?' \
                '(?P<ChapterNumber3>\d{1,3}(?=\s*:\s*))?' \
                '(?:\s*:*\s*(?P<VerseNumber3>\d{1,3}))?' \
                '(?:\s*[a-zA-Z]\s*)?' \
                '(?:\s*[-\u2013\u2014]\s*' \
                '(?P<EndChapterNumber3>\d{1,3}(?=\s*:\s*))?' \
                '(?:\s*:\s*)?' \
                '(?P<EndVerseNumber3>\d{1,3}|end)?' \
                ')?'

                '(?:\s*[,;]\s*)?' \
                '(?P<ChapterNumber4>\d{1,3}(?=\s*:\s*))?' \
                '(?:\s*:*\s*(?P<VerseNumber4>\d{1,3}))?' \
                '(?:\s*[a-zA-Z]\s*)?' \
                '(?:\s*[-\u2013\u2014]\s*' \
                '(?P<EndChapterNumber4>\d{1,3}(?=\s*:\s*))?' \
                '(?:\s*:\s*)?' \
                '(?P<EndVerseNumber4>\d{1,3}|end)?' \
                ')?'

                '(?:\s*[,;]\s*)?' \
                '(?P<ChapterNumber5>\d{1,3}(?=\s*:\s*))?' \
                '(?:\s*:*\s*(?P<VerseNumber5>\d{1,3}))?' \
                '(?:\s*[a-zA-Z]\s*)?' \
                '(?:\s*[-\u2013\u2014]\s*' \
                '(?P<EndChapterNumber5>\d{1,3}(?=\s*:\s*))?' \
                '(?:\s*:\s*)?' \
                '(?P<EndVerseNumber5>\d{1,3}|end)?' \
                ')?'

                '(?:\s*[,;]\s*)?' \
                '(?P<ChapterNumber6>\d{1,3}(?=\s*:\s*))?' \
                '(?:\s*:*\s*(?P<VerseNumber6>\d{1,3}))?' \
                '(?:\s*[a-zA-Z]\s*)?' \
                '(?:\s*[-\u2013\u2014]\s*' \
                '(?P<EndChapterNumber6>\d{1,3}(?=\s*:\s*))?' \
                '(?:\s*:\s*)?' \
                '(?P<EndVerseNumber6>\d{1,3}|end)?' \
                ')?'
                % (self.book_re_string,), re.IGNORECASE | re.UNICODE)

        else:
            raise Exception('Text has no "books"')

    def get_book(self, name):
        """
        Get a book from its name or None if not found
        """
        for book in self.books.values():
            if re.match('^%s$' % book[2], name, re.IGNORECASE):
                return book

        return None

    def get_end_verse(self, book, chapter):
        return book[3][chapter-1]


    def extract(self, text):
        """
        Extract a list of tupled scripture references from a block of text
        """
        references = []
        for r in re.finditer(self.scripture_re, text):
            groups = r.groups()
            sets = []
            sets.append((groups[0], groups[1], groups[2], groups[3], groups[4]))
            if groups[5] or groups[6] or groups[7] or groups[8]:
                sets.append((groups[0], groups[5] if groups[5] else groups[1], groups[6], groups[7], groups[8]))
            if groups[9] or groups[10] or groups[11] or groups[12]:
                sets.append((groups[0], groups[9] if groups[9] else groups[1], groups[10], groups[11], groups[12]))
            if groups[13] or groups[14] or groups[15] or groups[16]:
                sets.append((groups[0], groups[13] if groups[13] else groups[1], groups[14], groups[15], groups[16]))
            if groups[17] or groups[18] or groups[19] or groups[20]:
                sets.append((groups[0], groups[17] if groups[17] else groups[1], groups[18], groups[19], groups[20]))
            if groups[21] or groups[22] or groups[23] or groups[24]:
                sets.append((groups[0], groups[21] if groups[21] else groups[1], groups[22], groups[23], groups[24]))
            for set in sets:
                try:
                    references.append(self.normalize_reference(*set))
                except InvalidReferenceException:
                    pass
        return references

    def is_valid_reference(self, bookname, chapter, verse=None,
                           end_chapter=None, end_verse=None):
        """
        Check to see if a scripture reference is valid
        """
        try:
            return self.normalize_reference(bookname, chapter, verse,
                                            end_chapter, end_verse) is not None
        except InvalidReferenceException:
            return False

    def reference_to_string(self, bookname, chapter, verse=None,
                            end_chapter=None, end_verse=None):
        """
        Get a display friendly string from a scripture reference
        """
        book = None

        bn, c, v, ec, ev = self.normalize_reference(bookname, chapter, verse,
                                                    end_chapter, end_verse)

        book = self.get_book(bn)

        if c == ec and len(book[3]) == 1:  # single chapter book
            if v == ev:  # single verse
                return '{0} {1}'.format(bn, v)
            else:  # multiple verses
                return '{0} {1}-{2}'.format(bn, v, ev)
        else:  # multichapter book
            if c == ec:  # same start and end chapters
                if v == 1 and ev == book[3][c - 1]:  # full chapter
                    return '{0} {1}'.format(bn, c)
                elif v == ev:  # single verse
                    return '{0} {1}:{2}'.format(bn, c, v)
                else:  # multiple verses
                    return '{0} {1}:{2}-{3}'.format(
                        bn, c, v, ev)
            else:  # multiple chapters
                if v == 1 and ev == book[3][ec - 1]:  # multichapter ref
                    return '{0} {1}-{2}'.format(bn, c, ec)
                else:  # multi-chapter, multi-verse ref
                    return '{0} {1}:{2}-{3}:{4}'.format(bn, c, v, ec, ev)

    def normalize_reference(self, bookname, chapter, verse=None,
                            end_chapter=None, end_verse=None):
        """
        Get a complete five value tuple scripture reference with full book name
        from partial data
        """
        book = self.get_book(bookname)

        # SPECIAL CASES FOR: BOOKS WITH ONE CHAPTER AND MULTI-CHAPTER REFERENCES

        # If the ref is in format: (Book, #, None, None, ?)
        # This is a special case and indicates a reference in the format: Book 2-3
        if chapter is not None and verse is None and end_chapter is None:
            # If there is only one chapter in this book, set the chapter to one and
            # treat the incoming chapter argument as though it were the verse.
            # This normalizes references such as:
            # Jude 2 and Jude 2-4
            if len(book[3]) == 1:
                verse = chapter
                chapter = 1
            # If the ref is in format: (Book, ?, None, None, #)
            # This normalizes references such as: Revelation 2-3
            elif end_verse:
                verse = 1
                end_chapter = end_verse
                end_verse = None
        # If the ref is in the format (Book, #, None, #, #)
        # this is a special case that indicates a reference in the format Book 3-4:5
        elif chapter is not None and verse is None and end_chapter is not None:
            # The solution is to set the verse to one, which is what is
            # most likely intended
            verse = 1

        # Convert to integers or leave as None
        chapter = int(chapter) if chapter else None
        verse = int(verse) if verse else None
        end_chapter = int(end_chapter) if end_chapter else chapter
        if end_verse == 'end':
            end_verse = self.get_end_verse(book, end_chapter if end_chapter else chapter)
        end_verse = int(end_verse) if end_verse else None
        if not book \
                or (chapter is None or chapter < 1 or chapter > len(book[3])) \
                or (verse is not None and (verse < 1 or verse > book[3][chapter - 1])) \
                or (end_chapter is not None and (
                end_chapter < 1
                or end_chapter < chapter
                or end_chapter > len(book[3]))) \
                or (end_verse is not None and (
                end_verse < 1
                or (end_chapter and end_verse > book[3][end_chapter - 1])
                or (chapter == end_chapter and end_verse < verse))):
            raise InvalidReferenceException()

        if not verse:
            return (book[0], chapter, 1, chapter, book[3][chapter - 1])
        if not end_verse:
            if end_chapter and end_chapter != chapter:
                end_verse = book[3][end_chapter - 1]
            else:
                end_verse = verse
        if not end_chapter:
            end_chapter = chapter
        return (book[0], chapter, verse, end_chapter, end_verse)


