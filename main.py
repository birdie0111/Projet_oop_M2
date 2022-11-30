from Text import Text
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--txt_path", help = 'fichier d\'entrée en format .txt, utf-8')
parser.add_argument("--text", help = 'texte pure pour analyser')
parser.add_argument("--analyse_type", help = 'type pour analyser')
parser.add_argument("--research_token", help = 'token to be searched in text')
parser.add_argument("--csv_path", help = 'chemin pour sauvegarder fichier csv')
parser.add_argument("--conllu_path", help = 'chemin pour sauvegarder fichier conllu')
parser.add_argument("--language", help = 'langue (fr ou en)')
parser.add_argument("--min_len", help = 'longeur minimal pour corpus')
parser.add_argument("--max_len", help = 'longeur maximal pour corpus')
parser.add_argument("--terminal_output", help = 'true or false to show or hide terminal output')



def merge_text(text, txt_path):
    """Fonction pour obtenir texte pures (S'il y a input dans terminal et dans un fichier, cette fonction va les fusionner ensemble)

        Args:
            text: String, texte inséré dans terminal
            txt_path: String, chemin vers fichier .txt comme input
        Returns:
            text: String, texte pure

    """
    if (text == None):
        text = ""
    if (txt_path != None):
        with open(txt_path, "r", encoding="utf-8") as f_ori:
            for line in f_ori:
                text += line
    return text

def main(text, txt_path, analyse_type, research_token, csv_path, conllu_path, language, min_len, max_len, terminal_output):
    text = merge_text(text, txt_path)
    t = Text(text, language, min_len, max_len)
    if (terminal_output == None):
        terminal_output = True
    
    # Fait les analyses et obtient les dictionnaires qui sauvegardent les résultats
    dic_pos = t.POS_tagging(terminal_output = False)
    dic_statistics = t.statistics(terminal_output = False)
    dic_lemma = t.lemma(terminal_output = False)
    dic_morpho = t.morphology(terminal_output = False)
    # Obtenir un dictionnaire qui sauvegarde tous les résultats
    all_info = t.merge_dict([dic_pos, dic_statistics, dic_lemma, dic_morpho])

    # Sortir fichiers csv et conllu
    if (csv_path != None):
        print("\nLe resultat d'analyse sera sauvegardé dans le fichier: " + csv_path + "")
        t.to_csv(all_info, csv_path)
    if (conllu_path != None):
        print("\nLe resultat d'analyse sera sauvegardé dans le fichier: " + conllu_path + "")
        t.to_conllu(all_info, conllu_path)

    # Affichage seule sur terminal
    if (conllu_path == None and csv_path == None):
        print("\nLe resultat d'analyse ne sera pas sauvegard.")
        if (analyse_type == "pos"):
            t.POS_tagging(terminal_output)
        elif (analyse_type == "statistics"):
            t.statistics(terminal_output)
        elif (analyse_type == "lemma"):
            t.lemma(terminal_output)
        elif (analyse_type == "morpho"):
            t.morphology(terminal_output)
        elif(analyse_type == "research"):
            times = t.research(research_token)
            print("\nLe token est apparaît {} fois dans le texte.\n".format(times))
        else:
            print("\nError: No analyse type\n")
            exit()

if __name__ == "__main__":
    args = parser.parse_args()
    text = args.text
    txt_path = args.txt_path
    csv_path = args.csv_path
    conllu_path = args.conllu_path
    analyse_type = args.analyse_type
    research_token = args.research_token
    
    language = "en" if args.language == None else args.language
    min_len = 1 if args.min_len == None else int(args.min_len)
    max_len = 1000 if args.max_len == None else int(args.max_len)

    terminal_output = args.terminal_output

    main(text, txt_path, analyse_type, research_token, csv_path, conllu_path, language, min_len, max_len, terminal_output)