import spacy

class Text:
    def __init__(self, content = None, langue = "en", min_len = 1, max_len = 1000):
        self.content = content
        self.langue = langue
        self.min_len = min_len
        self.max_len = max_len
        self.nlp_toks = self.nlp_treatment()

    def nlp_treatment(self):
        """Fonction pour choisir les langues et obtenir les nlp tokens par Spacy

        Args:
            None
        Returns:
            toks: token de Spacy

        """
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
        """Funtion qui fait part-of-speech pour les tokens

        Args:
            terminal_output: True ou False pour contrôler l'affichage sur terminal

        Returns:
            pos_dic: dictionnaire qui contient chaque token comme clé, et POS comme valeurs

        """
        pos_dic = {}
        if (terminal_output):
            print("\nPOS tagging results:\n")
            for tok in self.nlp_toks:
                print("{} ---> {}\n".format(tok.text, tok.pos_))
        else:
            for tok in self.nlp_toks:
                if (tok.text not in pos_dic):
                    pos_dic[tok.text] = [tok.pos_]
                else:
                    if (pos_dic[tok.text][0] != tok.pos_): # Si il y a different POS pour un meme mot:
                        pos_dic[tok.text].append(tok.pos_)
        return pos_dic
    
    def statistics(self, terminal_output):
        """Funtion qui compte fréquences des tokens

        Args:
            terminal_output: True ou False pour contrôler l'affichage sur terminal

        Returns:
            stat_dic: dictionnaire qui contient chaque token comme clé, et fréquence comme valeurs

        """
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
        """Funtion qui fait lemmatisation

        Args:
            terminal_output: True ou False pour contrôler l'affichage sur terminal

        Returns:
            lemma_dic: dictionnaire qui contient chaque token comme clé, et lemma comme valeurs

        """
        lemma_dic = {}
        if (terminal_output):
            print("\nLemma:\n")
            for tok in self.nlp_toks:
                print("{} ---> {}\n".format(tok.text, tok.lemma_))
        else:
            for tok in self.nlp_toks:
                lemma_dic[tok.text] = tok.lemma_
                    
        return lemma_dic
        
    def research(self, tok_cherche):
        """Funtion qui cherche un token

        Args:
            tok_cherche: String, un token pour chercher dans le texte

        Returns:
            appear_times: int, nombre de fois qu'un token apparaît
        """
        appear_times = 0
        for tok in self.nlp_toks:
            if (tok.text == tok_cherche or tok.lemma_ == tok_cherche):
                appear_times += 1
        return appear_times
    
    def morphology(self, terminal_output):
        """Funtion qui fait morphologie

        Args:
            terminal_output: True ou False pour contrôler l'affichage sur terminal

        Returns:
            morpho_dic: dictionnaire qui contient chaque token comme clé, et morphologie comme valeurs

        """
        morpho_dic = {}
        if (terminal_output):
            print("\nmorphology:\n")
            for tok in self.nlp_toks:
                print("{} ---> {}\n".format(tok.text, tok.morph))
        else:
            for tok in self.nlp_toks:
                morpho_dic[tok.text] = str(tok.morph)
            return morpho_dic

    def length_verify(self, min, max):
        """Funtion qui vérifie si la longueur de texte est bon

        Args:
            min: int, longueur minimum
            max: int, longueur maximum

        Returns:
            True si la longueur est suffisante, False sinon

        """
        if (self.content != None):
            return (len(self.content) >= min and len(self.content) <= max)
        else:
            print("ERROR: No input text.\n")
            return False
    
    def to_csv(self, dict, path):
        """Funtion qui regroupe les résultats d'analyse et les écrit dans un fichier csv

        Args:
            dict: dictionnaire, un dictionnaire qui contient tous les résultats d'analyse
            path: string, chemin pour sauvegarder le fichier csv

        Returns:
            None

        """
        header = ["id","token", "POS", "statistics", "lemma", "morphology"]
        count = 1
        with open (path, "w", encoding="utf-8") as f_out:
            for h in header:
                f_out.write(h + ",")
            f_out.write("\n")
            for key in dict:
                info = ""
                for elem in dict[key]:
                    if (isinstance(elem, str)):
                        info += elem + ","
                    elif (isinstance(elem, list)):
                        info += elem[0] + ","
                    elif (isinstance(elem, int)):
                        info += str(elem) + ","
                count += 1
                f_out.write("{},{},{}\n".format(str(count), key, info))
    
    def merge_dict(self, li_dicts):
        """Funtion qui fusionne les dictionnaires

        Args:
            li_dict: list, une liste des dictionnaires

        Returns:
            all_info: un nouveau dictionnaire qui continennent tous les résultats d'analyse

        """
        all_info = {}
        for dic in li_dicts:
            for key in dic:
                if key in all_info:
                    all_info[key].append(dic[key])
                else:
                    all_info[key] = [ dic[key] ]
        return all_info

    def to_conllu(self, dict, path):
        """Funtion qui regroupe les résultats d'analyse et les écrit dans un fichier conllu

        Args:
            dict: dictionnaire, un dictionnaire qui contient tous les résultats d'analyse
            path: string, chemin pour sauvegarder le fichier conllu

        Returns:
            None

        """
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