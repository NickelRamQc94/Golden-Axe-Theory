# Golden-Axe Theory

Golden-Axe Theory (par Nickel David Grenier) explore une approche dimensionless pour évaluer l'instabilité et la turbulence des systèmes. Ce dépôt contient une page GitHub Pages, un utilitaire Python pour calculer Π_N, des tests et une licence MIT.

## Contenu du dépôt
- `index.html` : page GitHub Pages présentant le projet et un calculateur rapide.
- `tools/pi_n_calculator.py` : calculateur Python paramétrable pour Π_N.
- `LICENSE` : licence MIT.
- `.gitignore`, `requirements.txt`, tests et workflow CI.

## Définition (implémentation par défaut)
La fonction implémentée pour Π_N est :

Π_N = 0.8 * (std / mean) ** alpha

avec `alpha = 0.75` par défaut. Le calculateur renvoie un dictionnaire contenant Π_N, status, mean, std et data_points.

## Installation

1. Créez et activez un environnement virtuel (optionnel) :

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
.venv\Scripts\activate     # Windows (PowerShell)
```

2. Installez les dépendances :

```bash
pip install -r requirements.txt
```

## Utilisation

Exemple CLI :

```bash
python tools/pi_n_calculator.py --data 1.2 1.5 1.3 1.8 2.1
```

Exemple d'utilisation depuis Python :

```python
from tools.pi_n_calculator import PiNCalculator

calc = PiNCalculator(alpha=0.75)
res = calc.calculate([1.2,1.5,1.3,1.8,2.1])
print(res)
```

## Tests

Exécuter les tests :

```bash
pytest -q
```

## Auteur

Nickel David Grenier (GitHub: @NickelRamQc94)