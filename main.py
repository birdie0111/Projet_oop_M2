from Text import Text
from argparse import ArgumentParser
#import csv

parser = ArgumentParser()
parser.add_argument("--text", help = 'texte pure pour analyser')
parser.add_argument("--analyse_type", help = 'type pour analyser')
parser.add_argument("--csv_path", help= 'chemin pour sauvegarder fichier csv')
parser.add_argument("--language", help = 'langue (fr ou en)')
parser.add_argument("--min_len", help = 'longeur minimal pour corpus')
parser.add_argument("--max_len", help = 'longeur maximal pour corpus')


def to_csv(analyse_type, dict, path):
    if (analyse_type == "pos"):
        header = ["token", "POS"]
    elif (analyse_type == "statistics"):
        header = ["token", "Frequence"]
    else:
        print("ERROR: No analyse type\n")
        exit()
    with open (path, "w", encoding="utf-8") as f_out:
        f_out.write("{},{}\n".format(header[0], header[1]))
        for key in dict:
            f_out.write("{},{}\n".format(key, dict[key]))

def main(text, analyse_type, csv_path, language, min_len, max_len):
    if (csv_path != None):
        print("\nLe resultat d'analyse sera sauvegarde dans le fichier: " + csv_path + "")
        t = Text(text, language, min_len, max_len)
        if (analyse_type == "pos"):
            pos_dict = t.POS_tagging()
            to_csv(analyse_type, pos_dict, csv_path)
        elif (analyse_type == "statistics"):
            stat_dict = t.statistics()
            to_csv(analyse_type, stat_dict, csv_path)
    else:
        print("\nLe resultat d'analyse ne sera pas sauvegard.")
        t = Text(text, language, min_len, max_len)
        if (analyse_type == "pos"):
            pos_dict = t.POS_tagging()
        elif (analyse_type == "statistics"):
            stat_dict = t.statistics()

if __name__ == "__main__":
    args = parser.parse_args()
    text = args.text
    csv_path = args.csv_path
    analyse_type = args.analyse_type
    language = "en" if args.language == None else args.language
    min_len = 1 if args.min_len == None else int(args.min_len)
    max_len = 1000 if args.max_len == None else int(args.max_len)

    main(text, analyse_type, csv_path, language, min_len, max_len)