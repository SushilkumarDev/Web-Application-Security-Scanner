# **Contributing to Web Application Security Scanner**

Thank you for your interest in contributing to the Web Application Security Scanner project! Your input is valuable, whether you’re fixing bugs, adding new features, improving documentation, or engaging with the community.

## **Table of Contents**

1. [Getting Started](#getting-started)
2. [How to Report Issues](#how-to-report-issues)
3. [Suggesting New Features](#suggesting-new-features)
4. [Setting Up the Development Environment](#setting-up-the-development-environment)
5. [Contributing Code](#contributing-code)
6. [Style Guide](#style-guide)
7. [Testing](#testing)
8. [Submitting a Pull Request](#submitting-a-pull-request)
9. [Code of Conduct](#code-of-conduct)

---

## **Getting Started**

### Ways to Contribute

There are many ways you can contribute:

- **Report Bugs**: Identify and log issues with clear details.
- **Suggest Features**: Propose enhancements that could make the tool better.
- **Code Contributions**: Implement features, fix bugs, or improve code.
- **Documentation**: Enhance documentation for clarity and usability.

Before you begin, please check the existing issues and documentation to avoid redundant work.

---

## **How to Report Issues**

If you find a bug, please create an issue with the following details:

1. **Describe the Issue**: Include as much information as possible, like:
   - A clear, descriptive title.
   - Steps to reproduce the issue.
   - Expected vs. actual behavior.
   - Error messages, logs, or screenshots (if applicable).
2. **Environment Details**: Specify:
   - Python version and operating system.
   - Version of the Web Application Security Scanner.

Please review the [Issues page](https://github.com/SushilkumarDev/Web-Application-Security-Scanner/issues) to check if your issue has already been reported.

---

## **Suggesting New Features**

Feature requests are welcome! To propose a new feature, please:

1. **Check Existing Requests**: Look through open issues to see if someone else has already suggested the feature.
2. **Create a New Feature Request**: If it’s a new idea, please create a new issue with:
   - **Description**: Describe the problem or use case that motivates the feature.
   - **Solution**: Suggest a potential solution or approach.
   - **Additional Context**: Link references, examples, or tools that could be helpful.

---

## **Setting Up the Development Environment**

To start contributing code, set up your local environment by following these steps:

1. **Fork the Repository**:
   - Create your own fork on GitHub and clone it locally:
     ```bash
     git clone https://github.com/SushilkumarDev/Web-Application-Security-Scanner.git
     cd Web-Application-Security-Scanner
     ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Linux/macOS
   env\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Tests** to ensure everything is working:
   ```bash
   pytest
   ```

---

## **Contributing Code**

### Issue Assignment

- **Express Interest**: If you see an open issue you'd like to work on, comment on it to indicate your interest.
- **Wait for Assignment**: A maintainer will assign the issue to you, so no one duplicates work.

### Branch Naming Convention

Create a branch with a descriptive name:
   - **feature/feature-name** (e.g., `feature/ssl-scanner`)
   - **fix/issue-description** (e.g., `fix/csrf-detection`)

---

## **Style Guide**

- Follow **PEP 8** for Python code.
- Use meaningful variable and function names.
- Comment complex logic and add **docstrings** to all functions and modules.

---

## **Testing**

All new code should include tests where applicable. Use **pytest** for consistency and place tests in the `tests/` directory, following the `test_<module>.py` naming convention.

Run the test suite with:
   ```bash
   pytest
   ```

Ensure all tests pass before submitting a pull request.

---

## **Submitting a Pull Request**

When you’re ready to submit your changes:

1. **Commit Your Changes**: Write clear, concise commit messages.
   ```bash
   git commit -m "Add SSL/TLS vulnerability scanner"
   ```

2. **Push to Your Branch**:
   ```bash
   git push origin feature/your-branch-name
   ```

3. **Open a Pull Request**:
   - Navigate to the original repository and select **New Pull Request**.
   - Complete the PR template, linking to relevant issues and providing a summary of your changes.
   - Ensure all CI checks pass and be responsive to review feedback.

---

## **Code of Conduct**

By participating in this project, you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md) to foster a positive and inclusive community for all contributors.

---

Thank you for helping make the Web Application Security Scanner a better tool for everyone!
