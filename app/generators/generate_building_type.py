import pandas as pd

from app.config.settings import GENERATED_DIR, PROJECT_ROOT
from app.utils.file_utils import ensure_directory


def generate_building_type():

    source = PROJECT_ROOT / "data" / "reference" / "building_types.csv"

    df = pd.read_csv(source)

    ensure_directory(GENERATED_DIR)

    output = GENERATED_DIR / "DimBuildingType.csv"

    df.to_csv(output, index=False)

    print(f"✓ DimBuildingType generated ({len(df)} rows)")