# Projet_oop_M2
Ce truc fait des analyses linguistiques pour les textes pures ou fichiers .txt en utilisant Spacy.

**Les types d'analyses sont:**
1. POS tagging
2. Statistics
3. Lemmatisation
4. Morphologie
5. Recherche de token

**Les formats d'entrée sont:**
1. Textes pures avec paramètre *--text* dans terminal
2. Fichiers .txt
3. textes pures dans terminal + fichier .txt (ils seront fusionné ensemble)

**Les formats de output sont:**
1. Affichage de résultats d'analyse dans terminal (Il faut indiquer type d'analyse avec *--analyse_type*)
2. Fichiers .csv avec les résultats de toutes types d'analyses
3. Fichiers .conllu avec les résultats de toutes types d'analyses

**Arguments dans terminal:**

```python
"--txt_path",           help = 'fichier d\'entrée en format .txt, utf-8'
"--text",               help = 'texte pure pour analyser'
"--analyse_type",       help = 'type d\'analyses linguistiques'
"--research_token",     help = 'token à rechercher dans le texte'
"--csv_path",           help = 'chemin pour sauvegarder fichier csv'
"--conllu_path",        help = 'chemin pour sauvegarder fichier conllu'
"--language",           help = 'langue (fr ou en), par default c\'est anglais'
"--min_len",            help = 'longeur minimal pour corpus, par default 1'
"--max_len",            help = 'longeur maximal pour corpus, par default 1000'
"--terminal_output",    help = 'True ou False pour cacher ou montrer output sur terminal'
```

##### Exemple de l'utilisation:
Pour les entrées qui sont des fichiers textes:
```shell
# Faire une analyse linguistique (ici POS tagging) pour des phrases dans un fichier:
python3 main.py --txt_path "input/try.txt" --analyse_type "pos"  --language "fr"
# Rechercher un token dans un fichier:
python3 main.py --txt_path "input/try.txt" --analyse_type "research" --research_token "football"  --language "fr"
# Faire sortir des fichiers csv et conllu qui contiennent touts les résultats des analyses linguistiques:
python3 main.py --txt_path "input/try.txt" --conllu_path "output/fr.conllu" --language "fr" --csv_path "output/fr.csv"
```

Pour les entrées qui sont des textes pures:
```shell
# Faire une analyse linguistique (ici POS tagging) pour une phrase insérée par terminal:
python3 main.py --text "The HEAD and DEPREL values define the basic dependencies which must be strictly a tree. However, in addition to these basic dependencies, treebanks may optionally provide an enhanced dependency 
representation that specifies additional dependency relations, for example, when dependencies propagate over coordinate structures. The enhanced dependency representation, which in general is a graph and not a tree, is specified in the DEPS field, using a list of head-relation pairs" --language "en" --analyse_type "pos"

# Rechercher un token dans la phrase:
python3 main.py --text "The HEAD and DEPREL values define the basic dependencies which must be strictly a tree. However, in addition to these basic dependencies, treebanks may optionally provide an enhanced dependency 
representation that specifies additional dependency relations, for example, when dependencies propagate over coordinate structures. The enhanced dependency representation, which in general is a graph and not a tree, is specified in the DEPS field, using a list of head-relation pairs" --language "en" --analyse_type "research" --research_token "tree"

# Faire sortir des fichiers csv et conllu qui contiennent touts les résultats des analyses linguistiques:
python3 main.py --text "The HEAD and DEPREL values define the basic dependencies which must be strictly a tree. However, in addition to these basic dependencies, treebanks may optionally provide an enhanced dependency 
representation that specifies additional dependency relations, for example, when dependencies propagate over coordinate structures. The enhanced dependency representation, which in general is a graph and not a tree, is specified in the DEPS field, using a list of head-relation pairs" --language "en" --csv_path "output/en.csv" --conllu_path "output/en.conllu"

```