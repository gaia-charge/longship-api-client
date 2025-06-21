# Tests

This directory contains tests for the longship project.

## Running Tests

### Using Poetry (Recommended)

```bash
# Install dependencies
poetry install

# Run all tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=longship --cov=longship_api_client --cov-report=html

# Run specific test file
poetry run pytest tests/test_types.py

# Run specific test
poetry run pytest tests/test_types.py::TestWebhookPayload::test_charge_point_booted_payload
```

### Using the Test Runner Script

```bash
# Make the script executable
chmod +x run_tests.py

# Run tests
./run_tests.py
```

### Using pytest directly

```bash
# Install pytest if not already installed
pip install pytest pytest-cov

# Run tests
pytest tests/

# Run with coverage
pytest --cov=longship --cov=longship_api_client tests/
```

## Test Structure

- `test_types.py` - Tests for the `longship/types.py` module
  - `TestWebhookPayloadType` - Tests for webhook payload type enums
  - `TestRegistrationStatusType` - Tests for registration status enums
  - `TestDataClasses` - Tests for individual data classes
  - `TestWebhookPayload` - Tests for the main WebhookPayload class
  - `TestEdgeCases` - Tests for edge cases and error handling

## Test Coverage

The tests cover:

1. **Enum functionality** - All webhook payload types and registration status types
2. **Data class creation** - All data classes with various field combinations
3. **Webhook payload processing** - All webhook payload types with proper data conversion
4. **Extra field filtering** - Ensuring extra fields in payloads are ignored
5. **Edge cases** - Special handling like status case conversion
6. **Error handling** - Graceful handling of unexpected data

## Adding New Tests

When adding new functionality to the types module:

1. Add tests for new enums in the appropriate test class
2. Add tests for new data classes in `TestDataClasses`
3. Add tests for new webhook payload types in `TestWebhookPayload`
4. Add edge case tests in `TestEdgeCases` if needed

## Coverage Reports

After running tests with coverage, you can find the HTML coverage report in the `htmlcov/` directory. Open `htmlcov/index.html` in your browser to view the detailed coverage report. 