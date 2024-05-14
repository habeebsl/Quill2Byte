import re
import spacy



class Translator:
    
    early_modern_to_modern = {
    "mine":"my", "thou": "you", "thee": "you", "thy": "your",
    "thine": "yours", "yon":"that", "art": "are", "dost": "do",
    "doth": "does", "wilt": "will", "shalt": "shall", "mayest": "may",
    "mightest": "might", "canst": "can", "must": "must", "wert":"were",
    "o'":"of", "prithee": "please", "anon": "soon", "ere": "before",
    "hither": "here", "thither": "there", "hence": "away", "whence": "from where",
    "withal": "with", "haply": "perhaps", "nay": "no", "zounds": "exclamation",
    "fain": "gladly", "hie": "hurry", "wherefore": "why", "hark": "listen",
    "an't": "and it", "'twas": "it was", "ne'er": "never", "tis": "it is",
    "ye": "you", "oft": "often", "sirrah": "sir", "yea": "yes",
    "forefend": "prevent", "methinks": "I think", "whither": "where",
    "hast": "have", "hath": "has", "e'er":"ever", "o'er":"over"
    }

    def __init__(self, text):
          self.text = text
          self.doc = self.load_spacy_lib(self.text)

    def load_spacy_lib(self, text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        return doc

    def to_current_modern_english(self):
        for key, value in self.early_modern_to_modern.items():
            if key in self.text.lower():
                self.__regex_and_modify_text(key, value)

            new = self.text.split(" ")
            for i in new:
                if i.endswith("eth"):
                    without_eth = i.replace("eth", "s")
                    new_new = " ".join(new)
                    self.text = new_new.replace(i, without_eth)

    def __replace_you_with_equivalent(self):
        if "you" in self.text.lower():
            new_tokens = []
            for token in self.doc:
                if token.text.lower() == "you":
                    replacement = "thou" if token.dep_ == "nsubj" else "thee"
                    new_tokens.append(replacement + token.whitespace_)
                else:
                    new_tokens.append(token.text_with_ws)
            self.text = "".join(new_tokens)

    def __replace_text_with_early_equivalent(self):
        for key, value in self.early_modern_to_modern.items():         
            if value in self.text:
                self.__regex_and_modify_text(value, key)

    def __replace_words_with_eth_equivalent(self):
        for token in self.doc:
            if token.pos_ == "VERB" and token.tag_ == "VBZ":
                eth_verb = token.lemma_ + "eth"
                self.__regex_and_modify_text(token.text, eth_verb)
    
    def __regex_and_modify_text(self, escape_text, sub_text):
        actual_pattern = r"(?<!\w)" + re.escape(escape_text) + r"(?!\w)"
        pattern = re.compile(actual_pattern, re.IGNORECASE)
        self.text = re.sub(pattern, sub_text, self.text)

                
    def to_early_modern_english(self):
        self.__replace_you_with_equivalent()
        self.__replace_text_with_early_equivalent()
        self.__replace_words_with_eth_equivalent()
         