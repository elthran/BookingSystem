# http://blog.keyrus.co.uk/fuzzy_matching_101_part_i.html
import pandas as pd
from fuzzywuzzy import process, fuzz

from booking import db
from booking.models import Client


def fuzzy_match(x, choices, scorer, limit):
    return process.extract(
        x, choices=choices, scorer=scorer, limit=limit
    )


def searchable_data(df, columns):
    """Return a searchable data matrix."""
    df['searchable_data'] = df[columns].apply(lambda x: ' '.join(x), axis=1)
    df = df.drop(columns, axis=1)
    df['searchable_data'] = df['searchable_data'].map(clean_data)
    return df


def clean_data(s):
    """Clean a string for search purposes.

    Add in any extra functions that seem useful.
    I only used these because I felt they gave the best results.
    """
    s = s.strip()
    s = s.lower()
    return s


def search_clients(keywords, business_id, limit=5):
    """Search restricted client set for similarity to keywords.

    Optimized to search only clients of this business.
    Optimized to ignore anonymous clients.
    Future: optimize Client.query.get() ... ? current way retain match order
    but produces 1 query per result.

    Uses: fuzz.token_set_ratio ... could use a more complex matching scheme.
    """
    cleaned_input = clean_data(keywords)

    # search_data = pd.DataFrame(data, columns=data.keys())
    client_data = pd.read_sql(
        sql="SELECT id, name, email, phone, business_id FROM client where business_id={} and email != 'anonymous@hidden.com';".format(
            business_id), con=db.engine, index_col='id')
    client_data = searchable_data(client_data, ['name', 'email', 'phone'])

    matching_results = fuzzy_match(cleaned_input, client_data.loc[:, "searchable_data"], fuzz.token_set_ratio, limit)
    # x[2] is the id of the client in order of matchingness. I hope.
    return [Client.query.get(x[2]) for x in matching_results]
