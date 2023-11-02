""" Define Urls"""
import requests
from bs4 import BeautifulSoup as bs
import json


class Urls:
    """ Définition de la class Urls"""
    def __init__(self, url, soup=""):
        """ Initialisation de la class"""
        self.url = url
        self.soup = soup

    def __repr__(self):
        """ représentation de l'objet de type Urls"""
        return self.url

    def connect_page(self):
        """methode permettant la connection à une url et la gestion des erreurs de saisie
        elle sera utilisé dans download_datas
        """
        try:
            response = requests.get(self)
            # test / ok si code 200, sinon stop
            if response.ok:
                print("1. Connecté à", self)
            else:
                print("erreur de connexion à ", self)
        except Exception:
            """En cas d'erreur de saisie le message apparait """
            print("L'url n'est pas valide, merci de corriger votre saisie.")

    def download_datas(self):
        """ Méthode permettant de lancer connect_page et de récupérer les données de la page grace à la librairie
        BeutifulSoup4
        ensuite on les place dans un object soup
        """
        Urls.connect_page(self)
        response = requests.get(self.url)
        self.soup = bs(response.content, 'lxml')
        print("   Les données de la page ", self.url, " ont été chargées.")


class UrlIndex(Urls):
    """ Création de la sous_classe UrlIndex pour les page d'index """
    def __init__(self, url, soup=""):
        super().__init__(url)
        self.url = url
        self.soup = soup

    def __repr__(self):
        return self.url

    def connect_page(self):
        super().connect_page()
        
    def download_datas(self):
        super().download_datas()

    def extract_urls_sidebar(self):
        """ Méthode permettant la récupération de la liste des urls index des pages de catégories """
        UrlIndex.download_datas(self)
        masoupdea = self.soup.findAll('a')
        """ extraction de la partie href et ajout dans la liste nameLinks_catego sous forme de liste
         avec le lien de la catégorie en position [1]et le nom de la catégorie en [0]
         la variable i va ajouter le numéro de la catégorie afin qu'il puisse etre utilisé pour créer d'autres urls
        """
        name_links_catego = []
        i = -2
        for a in masoupdea:
            i = i + 1
            istr = str(i)
            link_catego = a['href']
            name_catego = a.text
            name_catego = name_catego.lstrip("\n")
            name_catego = name_catego.strip()
            name_catego = name_catego.rstrip('\n')
            name_catego = name_catego+'_'+istr
            name_links_catego.append([name_catego, 'https://books.toscrape.com/' + link_catego])
        """ suppression des données inutiles """
        del (name_links_catego[0:3])
        del (name_links_catego[50:])
        """enregistrment de la liste dans un fichier json"""
        try:
            with open("Temp_name_links_catego.json", "w") as f:
                json.dump(name_links_catego, f)
                print('2. La liste_urls index est chargée')
        except Exception:
            print("Erreur a l'enregistrement du fichier Temp_name_links_catego.json .")

    def extract_urls_books(self):
        UrlIndex.download_datas(self)
        masoupdeh3 = self.soup.findAll('h3')


