# Collaboration guide

This guide contains the collaboration guidelines to use
for contributing and maintening this project.

To assure future compatibility and ease of maintenance,
**these are to be observed as strictly as possible**.

## Code Formatting

This project relies on the automatic code formatting
provided by **[Black](https://github.com/psf/black)**.

### DO NOT USE ANY OTHER CODE FORMATTING TOOL UNDER ANY CIRCUMSTANCES

This assures consistency.

### ALWAYS RUN `make format` OVER THE WHOLE PROJECT BEFORE COMMITTING

This assures that no wrong formatting gets committed.
It also assures that the code is compilable.

## Commit Convention

This project follows the **[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)**
guidelines, albeit with more verbosity.

* `file: add <filename>` for adding a new file.
  If the file is a source files (`.cs`), it must be empty or only contain a barebone (empty!) class.
* `file: move <path/to/filename> -> <new/folder>` for moving an existing file.
  No modifications wrt the file contents must be made.
* `file: rename <filename> -> <new filename>` for renaming an existing file.
  No modifications wrt the file contents must be made.
* `file: delete <filename>` for removing an existing file.
  If part of a refactor pass, prefer `refactor: remove <feature>`.
  A short contents line `Reason: <justification for change>` is welcome to add context.
* `feature: implement <feature description>` for implementations of a new feature, class, function.
* `refactor: <change description>` for refactoring changes.
  Refactoring changes MUST BE as atomic as possible, and as complete as feasible.
  Prefer splitting into several commits for clarity if needed.
  A short contents line `Reason: <justification for change>` is welcome to add context.
* `repo: <change description>` for changes affecting the repository.
* `build: <change description>` for changes affecting the build.
  Dependency changes (add/remove/update) go into this category.
  Changes wrt build settings are part of this category as well.
* `merge[pull request #<num>]: branch/name` is the only correct way to merge pull requests.
  **SPECIAL CARE IS REQUIRED** as this format is not the default format that GitHub uses.

## Language convention

**Only grammatically and orthographically correct US English is allowed.**
In case of doubt for wording and spelling, check an online thesaurus and dictionary.

## Line endings

### DO NOT CHANGE LINE ENDINGS

Black restores the correct line endings anyway.

## UTF-8

**UTF-8 NO BOM** is set by Black and must not be altered.
