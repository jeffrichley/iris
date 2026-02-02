"""Placeholder test to ensure pytest runs successfully."""

import pytest


@pytest.mark.unit
def test_placeholder_passes() -> None:
    """Placeholder test that always passes.

    This test exists to ensure the CI pipeline runs successfully
    even before actual implementation code exists.
    """
    assert True


@pytest.mark.unit
def test_project_structure_exists() -> None:
    """Verify that project structure is set up correctly."""
    from pathlib import Path

    # Verify src/iris directory exists
    src_dir = Path(__file__).parent.parent / "src"
    iris_dir = src_dir / "iris"
    assert src_dir.exists()
    assert iris_dir.exists()
    assert (iris_dir / "__init__.py").exists()

    # Verify tests directory exists
    tests_dir = Path(__file__).parent
    assert tests_dir.exists()
    assert (tests_dir / "__init__.py").exists()


@pytest.mark.unit
def test_version_exists() -> None:
    """Test that the version is accessible from the package."""
    import iris

    assert hasattr(iris, "__version__")
    assert iris.__version__ == "0.1.0"
