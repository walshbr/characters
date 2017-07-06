import nltk
import os

#TODO: right now it's getting all texts and even though they're associated with a character there is no easy way get a list of all the texts for that particular character
#TODO: clean the texts
#TODO: do something interesting

class Corpus(object):
    def __init__(self, corpus_dir):
        self.corpus_dir = corpus_dir
        self.manifest = self.get_manifest()
        self.fns = [text[1] for text in self.manifest]
        self.characters = [text[0] for text in self.manifest]
        self.texts = [Text(text[0], text[1]) for text in self.manifest]

    def get_manifest(self):
        texts = []
        for (root, _, files) in os.walk(self.corpus_dir):
            for fn in files:
                if fn[0] == '.':
                    pass
                elif os.path.splitext(fn)[1] == '.jpg':
                    pass
                else:
                    path = os.path.join(root, fn)
                    character = os.path.basename(root)
                    texts.append((character, path))
        return texts


class Text(object):
    def __init__(self, character, fn):
        self.fn = fn
        self.character = character
        self.raw = self.open_text(self.fn)

    def open_text(self, fn):
        with open(fn, 'r')as fin:
            return fin.read()

    def clean_text(text):
        pass


def main():
    corpus_dir = 'text'
    corpus = Corpus(corpus_dir)

    # cleaned_texts =
    # print(texts)


if __name__ == "__main__":
    main()
