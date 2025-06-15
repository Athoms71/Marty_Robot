# Projet de Suivi et d'Analyse de Mouvements - Interface & Traitement

Ce projet est une application Python développée dans le cadre d’un travail collaboratif, visant à analyser et gérer les mouvements et émotions du robot Marty dans une interface graphique. Il comprend plusieurs modules pour le suivi en temps réel, la gestion de séquences, et l’analyse de données sensorielles ou gestuelles.

## Contenu du Projet

Le projet se compose des fichiers suivants :

### Fichiers Python principaux :

-   `main.py` — Point d’entrée principal de l’application.
-   `MainWindow.py` — Fenêtre principale de l’interface utilisateur.
-   `MouseTrackingWindow.py` — Module de suivi de mouvement via la souris.
-   `ConnectWindow.py` — Fenêtre de connexion au capteur ou interface externe.
-   `AbsoluteWindow.py` — Gestion d’une interface liée à des mouvements absolus.
-   `Moves.py`, `Sequential.py` — Modules de gestion des mouvements et des séquences.
-   `capteur.py` — Intégration ou simulation d’un capteur de mouvement.
-   `file_management.py` — Lecture, écriture et gestion des fichiers `.dance` ou `.feels`.
-   `emotions.py` — Probablement un module lié à l’analyse émotionnelle des mouvements.

### Fichiers de données :

-   `*.dance`, `*.feels`, etc. — Fichiers d’entrée contenant les données à analyser ou jouer (mouvements, séquences, émotions).

## Installation et Lancement

### Prérequis

-   Python 3.9 ou supérieur
-   pip (installateur de paquets Python)
-   Utilisation d’un environnement virtuel recommandée

### Dépendances Python

Installer les dépendances nécessaires :

```bash
pip install PyQt5 numpy
```

## Exécution

Pour lancer l'application :

```bash
python main.py
```

## Fonctionnalités

-   Interface graphique interactive avec PyQt5
-   Suivi de mouvement (via capteur ou souris)
-   Chargement et visualisation de fichiers `.dance`, `.feels`
-   Organisation des séquences de mouvements
-   Simulation ou traitement d’émotions liées aux gestes

## Arborescence type

```
projet/
├── main.py
├── *.py
├── *.dance
├── *.feels
└── README.md
```

## Auteurs

-   GABORIT Amaury
-   LOCTIN Thomas
-   PEYRONNET Emmanuel
-   RUSSIER Robin

## Licence

Ce projet est soumis à une licence universitaire dans le cadre d’un travail d’étude. Pour tout usage ou redistribution, veuillez contacter les auteurs.

## Perspectives d'amélioration

-   Intégration d’un vrai capteur (ex : Kinect, IMU)
-   Visualisation 3D des mouvements
-   Détection d’émotions en temps réel avec intelligence artificielle
-   Exportation des séquences au format vidéo ou CSV
