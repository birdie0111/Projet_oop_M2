# Projet_oop_M2
nlp treatments for pure texts using spacy

##### Arguments dans terminal:

```python
"--txt_path",           help = 'fichier d\'entrée en format .txt, utf-8'
"--text",               help = 'texte pure pour analyser'
"--analyse_type",       help = 'type pour analyser'
"--research_token",     help = 'token to be searched in text'
"--csv_path",           help = 'chemin pour sauvegarder fichier csv'
"--language",           help = 'langue (fr ou en)'
"--min_len",            help = 'longeur minimal pour corpus'
"--max_len",            help = 'longeur maximal pour corpus'
```

##### Exemple de l'utilisation:
```shell
# POS tagging pour des phrases dans un fichier:
python3 main.py --txt_path "input/try.txt" --analyse_type "pos"  --language "fr"
# Rechercher un token dans un fichier:
python3 main.py --txt_path "input/try.txt" --analyse_type "research" --research_token "football"  --language "fr"

# Faire la lemmatization d'une phrase et sauvegarder le résultat dans un fichier csv:
python3 main.py --text "I just got it." --analyse_type "lemma" --csv_path "output/try.csv" 
```