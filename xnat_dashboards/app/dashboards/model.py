import pickle
from xnat_dashboards import path_creator

"""
This is a dashboard model. Here pickle related
function are present for displaying the pickle data.

load_users_data: Loads the pickle data.
"""


def load_users_data(server):

    try:
        with open(
                path_creator.get_pickle_path(), 'rb') as handle:
            user_data = pickle.load(handle)

        if user_data['server'] != server:
            return None
    except FileNotFoundError:
        return None

    return user_data
