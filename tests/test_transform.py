import pytest
from src.data_transformation.transform import transform_data

def test_handle_exception():
    data = None
    with pytest.raises(TypeError):
        transform_data(data)

def test_handle_invalid_input():
    data = 'invalid'
    with pytest.raises(TypeError):
        transform_data(data)

def test_handle_empty_list():
    data = []
    result = transform_data(data)
    assert result == data