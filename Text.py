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
    
    def POS_tagging(self, terminal_output):
        pos_dic = {}
        print("\nPOS tagging results:\n")
        for tok in self.nlp_toks:
            if (terminal_output):
                print("{} ---> {}\n".format(tok.text, tok.pos_))
            if (tok.text not in pos_dic):
                pos_dic[tok.text] = [tok.pos_]
            else:
                if (pos_dic[tok.text][0] != tok.pos_): # Si il y a different POS pour un meme mot:
                    pos_dic[tok.text].append(tok.pos_)
        return pos_dic
    
    def statistics(self, terminal_output):
        stat_dic = {}
        for tok in self.nlp_toks:
            if (tok.text not in stat_dic):
                stat_dic[tok.text] = 1
            else:
                stat_dic[tok.text] += 1
        if (terminal_output):
            print(stat_dic)
        return stat_dic
    
    def lemma(self, terminal_output):
        lemma_dic = {}
        print("\nLemma:\n")
        for tok in self.nlp_toks:
            lemma_dic[tok.text] = tok.lemma_
            if (terminal_output):
                print("{} ---> {}\n".format(tok.text, tok.lemma_))
        return lemma_dic
        
    def research(self, tok_cherche):
        appear_times = 0
        for tok in self.nlp_toks:
            if (tok.text == tok_cherche or tok.lemma_ == tok_cherche):
                appear_times += 1
        return appear_times

    def length_verify(self, min, max):
        if (self.content != None):
            return (len(self.content) >= min and len(self.content) <= max)
        else:
            print("ERROR: No input text.\n")
            return False
    
    def to_csv(self, analyse_type, dict, path):
        if (analyse_type == "pos"):
            header = ["token", "POS"]
        elif (analyse_type == "statistics"):
            header = ["token", "Frequence"]
        elif (analyse_type == "lemma"):
            header = ["token", "lemma"]
        else:
            print("ERROR: No analyse type\n")
            exit()
        with open (path, "w", encoding="utf-8") as f_out:
            f_out.write("{}\t{}\n".format(header[0], header[1]))
            for key in dict:
                f_out.write("{}\t{}\n".format(key, dict[key]))
    
    def merge_dict(self, li_dicts):
        all_info = {}
        for dic in li_dicts:
            for key in dic:
                if key in all_info:
                    all_info[key].append(dic[key])
                else:
                    all_info[key] = [ dic[key] ]
        return all_info

    def to_conllu(self, dict, path):
        count = 1
        with open (path, "w", encoding="utf-8") as f_out:
            for key in dict:
                info = ""
                for elem in dict[key]:
                    if (isinstance(elem, str)):
                        info += elem + "\t"
                    elif (isinstance(elem, list)):
                        info += elem[0] + "\t"
                    elif (isinstance(elem, int)):
                        info += str(elem) + "\t"
                f_out.write("{}\t{}\t{}\n".format(str(count), key, info))
                count += 1