from flask import Flask, render_template, jsonify, request ,redirect, url_for
import sys,os
import base64
import subprocess
import json
import collections
import string
from unidecode import unidecode
import requests
import base64


UPLOAD_FOLDER = 'Codes'
ALLOWED_EXTENSIONS = {'c'}


def open_classement_read():
    with open('classement.json') as Read :
        classement = json.load(Read)
    return classement


def open_classement_write(val_add):
    with open('classement.json') as Read :
        classement = json.load(Read)
        classement.update(val_add)

    with open('classement.json', 'w') as mon_fichier:
        json.dump(classement,mon_fichier)

def sort_classement():
    
    with open('classement.json') as Read :
        classement = json.load(Read)
    classement = {key: val for key, val in sorted(classement.items(), key=lambda value: value[1])}
    print (classement)
    
    with open('classement.json', 'w') as mon_fichier:
            json.dump(classement,mon_fichier)
            
    return classement


def propre(source):
    # URL du micro-service d'analyse de code C
    url = "http://savoircoder.fr:7979/api/analyse/"

    # Lecture du fichier source
    code_source = open(source,"r").read()
    # Encodage du fichier source
    message_bytes = code_source.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    chaine = base64_bytes.decode('ascii')

    # Construction de la requete et reception du resultat
    payload={'code': chaine,'langage': 'C'}
    files=[]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    # Affichage du code de résultat: 200 si tout se passe bien
    print(response.status_code)

    # Enregistrement du résultat sous la forme d'un fichier au format json
    # Possibilité d'ouvrir ce fichier avec firefox
    fichier = open("resultat.json","w")
    fichier.write(response.text)
    fichier.close()

def time():
    #On ouvre le fichier json :
    name_file = "resultat.json"

    with open(name_file,'r', encoding='utf-8') as jsonRead:
        dico = json.load(jsonRead)
    #parcourons le fichier json pour trouver la bonne fonction :
    for cle in dico['informations']['functions'].keys():
        #print(dico['informations']['functions'][cle]['code'])
   #envoyer le code retirer dans un autre ficheir
        chaine = dico['informations']['functions']["factorielle_iterative"]['code']
        fichier = open("propre.c","w")
        fichier.write("#include <stdio.h>\n#include <stdlib.h>\n#include <time.h>\n")
        fichier.write(chaine)
        #fichier.write('\nint main(){\nclock_t deb = clock();\n\nif(factorielle_iterative(5) == 120){\nfor(int i=0;i<=9999999;i++){\nfactorielle_iterative(40);\n}\nclock_t fin=clock()-deb;\n\nreturn fin;\n}}\nreturn -1\n\n')
        fichier.write('\nint main(){\nclock_t deb = clock();\nfor(int i=0;i<=1000000;i++){\nfactorielle_iterative(40);\n}\nclock_t fin=clock()-deb;\nFILE * tmp = NULL;\n tmp = fopen("tmp.txt","w");\n\nfprintf(tmp,"%ld",fin);\nfclose(tmp);\nreturn fin;\n}\n\n')
        fichier.close()

    subprocess.run(['gcc','propre.c','-o','propre'])
    command = ["./propre"]
    process = subprocess.Popen(command,stdout = subprocess.PIPE, stderr=subprocess.PIPE)
    output,err = process.communicate()
    return process.returncode


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['get','post'])
def home():
    classement = sort_classement()
    print(classement)
    
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        fichier = request.files.get('file')

        if 'file' not in request.files:
            return redirect('/')
        name = nom+" "+prenom
        regiseter_name = name+".c"
        fichier.save(os.path.join(app.config['UPLOAD_FOLDER'],regiseter_name))
        #verifier le code c :
        chemain ="Codes/"+regiseter_name 
        propre(chemain)
        time_var = str(time())
        if time_var == "-1": return "nous n'avons pas pue repondre a votre demande"
        #! si meme score ca remplace
        add = {name:time_var}
        open_classement_write(add)
        return redirect('/')
            
    return render_template('home.html',classement =classement)

@app.route('/build', methods=['get','post'])
def build():
    return "la page est en cours de conception retourner en arriere"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    #http://localhost:8080/
    app.run(debug=True, host='0.0.0.0', port=port)
