workflow "Publish Python package" {
  on = "push"
  resolves = ["publish"]
}

action "Install" {
  uses = "abatilo/actions-poetry@3.7.3"
  args = ["install"]
}

action "Run flake8" {
  needs = "Install"
  uses = "abatilo/actions-poetry@3.7.3"
  args = ["run", "python", "setup.py", "flake8"]
}

action "Run tests" {
  needs = "Install"
  uses = "abatilo/actions-poetry@3.7.3"
  args = ["run", "python", "setup.py", "pytest"]
}

action "Master branch" {
  needs = ["Run flake8", "Run tests"]
  uses = "actions/bin/filter@master"
  args = "branch master"
}

action "publish" {
  needs = "Master branch"
  uses = "abatilo/actions-poetry@3.7.3"
  secrets = ["PYPI_USERNAME", "PYPI_PASSWORD"]
  args = ["publish", "--build", "--no-interaction", "-vv", "--username", "$PYPI_USERNAME", "--password", "$PYPI_PASSWORD"]
}
