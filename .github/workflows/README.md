# GitHub Actions Workflows

This directory contains GitHub Actions workflows for automated testing and CI/CD.

## Available Workflow

### `test.yml` - Default Test Suite

**Triggers:**
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

**Features:**
- Tests against Python 3.8, 3.9, 3.10, and 3.11
- Uses Poetry for dependency management
- Runs pytest with coverage reporting (terminal output only)
- No external service dependencies

**Steps:**
1. Checkout code
2. Set up Python environment
3. Install Poetry
4. Cache virtual environment for faster builds
5. Install dependencies with `poetry install --with dev`
6. Run tests with coverage: `poetry run pytest --cov=longship --cov=longship_api_client --cov-report=term-missing`
7. Run tests with verbose output: `poetry run pytest -v`

## Usage

This workflow will automatically run when you:
- Push to `main` or `develop` branches
- Create pull requests to `main` or `develop` branches

## Configuration

### Poetry Configuration
The workflow uses Poetry with the following settings:
- Virtual environments created in project directory (`.venv`)
- Development dependencies installed with `--with dev`
- Caching enabled for faster builds

### Python Versions
Currently testing against:
- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11

### Coverage Configuration
Coverage is configured to track:
- `longship` package
- `longship_api_client` package

## Local Testing

To run the same tests locally:

```bash
# Install dependencies
poetry install --with dev

# Run tests with coverage
poetry run pytest --cov=longship --cov=longship_api_client --cov-report=term-missing

# Run tests with verbose output
poetry run pytest -v
```

## Troubleshooting

### Common Issues

1. **Poetry not found**: Make sure you're using the latest version of the `snok/install-poetry@v1` action
2. **Cache misses**: The cache key is based on the poetry.lock file hash, so changes to dependencies will invalidate the cache

### Customization

You can customize the workflow by:
- Adding more Python versions to the matrix
- Changing the trigger branches
- Adding additional test commands
- Modifying the coverage configuration
- Adding linting or other quality checks 