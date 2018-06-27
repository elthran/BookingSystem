import pandas as pd
from fuzzywuzzy import process, fuzz

# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request
# Import session management
from flask_login import login_required, current_user
from booking.models.bases import db
from booking.models.forms.client import ClientSearchForm


@app.route('/business/clients/', methods=['GET', 'POST'])
@app.route('/business/clients/<int:business_id>/', methods=['GET', 'POST'])
@login_required
def clients(business_id=1):
    form = ClientSearchForm(request.form)
    if form.validate_on_submit():
        terms = form.keywords.data
        # name, email, phone
        # convert terms to pd data array thingy
        # should be able to parse name, email, phone# into the correct
        # columns

        client_data = pd.read_sql(sql="SELECT id, name, email, phone FROM client;", con=db.engine, index_col='id')

        def fuzzy_match(x, choices, scorer, cutoff):
            return process.extractOne(
                x, choices=choices, scorer=scorer, score_cutoff=cutoff
            )

        print(client_data.loc[:, :])

    # match = process.extractOne(
    #     client_data.loc[0, column],
    #     choices=data_2.loc[:, column],
    #     scorer=fuzz.ratio,
    #     score_cutoff=80
    # )

    # matching_results = client_data.loc[:, :].apply(
    #     fuzzy_match,
    #     args=(
    #         client_data.loc[:, :],
    #         fuzz.ratio,
    #         80
    #     )
    # )
    # print(client_data)

    clients = current_user.business.get_clients()
    #http://blog.keyrus.co.uk/fuzzy_matching_101_part_i.html
    return render_template("business/clients.html", clients=clients, form=form)
