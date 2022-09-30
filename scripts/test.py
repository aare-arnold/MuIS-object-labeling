import typer
import pandas as pd
import numpy as np
from pathlib import Path

import spacy

import utils

def test(model: str, input_path: Path, output_path: Path):
    nlp = spacy.load(model)
    
    data = pd.read_csv(input_path, encoding='utf-8')
    data = data.replace(({ np.nan: '' }))

    docs = [nlp.tokenizer(utils.clean_text2(row)) for index, row in data.iterrows()]
    textcat = nlp.get_pipe('textcat')

    scores = textcat.predict(docs)
    predicted_labels = scores.argmax(axis=1)

    result = { 'id': [], 'type': [] }

    for index, label in enumerate(predicted_labels):
        result['id'].append(data.iloc[index]['id'])
        result['type'].append(textcat.labels[label])

    df = pd.DataFrame(result)
    df.to_csv(output_path, encoding='utf-8', index=False)


if __name__ == "__main__":
    typer.run(test)
