# config.py

from pathlib import Path
import matplotlib.pyplot as plt

# =========================================================
# PATHS
# =========================================================

# Root directory of the project
ROOT_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

NOTEBOOKS_DIR = ROOT_DIR / "notebooks"

OUTPUTS_DIR = ROOT_DIR / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"
TABLES_DIR = OUTPUTS_DIR / "tables"


# =========================================================
# CREATE DIRECTORIES (if not exist)
# =========================================================

for path in [
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    FIGURES_DIR,
    TABLES_DIR,
]:
    path.mkdir(parents=True, exist_ok=True)


# =========================================================
# SAVE FIGURE HELPER
# =========================================================

def savefig(fig, filename, dpi=300):
    """
    Save matplotlib figure to outputs/figures/
    """
    filepath = FIGURES_DIR / filename
    fig.savefig(filepath, dpi=dpi, bbox_inches="tight")
    print(f"Saved figure to: {filepath}")


# =========================================================
# PROJECT SETTINGS
# =========================================================

# Time resolution: 'daily' or 'hourly'
TIME_RESOLUTION = "daily"

# Prediction horizons (in time steps)
HORIZONS = [1, 2, 3, 4]

# Random seed
RANDOM_STATE = 42


# =========================================================
# MODEL SETTINGS
# =========================================================

MODEL_CONFIGS = {
    "linear": {
        "type": "linear"
    },
    "rf": {
        "type": "random_forest",
        "n_estimators": 100,
        "max_depth": None
    },
    "gb": {
        "type": "gradient_boosting",
        "n_estimators": 100,
        "learning_rate": 0.1
    }
}


# =========================================================
# FEATURE SETTINGS
# =========================================================

# Lag features (in time steps)
LAG_FEATURES = [1, 2, 3, 7]

# Weather features toggle
USE_WEATHER = True

# =========================================================
# PLOTTING STYLE (optional but nice)
# =========================================================

plt.style.use("seaborn-v0_8")
