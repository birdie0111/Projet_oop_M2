import spacy

class Text:
    def __init__(self, content = None, langue = "en", min_len = 1, max_len = 1000):
        self.content = content
        self.langue = langue
        self.min_len = min_len
        self.max_len = max_len
        self.nlp_toks = self.nlp_treatment()

    def nlp_treatment(self):
        if (self.length_verify(self.min_len, self.max_len)):
            if self.langue == "fr":
                nlp = spacy.load("fr_core_news_sm")
            elif self.langue == "en":
                nlp = spacy.load("en_core_web_sm")
            else:
                print("\nERROR: No package for this language\n")
                exit()
            toks = nlp(self.content)
        else:
            print("\nERROR: Length of corpus is not right\n")
            exit()
            
        return toks
    
    def POS_tagging(self):
        pos_dic = {}
        print("\nPOS tagging results:\n")
        for tok in self.nlp_toks:
            print("{} ---> {}\n".format(tok.text, tok.pos_))
            if (tok.text not in pos_dic):
                pos_dic[tok.text] = [tok.pos_]
            else:
                if (pos_dic[tok.text][0] != tok.pos_): # Si il y a different POS pour un meme mot:
                    pos_dic[tok.text].append(tok.pos_)
        return pos_dic


        
    
    def statistics(self):
        stat_dic = {}
        for tok in self.nlp_toks:
            if (tok.text not in stat_dic):
                stat_dic[tok.text] = 1
            else:
                stat_dic[tok.text] += 1
        print(stat_dic)
        return stat_dic
    
        



    def length_verify(self, min, max):
        if (self.content != None):
            return (len(self.content) >= min and len(self.content) <= max)
        else:
            print("ERROR: No input text.\n")
            return False