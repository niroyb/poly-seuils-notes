poly-seuils-notes
=================

Analyse du fichier des résultats d'un cours à l'École Polytechnique de Montréal pour déterminer les seuils de chaque note. Les fichiers d'entrées peuvent être de type *txt* ou *pdf*, soient les deux formats qui sont envoyés aux étudiants.

L'analyse se fait en recherchant la valeur minimale et la valeur maximale pour chaque type de note.

Exécution
---------
Lancement du script:

    $ python main.py examples/foo1001.txt

Exemple de sortie:
```
32 notes :
 A* ( 4) [ 19.29 - 19.99 ]
 A  ( 4) [ 16.81 - 18.64 ]
 B+ ( 4) [ 14.29 - 15.80 ]
 B  ( 4) [ 13.77 - 14.25 ]
 C+ ( 4) [ 13.34 - 13.59 ]
 C  ( 3) [ 12.79 - 13.07 ]
 D+ ( 3) [ 11.65 - 12.19 ]
 D  ( 3) [ 10.72 - 11.38 ]
 F  ( 3) [  1.29 -  6.33 ]
```


Dependances
-----------

Le script est développé avec Python 2.7 et utilies la dépendance suivante:
  * [PyPDF2](http://mstamy2.github.io/PyPDF2/) ```pip install pypdf2```


TODO
----

  * Gestion d'exception si le module PyPDF2 n'est pas présent
