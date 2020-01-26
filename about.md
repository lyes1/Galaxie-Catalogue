# Catalogue astronomique en ligne

## Membres de goupe
- Lyes BOUALI
- Branda CHIRATA
- Chérif DIOP

## Données du catalogue
- Numéro NGC de l'objet,
- Numéro de l'objet dans les 3 catalogues amateurs : Messier (M#), Caldwell (C#) ou Herschel 400 (H#),
- Nom commun de l'objet,
- Type de l'objet: galaxie, nébuleuse, amas stellaire, ou autres objets (Étoile binaire, ), 
- Sous type de l'objet si applicable : Galaxie (elliptique, spérale, lenticulaire ou irrégulière), nébuleuse (obscure, diffuse par réflexion/émission, planétaire), amas d'étoiles ( ouvert, globulaire)
- Nom de la constellation à laquelle l'objet appartient.
- Distance en kal (kilo année-lumière)
- Magnitude et taille apparentes
- Ascension Droite, Déclinaison
- Image de l'objet
- Date de découverte,
- Nom de découvreur
- Notes d'observation
- Observable / non observable

## Intérêt sientifique du catalogue
Notre catalogue trouve son intérêt dans le cadre de l’astronomie amateur. Il liste les objets observables depuis la terre. Il est utile pour tous les observateurs du ciel (équipés d’un télescope ou d’une lunette astronomique) quelque soit leurs positions. En effet, notre catalogue collecte **558 objets** des plus beaux qui peuvent être obsérvés sous toutes les déclinaison.
Dans le catalogue de **Messier**, on trouve **110 objets** observables en haute déclinaison (uniquement dans hémisphère nord). Nous ajoutons les **109 objets** du catalogue **Caldwell** observables depuis l'hémisphère sud du globe. Notre catalogue est enrichi par les **339 objets** (non présent dans les catalogues de Messier et Caldwell) listés dans le catalogue **Herschel 400**.

## Source de données
* [OpenNGC](https://github.com/mattiaverga/OpenNGC)
* [Messier catalogue](https://github.com/jbcurtin/messier-catalogue)
* [Messier catalogue of Datastro](https://www.datastro.eu/explore/dataset/catalogue-de-messier/table/?disjunctive.objet&disjunctive.mag&disjunctive.english_name_nom_en_anglais&disjunctive.french_name_nom_francais&disjunctive.latin_name_nom_latin&sort=messier)
* [Messier, Caldwell, Hescheller 400 and NGC catalogues](https://www.nexstarsite.com/Book/DSO.htm)



## Fonctionnalités minimales
- Recherche et tri par constellation, taille et distance de l'objet.

## Fonctionnalités idéales
- ajout d'informations complémentaires sur chaque objet avec carte celestre.

## Technologies indispensables 
- Pandas pourla consolidation des données
- SQLite pour la consolidation et le stockage  des données récupérées depuis les trois catalogues ,
- Interface graphique et design.