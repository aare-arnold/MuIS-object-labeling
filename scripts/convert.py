"""Convert textcat annotation from CSV to spaCy v3 .spacy format."""
import typer
import pandas as pd
import numpy as np
from pathlib import Path
import re

import spacy
from spacy.tokens import DocBin
from spacy.tokens import Doc

import utils

def strp_string(text):
    return text.strip()

def convert(lang: str, input_path: Path, input_types_path: Path, output_path: Path):
    nlp = spacy.blank(lang)

    db = DocBin()

    data = pd.read_csv(input_path, encoding='utf-8')
    data = data.replace(({ np.nan: '' }))

    types = pd.read_csv(input_types_path, encoding='utf-8', converters={
        'type': strp_string
    })

    for index, row in data.iterrows():
        text = utils.clean_text(row)
        
        if (len(text) == 0): continue

        doc = nlp.tokenizer(text)
        doc_cat = strp_string(row['type'])
        doc.cats = { t['type']: 0 for i, t in types.iterrows() }
        doc.cats[doc_cat] = 1
        db.add(doc)

    db.to_disk(output_path)


if __name__ == "__main__":
    typer.run(convert)
