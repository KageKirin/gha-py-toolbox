# GitHub Actions Python Toolbox (`gha-py-toolbox`)

This repo contains a collection of actively used GitHub Actions
implemented in Python :snake:.

This collection came alive due to the following facts:

* GitHub Actions can be invoked from any other action or workflow,
  given their canonical path,
  and don't need to be published on the GitHub Actions Marketplace.

* GitHub Actions can be scriped in Python, whiches do not need to depend
  on a specific OS.
  The actions are thus cross-platform (or at least intended to be).

* Python is much clearer language to write scripts, compared to Bash,
  PowerShell or DOS. The overhead to calling native programs is minimal,
  and the usual need to rely on external tools such as ripgrep, fd-find, etc
  is easily gapped by the language itself, or its many libraries.

## ⚡ Getting Started

The actions contained inside this repo are grouped by their respective purpose:

* `gh`: actions pertaining to GitHub services (pull requests, workflows, ...)
* `git`: actions pertaining to git (via libgit2 when possible)
* `npm`: actions pertaining to the NodeJS Package Manager
* `dotnet`: actions pertaining to C#/.NET projects (build, pack, publish, ...)
* `install`: actions pertaining to package-based installers (apt-get, snap, brew, ...)
* `util`: actions pertaining to miscellanous generic utility functions

We differentiate between **actions** which are atomic tasks,
and **macros** which are composite tasks referencing several actions.

* **Actions** are stored in `actions`.
* **Macros** are stored in `macros`.

## 🔧 Referencing an action

The `uses` property of a `step` allows to directly reference an action in any GitHub repository.

```yaml
jobs:
  a-job:
    steps:
    - name: Referencing an action directly
      uses: <repo-owner>/<repo-name>/<path-to-action>@<branch>
```

For the gha-py-toolbox actions, this would look as follows:

```yaml
jobs:
  a-job:
    steps:
    - name: Greet the world
      uses: kagekirin/gha-py-toolbox/actions/gh/hello@main
```

* `kagekirin/gha-py-toolbox` is this repo, of which I am the owner.
* `actions/gh/hello` references the action itself.
* `main` is the principal branch of this repo, and thus the only branch that is assured not be removed on a whim.

### 🔨 Build the Project

### ▶ Running and Settings

## 🤝 Collaborate with My Project

Accepting bugfixes and ideas for improvement.
Please refer to the [Collaboration Guidelines](./COLLABORATION.md).
