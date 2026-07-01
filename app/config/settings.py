from pathlib import Path

# ===================================
# Project Paths
# ===================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
GENERATED_DIR = DATA_DIR / "generated"
PROCESSED_DIR = DATA_DIR / "processed"

# ===================================
# Dataset Configuration
# ===================================

START_DATE = "2017-01-01"
END_DATE = "2026-12-31"

NUM_CUSTOMERS = 1200
NUM_BUILDINGS = 15000
NUM_VENDORS = 500

GERMAN_CITIES = 80

RANDOM_SEED = 42