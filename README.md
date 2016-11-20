# SciMS
CMS for Scientific papers, Rouen Normandy University

## Énoncé du projet

Le mini projet consiste à réaliser un petit CMS (Content Management Software) que l’on peut assimiler à un blog multi-utilisateur. Les articles seront à caractère scientifique c’est à dire que leur style de présentation se situera entre l’article web et l’article scientifique, et l’on souhaitera y retrouver les fonctionnalités dont l’on dispose en LaTeX, comme par exemple les références automatiques à des éléments (figures, sections, ...) ou
bibliographiques, la numérotation automatique.

Ces fonctionnalités devront être réparties de manières appropriées sur les différents paradigmes (structuration, feuilles de styles, Javascript, ...) 
Un article sera structuré de la manière suivante :

* un article possède un titre, un auteur (utilisateur de la plate-forme), une date de publication, une catégorie de classement ;
* un article possède un résumé (abstract), ainsi qu’une liste de mot-clés (keywords) en général affiché au début ;
* un article sera structuré en section, sous-section ;
* le contenu des (sous)sections sera divisé en paragraphes, figures, formule mathématique;
* Les figures pourront être des images bitmap ou du contenu vectoriel (SVG) ; 
* une figure dispose d’un numéro pour les références et d’une légende qui seront affichés en dessous.
* Une formule mathématique sera numérotée (voir fichier d’exemple, page 3) pour y faire également référence ;
* Les formules seront saisies en LaTeX et automatiquement transformées en MathML. Une solution sera proposée plus tard.
* Un article se termine par une liste de références (voir fichier d’exemple, page 20).
* L’auteur pourra éventuellement décider d’incorporer un sommaire à une position de son choix qui affichera la structure des sections/sous-sections et permettra d’accéder directement à ces dernières en
cliquant sur leur nom.

L’interface principale de l’application sera divisée en plusieurs parties :
* un bandeau supérieur éventuellement personnalisable ;
* la partie principale ou seront affichés les articles, l’éditeur d’article ou bien les catégories et leur contenu, etc. ;
* un menu vertical à gauche permettant de naviguer dans les catégories d’articles, de se loger, d’accéder aux fonctionnalités d’un utilisateur authentifié.

Les catégories servent à classer les articles (exemple : informatique, mathématiques, physique, chimie, ...).

## Réalisation

* Le sujet vous est communiqué maintenant afin que vous puissiez commencer progressivement sa réalisation au fur et à mesure des thèmes abordés. Évitez de développer des parties avant leur introduction en
cours.
* Du temps pourra y être consacré en TP lorsque les exercices sont terminés.
* Le travail sera à rendre avant les vacances de fin d’année et pourra être réalisé en binôme maximum.

