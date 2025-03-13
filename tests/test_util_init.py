import pytest
pytest.skip("Placeholder test—not yet implemented.", allow_module_level=True)


def test_util_module_exists():
    """Test that the util module is importable."""
    assert "util" in dir()
