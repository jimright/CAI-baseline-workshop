# Contributing to lab-cai-mlops-banking

## Before You Start

Announce your intentions by commenting on an existing issue or creating a new one. Check the Discussions section for ideas.

## Branch and PR Process

Create a branch from `main` in your forked repository using these naming conventions:

- `feature/` for new features or documentation updates
- `fix/` for non-urgent bug fixes
- `hotfix/` for urgent bug fixes

Submit pull requests against `main` with a reference to your issue.

## Pre-commit Requirements

This project uses pre-commit for linting and validation:

```bash
pip install pre-commit
pre-commit install
pre-commit run -a
```

Run `pre-commit run -a` before submitting changes.

## Commit Signing

All contributions require signed commits following the Developer Certificate of Origin. Add this line to your commit message:

> Signed-off-by: [Your Name] <your.email@example.com>

Use the `-s` flag with `git commit` to automate this:

```bash
git commit -s
```

## Questions or Feedback?

Visit the project's Discussions section on GitHub.
