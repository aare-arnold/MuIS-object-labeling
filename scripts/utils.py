import re
import pandas
import unidecode

def clean_text(row: pandas.Series):
    columns = [
        'material', 'technique', 'museum_abbr', 'collection_mark',
        'name', 'commentary', 'participants_role', 'location', 'event_type',
        'text', 'parameter', 'unit', 'legend', 'initial_info',
    ]

    rows = [row[column] for column in columns]
    
    # list of words
    description = ' '.join(rows)
    # convert all characters to lowercase
    description = description.lower()
    # removing accented characters
    description = unidecode.unidecode(description)
    # remove extra whitespaces
    description = re.sub(r'^\s*|\s\s*', ' ', description).strip()

    return description
