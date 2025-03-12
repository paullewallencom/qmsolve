import pytest
import util

def test_util_module_exists():
    """Test that the util module is importable."""
    assert "util" in dir()
