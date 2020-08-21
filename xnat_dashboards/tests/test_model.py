from xnat_dashboards.app.dashboards import model as model_dash
from xnat_dashboards.app.auth import model as model_auth
from xnat_dashboards import path_creator


path_creator.set_dashboard_config_path(
    'xnat_dashboards/config/dashboard_config.json')


def test_user_exists(mocker):

    mocker.patch(
        'xnat_dashboards.pyxnat_interface.'
        'data_fetcher.Fetcher.get_instance_details',
        return_value=0)

    not_exist = model_auth.user_exists('x', 'y', 'z', 'p')

    assert type(not_exist) == list

    mocker.patch(
        'xnat_dashboards.pyxnat_interface.'
        'data_fetcher.Fetcher.get_instance_details',
        return_value=[])

    exist = model_auth.user_exists('x', 'y', 'z', 'p')

    assert exist == []


def test_user_role_exists(mocker):

    exists = model_auth.user_role_config('testUser')
    assert type(exists) == dict
    exists = model_auth.user_role_config('testUer')
    assert type(exists) is dict
    exists = model_auth.user_role_config('noUser')
    assert exists is False


def test_model():

    user_data = model_dash.load_users_data('https://central.xnat.org')
    assert type(user_data)

    user_data = model_dash.load_users_data('ttps://central.org')
    assert user_data is None
