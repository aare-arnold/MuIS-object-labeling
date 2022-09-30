import typer
import pandas as pd
import numpy as np
from pathlib import Path

def test(input_path: Path, output_path: Path):
    train = pd.read_csv(input_path, encoding='utf-8')
    train = train.replace(({ np.nan: '' }))

    data = train.sample(frac=1)

    data.to_csv(output_path, encoding='utf-8', index=False)


if __name__ == "__main__":
    typer.run(test)
