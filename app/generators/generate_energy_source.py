import pandas as pd

from app.config.settings import GENERATED_DIR, PROJECT_ROOT
from app.utils.file_utils import ensure_directory


def generate_energy_source():

    source = PROJECT_ROOT / "data" / "reference" / "energy_sources.csv"

    df = pd.read_csv(source)

    ensure_directory(GENERATED_DIR)

    output = GENERATED_DIR / "DimEnergySource.csv"

    df.to_csv(output, index=False)

    print(f"✓ DimEnergySource generated ({len(df)} rows)")
