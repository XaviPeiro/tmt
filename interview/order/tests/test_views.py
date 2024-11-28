import pytest


class TestViews:
    @pytest.mark.django_db
    def test_deactivate_order_with_PUT_SHOULD_return_405(self, api_client):
        # METHOD NOT ALLOWED
        response = api_client.put('/orders/1/deactivate/')
        assert response.status_code == 405

    @pytest.mark.django_db
    def test_deactivate_order_with_PATCH_SHOULD_return_200and_set_is_active_to_false(self, api_client):
        response = api_client.patch('/orders/1/deactivate/')
        assert response.status_code == 200

        # here retrieve and check is_active

    @pytest.mark.django_db
    def test_deactivate_order_with_non_existing_order_SHOULD_return_404(self, api_client):
        response = api_client.patch('/orders/-1/deactivate/')
        assert response.status_code == 404
