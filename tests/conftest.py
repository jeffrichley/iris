"""Pytest configuration and fixtures for Iris test suite."""

import pytest


@pytest.fixture
def sample_fixture():
    """Sample fixture for testing."""
    return "test_data"

