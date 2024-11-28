import pytest


class TestViews:

    @pytest.mark.django_db
    def test_list_with_created_at_filter_SHOULD_return_200_and_items(self, api_client):
        response = api_client.get('/inventory/?created_at=1914-10-01')
        assert len(response.json()) > 0
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_list_inventory_SHOULD_return_200_and_items(self, api_client):
        response = api_client.get('/inventory/')
        assert len(response.json()) > 0
        assert response.status_code == 200


    @pytest.mark.django_db
    def test_list_with_wrong_created_at_format_SHOULD_return_400(self, api_client):
        response = api_client.get('/inventory/?created_at=10-01-2019')
        assert response.status_code == 400


    @pytest.mark.django_db
    def test_list_with_future_created_at_SHOULD_return_200_and_no_items(self, api_client):
        response = api_client.get('/inventory/?created_at=2101-10-01')
        assert len(response.json()) == 0
        assert response.status_code == 200

