import pytest
from src.data_transformation.transform import transform_data

def test_transform_data_success():
    data = [1, 2, 3]
    result = transform_data(data)
    assert result == data

def test_transform_data_empty():
    data = []
    result = transform_data(data)
    assert result == data

def test_transform_data_failure():
    data = None
    with pytest.raises(TypeError):
        transform_data(data)