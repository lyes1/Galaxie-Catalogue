# Catalogue des galaxies
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://tldrlegal.com/license/apache-license-2.0-%28apache-2.0%29#summary)

Création d'une API pour interroger un catalogue sur les objets célestes les plus célèbres.

## Pour commencer

La première étape consiste à récolter les données contenant les objets célestes. Nous avons assemblé les objets listés dans 3 catalogues bien connus (Messier, Caldwell et Heschel400). Ainsi, on a une base de données constituée de **558 objets**. Puis, nous avons enrichi les descriptions de nos objets avec des données présentes, notamment dans le catalogue NGC  de [OpenNGC](https://github.com/mattiaverga/OpenNGC) et des images pour certains objets.

### Pré-requis

- *Python*
- *Pandas* si vous voulez manipuler et intégrer de nouvelles données
- *SQLite3* pour la manipulation de la base de donnée.
- *Flask*

### Utilsation de l'API en ligne
L'API est accessible en production pour la tester et l’interroger sous l'URL [lyes.pythonanywhere.com/api/celestialObjetcs](http://lyes.pythonanywhere.com/api/celestialObjetcs). Pour plus d'informations sur l'utilisation de l'API veuillez consulter la section **Utilisation de la Web API** dans le document [Documentation.md](https://github.com/lyes1/Galaxie-Catalogue/blob/master/Documentation.md#use).

### Contribution et amélioration

La contribution peut être réalisée sur plusieurs niveaux :
- Améliorer la complétion des données (Voir les sections [Préparation des données](https://github.com/lyes1/Galaxie-Catalogue/blob/master/Documentation.md#prep) et [Complétude des données](https://github.com/lyes1/Galaxie-Catalogue/blob/master/Documentation.md#comp)).
- Améliorer les performances de l'application en migrant vers une base de données plus performante et intégration d'un ORM tel que Pony.

## Catalogue fabriqué avec les données récupérées de notamment: 

* [OpenNGC](https://github.com/mattiaverga/OpenNGC)
* [Messier catalogue](https://github.com/jbcurtin/messier-catalogue)
* [Messier catalogue of Datastro](https://www.datastro.eu/explore/dataset/catalogue-de-messier/table/?disjunctive.objet&disjunctive.mag&disjunctive.english_name_nom_en_anglais&disjunctive.french_name_nom_francais&disjunctive.latin_name_nom_latin&sort=messier)
* [Messier, Caldwell, Heschel400 and NGC catalogues](https://www.nexstarsite.com/Book/DSO.htm)
* Voir [reference.md](https://github.com/lyes1/Galaxie-Catalogue/blob/master/1_Data_brute/reference.md) pour la liste exhaustive.


## Versions

**Dernière version stable :** 0.0

## Auteurs
* **Lyes BOUALI** [@lyes1](https://github.com/lyes1)
* **Branda CHIRATA**  [@brendachirata](https://github.com/brendachirata)
* **Chérif DIOP**  [@cherifdiop](https://github.com/cherifdiop)
* **NDIAYE MARIAMA**  [@Mariaman](https://github.com/Mariaman)

## License

Ce projet est sous licence ``Appache 2.0``
