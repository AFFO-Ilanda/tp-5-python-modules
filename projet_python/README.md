# TP 5 – Travaux Pratiques sur les Modules Python

## Objectif

Ce projet est réalisé dans le cadre du TD 5 de Programmation Python (Licence 2 GL 2025/2026).  
Il couvre la création et l'organisation de modules, les imports relatifs, la gestion de `__all__`, et l'utilisation de modules externes.

## Structure du projet

```
projet_python/
├── __init__.py
├── main.py
├── main2.py
├── main3.py
├── meteo_main.py
├── requirements.txt
├── README.md
├── captures/
│   └── (captures d'écran des exécutions)
├── maths/
│   ├── __init__.py
│   ├── operations.py
│   └── statistiques.py
└── utils/
    ├── __init__.py
    └── string_utils.py
```

## Installation

### 1. Créer un environnement virtuel (optionnel mais recommandé)

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

## Exécution

```bash
python projet_python/main.py
python -m projet_python.main2
python projet_python/main3.py
python projet_python/meteo_main.py
```

> **Note :** Pour `meteo_main.py`, remplace la valeur de `API_KEY` par ta vraie clé API obtenue sur [openweathermap.org](https://openweathermap.org/).
