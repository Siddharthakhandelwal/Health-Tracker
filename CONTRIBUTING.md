# 🤝 Contributing to Health Tracker

Thank you for your interest in contributing to the Health Tracker project! This guide will help you get started with contributing to our AI-powered health tracking API.

## 📋 Table of Contents

1. [Code of Conduct](#-code-of-conduct)
2. [Getting Started](#-getting-started)
3. [Development Setup](#-development-setup)
4. [How to Contribute](#-how-to-contribute)
5. [Code Style Guidelines](#-code-style-guidelines)
6. [Testing Requirements](#-testing-requirements)
7. [Pull Request Process](#-pull-request-process)
8. [Issue Reporting Guidelines](#-issue-reporting-guidelines)
9. [Documentation Guidelines](#-documentation-guidelines)
10. [Community and Support](#-community-and-support)

## 📜 Code of Conduct

### Our Pledge

We are committed to making participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

**Positive behavior includes:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable behavior includes:**
- The use of sexualized language or imagery
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information without explicit permission
- Other conduct which could reasonably be considered inappropriate in a professional setting

## 🚀 Getting Started

### Prerequisites

Before contributing, ensure you have:

- **Python 3.9 or higher** installed
- **Git** for version control
- **Google Gemini API key** for testing
- **Basic understanding** of FastAPI and REST APIs
- **Text editor or IDE** (VS Code, PyCharm recommended)

### First-Time Contributors

If you're new to open source:

1. **Read the documentation**: Start with [`README.md`](README.md) and [`SETUP_GUIDE.md`](SETUP_GUIDE.md)
2. **Look for "good first issue" labels**: These are beginner-friendly issues
3. **Join our community**: Introduce yourself in discussions
4. **Ask questions**: Don't hesitate to ask for help or clarification

## 🛠️ Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/Health-Tracker.git
cd Health-Tracker

# Add the original repository as upstream
git remote add upstream https://github.com/ORIGINAL_OWNER/Health-Tracker.git
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv health-tracker-dev
source health-tracker-dev/bin/activate  # On Windows: health-tracker-dev\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8 mypy pre-commit
```

### 3. Configure Environment

```bash
# Copy environment template
cp env.example .env

# Edit .env with your API keys
# GEMINI_API_KEY=your_api_key_here
```

### 4. Verify Setup

```bash
# Run the application
python main.py

# In another terminal, run tests
python test_api.py
```

## 🎯 How to Contribute

### Types of Contributions

We welcome various types of contributions:

1. **🐛 Bug Reports**: Help us identify and fix issues
2. **✨ Feature Requests**: Suggest new functionality
3. **📝 Documentation**: Improve or add documentation
4. **🧪 Tests**: Add or improve test coverage
5. **🔧 Code**: Fix bugs or implement features
6. **🎨 UI/UX**: Improve user experience
7. **🌐 Translations**: Help make the project accessible globally

### Contribution Workflow

1. **Check existing issues**: Look for existing issues or discussions
2. **Create an issue**: If none exists, create one describing your contribution
3. **Get assignment**: Wait for maintainer approval before starting work
4. **Create branch**: Create a feature branch from `main`
5. **Make changes**: Implement your changes following our guidelines
6. **Test thoroughly**: Ensure all tests pass and add new tests if needed
7. **Submit PR**: Create a pull request with clear description
8. **Address feedback**: Respond to review comments promptly
9. **Merge**: Once approved, your changes will be merged

## 📏 Code Style Guidelines

### Python Code Standards

We follow **PEP 8** with some project-specific conventions:

#### Formatting
```python
# Use Black for automatic formatting
black main.py

# Line length: 88 characters (Black default)
# Indentation: 4 spaces (no tabs)
# String quotes: Double quotes preferred
```

#### Naming Conventions
```python
# Variables and functions: snake_case
user_data = get_user_info()

# Classes: PascalCase
class HealthTracker:
    pass

# Constants: UPPER_SNAKE_CASE
MAX_WATER_INTAKE = 10.0

# Private methods: _leading_underscore
def _internal_method(self):
    pass
```

#### Type Hints
```python
# Always use type hints for function parameters and return values
def build_prompt(data: dict, endpoint: str) -> str:
    return f"Prompt for {endpoint}: {data}"

# Use Optional for nullable values
from typing import Optional
def process_data(value: Optional[str] = None) -> dict:
    pass
```

#### Documentation
```python
def send_to_gemini(data: dict, endpoint: str) -> str:
    """
    Send health data to Gemini AI for analysis.
    
    Args:
        data: Dictionary containing health tracking data
        endpoint: The health category ('water', 'gym', 'food')
        
    Returns:
        AI-generated health advice string (≤25 words)
        
    Raises:
        EnvironmentError: If GEMINI_API_KEY is not set
        Exception: If AI service is unavailable
    """
    pass
```

### FastAPI Specific Guidelines

#### Endpoint Structure
```python
@app.post("/water")
async def water_endpoint(request: Request) -> JSONResponse:
    """Water intake tracking endpoint."""
    return await handle_request(request, "water")
```

#### Error Handling
```python
try:
    # API logic here
    pass
except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))
except Exception as e:
    raise HTTPException(status_code=500, detail="Internal server error")
```

### File Organization

```
health-tracker/
├── main.py              # Main FastAPI application
├── models/              # Pydantic models (future)
├── services/            # Business logic services (future)
├── tests/               # Test files
├── docs/                # Documentation files
└── scripts/             # Utility scripts
```

## 🧪 Testing Requirements

### Test Coverage

- **Minimum coverage**: 80% for new code
- **Critical paths**: 100% coverage for core functionality
- **Integration tests**: All endpoints must have integration tests

### Running Tests

```bash
# Run existing tests
python test_api.py

# Run with pytest (recommended for new tests)
pytest tests/ -v

# Run with coverage
pytest --cov=main tests/

# Run specific test
pytest tests/test_water_endpoint.py::test_valid_water_data
```

### Writing Tests

#### Unit Tests
```python
import pytest
from main import build_prompt

def test_build_prompt_water():
    """Test water prompt generation."""
    data = {"amount_liters": 2.0}
    prompt = build_prompt(data, "water")
    
    assert "water intake" in prompt.lower()
    assert "2.0" in prompt
    assert len(prompt) > 0
```

#### Integration Tests
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_water_endpoint_success():
    """Test successful water endpoint response."""
    response = client.post("/water", json={"amount_liters": 2.0})
    
    assert response.status_code == 200
    assert "message" in response.json()
    assert len(response.json()["message"]) > 0
```

### Test Data

```python
# Use consistent test data
VALID_WATER_DATA = {"amount_liters": 2.0, "time": "2024-06-01T10:00:00"}
VALID_GYM_DATA = {"activity": "running", "duration_minutes": 30}
VALID_FOOD_DATA = {"meal": "breakfast", "food": "oatmeal with berries"}

INVALID_WATER_DATA = {"amount_liters": -1}  # Negative value
INVALID_GYM_DATA = {"activity": ""}         # Empty activity
INVALID_FOOD_DATA = {}                      # Missing required field
```

## 📥 Pull Request Process

### Before Submitting

1. **Update your branch**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run all checks**:
   ```bash
   # Format code
   black .
   
   # Check linting
   flake8 .
   
   # Type checking
   mypy main.py
   
   # Run tests
   pytest
   ```

3. **Update documentation**: Ensure all changes are documented

### PR Title and Description

#### Title Format
```
<type>(<scope>): <description>

Examples:
feat(api): add user authentication endpoint
fix(water): handle negative water intake values
docs(readme): update installation instructions
test(gym): add integration tests for gym endpoint
```

#### Description Template
```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Test improvement

## Testing
- [ ] All existing tests pass
- [ ] New tests added for new functionality
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings or errors introduced
```

### Review Process

1. **Automated checks**: All CI checks must pass
2. **Code review**: At least one maintainer review required
3. **Testing**: Reviewer will test functionality
4. **Documentation**: Ensure documentation is updated
5. **Approval**: Maintainer approval required for merge

## 🐛 Issue Reporting Guidelines

### Before Creating an Issue

1. **Search existing issues**: Check if the issue already exists
2. **Check documentation**: Ensure it's not a usage question
3. **Test with latest version**: Verify the issue exists in the current version

### Bug Report Template

```markdown
**Bug Description**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Send POST request to '/water'
2. With data: `{"amount_liters": -1}`
3. Observe error response

**Expected Behavior**
A clear description of what you expected to happen.

**Actual Behavior**
What actually happened instead.

**Environment**
- OS: [e.g., Windows 10, macOS 12.0, Ubuntu 20.04]
- Python Version: [e.g., 3.9.7]
- FastAPI Version: [e.g., 0.115.14]
- Browser: [if applicable]

**Additional Context**
Add any other context about the problem here.

**Logs**
```
Paste relevant logs here
```
```

### Feature Request Template

```markdown
**Feature Description**
A clear and concise description of the feature you'd like to see.

**Problem Statement**
What problem does this feature solve?

**Proposed Solution**
Describe your preferred solution.

**Alternative Solutions**
Describe any alternative solutions you've considered.

**Use Cases**
Provide specific use cases for this feature.

**Additional Context**
Add any other context or screenshots about the feature request.
```

## 📚 Documentation Guidelines

### Documentation Types

1. **Code Documentation**: Docstrings and inline comments
2. **API Documentation**: Endpoint descriptions and examples
3. **User Documentation**: Setup guides and tutorials
4. **Developer Documentation**: Architecture and contribution guides

### Writing Style

- **Tone**: Friendly, professional, and beginner-friendly
- **Structure**: Use clear headings and bullet points
- **Examples**: Include practical, working examples
- **Emojis**: Use consistently for visual appeal (following existing pattern)
- **Links**: Use relative links for internal documentation

### Documentation Standards

#### Markdown Files
```markdown
# 📋 Document Title

Brief description of the document's purpose.

## 🎯 Section Title

Content with clear explanations and examples.

### Subsection

More detailed information.

#### Code Examples
```python
# Always include working code examples
def example_function():
    return "Hello, World!"
```
```

#### API Documentation
```markdown
### POST /endpoint

**Purpose**: Brief description of what this endpoint does.

**Request Format**:
```json
{
  "field": "value",
  "optional_field": "optional_value"
}
```

**Response Format**:
```json
{
  "message": "AI-generated response"
}
```

**Example**:
```bash
curl -X POST "http://localhost:8000/endpoint" \
     -H "Content-Type: application/json" \
     -d '{"field": "value"}'
```
```

## 🌟 Community and Support

### Getting Help

1. **Documentation**: Check existing documentation first
2. **Issues**: Search existing issues for similar problems
3. **Discussions**: Use GitHub Discussions for questions
4. **Community**: Join our community channels

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and community discussion
- **Pull Requests**: Code review and collaboration

### Recognition

We appreciate all contributions! Contributors will be:

- **Listed in CHANGELOG.md**: For significant contributions
- **Mentioned in release notes**: For major features or fixes
- **Added to contributors list**: All contributors are recognized

### Maintainer Responsibilities

Maintainers will:

- **Respond promptly**: Aim to respond to issues/PRs within 48 hours
- **Provide clear feedback**: Give constructive and actionable feedback
- **Maintain quality**: Ensure code quality and consistency
- **Foster community**: Create a welcoming environment for all contributors

## 🎉 Thank You!

Thank you for contributing to Health Tracker! Your contributions help make health tracking more accessible and effective for everyone.

### Quick Links

- [Setup Guide](SETUP_GUIDE.md)
- [API Documentation](API_GUIDE.md)
- [Architecture Overview](ARCHITECTURE.md)
- [Examples](EXAMPLES.md)
- [Deployment Guide](DEPLOYMENT.md)

---

**Happy Contributing! 🚀**

*For questions about contributing, please create an issue or start a discussion. We're here to help!*