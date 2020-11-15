"""Test APP module"""
import pytest


@pytest.mark.parametrize(('message', 'grandpy'), (
    ('', b'Parles'),
    ('absolument le , la', b'pas bien compris'),
    ('openclassrooms', b'Charente'),
    ('fkrbiufru', b'souviens de rien'),
))
def test_user_input(client, message, grandpy):
    """Test AJAX responses"""
    response = client.post(
        '/show_response',
        data={'message': message}
    )
    assert grandpy in response.data
    assert client.get('/show_response').status_code == 200
