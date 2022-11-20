from Text import Text
from argparse import ArgumentParser
#import csv

parser = ArgumentParser()
parser.add_argument("--txt_path", help = 'fichier d\'entrée en format .txt, utf-8')
parser.add_argument("--text", help = 'texte pure pour analyser')
parser.add_argument("--analyse_type", help = 'type pour analyser')
parser.add_argument("--research_token", help = 'token to be searched in text')
parser.add_argument("--csv_path", help = 'chemin pour sauvegarder fichier csv')
parser.add_argument("--language", help = 'langue (fr ou en)')
parser.add_argument("--min_len", help = 'longeur minimal pour corpus')
parser.add_argument("--max_len", help = 'longeur maximal pour corpus')


def to_csv(analyse_type, dict, path):
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
        f_out.write("{},{}\n".format(header[0], header[1]))
        for key in dict:
            f_out.write("{},{}\n".format(key, dict[key]))

def merge_text(text, txt_path):
    if (text == None):
        text = ""
    if (txt_path != None):
        with open(txt_path, "r", encoding="utf-8") as f_ori:
            for line in f_ori:
                text += line
    return text

def main(text, txt_path, analyse_type, research_token, csv_path, language, min_len, max_len):
    text = merge_text(text, txt_path)
    t = Text(text, language, min_len, max_len)
    if (csv_path != None):
        print("\nLe resultat d'analyse sera sauvegardé dans le fichier: " + csv_path + "")

        if (analyse_type == "pos"):
            pos_dict = t.POS_tagging()
            to_csv(analyse_type, pos_dict, csv_path)
        elif (analyse_type == "statistics"):
            stat_dict = t.statistics()
            to_csv(analyse_type, stat_dict, csv_path)
        elif (analyse_type == "lemma"):
            lemma_dict = t.lemma()
            to_csv(analyse_type, lemma_dict, csv_path)
    else:
        print("\nLe resultat d'analyse ne sera pas sauvegard.")

        if (analyse_type == "pos"):
            t.POS_tagging()
        elif (analyse_type == "statistics"):
            t.statistics()
        elif (analyse_type == "lemma"):
            t.lemma()
        elif(analyse_type == "research"):
            times = t.research(research_token)
            print("\nLe token est apparaît {} fois dans le texte.\n".format(times))

if __name__ == "__main__":
    args = parser.parse_args()
    text = args.text
    txt_path = args.txt_path
    csv_path = args.csv_path
    analyse_type = args.analyse_type
    research_token = args.research_token
    
    language = "en" if args.language == None else args.language
    min_len = 1 if args.min_len == None else int(args.min_len)
    max_len = 1000 if args.max_len == None else int(args.max_len)

    main(text, txt_path, analyse_type, research_token, csv_path, language, min_len, max_len)