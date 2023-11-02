import json

class Controller:
    """ Main controller. """

    def createListPagesCategory(json_file):
        try:
            with open(json_file, "r") as f:
                name_links_catego = json.load(f)
        except Exception:
            print("Erreur a l'ouverture du fichier Temp_name_links_catego.json .")

        for i in range(50):
            p = 1
            namelink = name_links_catego[i]
            link = (namelink[1])[:-10]
            name = (namelink[0])
            # le IF charge les indexs et traite la première page
            if i == 0:
                name_links_allpages = name_links_catego


            p = p + 1
            nextlink = link + 'page-' + str(p) + '.html'
            name_links_allpages.append([name, nextlink])
            # print('Liste ', name , 'complétée avec : ' , 'la page' , p , nextlink)
            while p <= 7:
                p = p + 1
                nextlink2 = link + 'page-' + str(p) + '.html'
                name_links_allpages.append([name, nextlink2])

        print('   La liste commence par :', name_links_allpages[0], '\n', '  et se termine par :', name_links_allpages[-1])
        print('   La liste comporte maintenant :', len(name_links_allpages), 'URL(s) de pages')
        try:
            with open("Temp_name_links_allpages.json", "w") as f:
                json.dump(name_links_catego, f)
        except Exception:
            print("Erreur a l'enregistrement du fichier Temp_name_links_catego.json .")




