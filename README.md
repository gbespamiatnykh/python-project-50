# GENDIFF
Compares two configuration files and shows a difference.

### Hexlet tests and linter status:
[![Actions Status](https://github.com/gbespamiatnykh/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/gbespamiatnykh/python-project-50/actions)

### CI and SonarQube status:
[![Python CI](https://github.com/gbespamiatnykh/python-project-50/actions/workflows/build.yml/badge.svg)](https://github.com/gbespamiatnykh/python-project-50/actions/workflows/build.yml)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=gbespamiatnykh_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=gbespamiatnykh_python-project-50)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=gbespamiatnykh_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=gbespamiatnykh_python-project-50)

## Requirements
- Python >= 3.12
- `uv` tool

## Setup
```bash
make install
```
```bash
make build
```
```bash
make package-install
```

## Generate diff
Run Command:
```bash
gendiff
```
<details>
<summary>gendiff .json demo</summary>

[![asciicast](https://asciinema.org/a/BX7WZNQ2VSCGR59QJ5gZoV9bT.svg)](https://asciinema.org/a/BX7WZNQ2VSCGR59QJ5gZoV9bT)
</details>

<details>
<summary>gendiff .yaml demo</summary>

[![asciicast](https://asciinema.org/a/yuiU7rOxwkx9Kqwi477DSL239.svg)](https://asciinema.org/a/yuiU7rOxwkx9Kqwi477DSL239)
</details>

<details>
<summary>gendiff --format stylish demo</summary>

[![asciicast](https://asciinema.org/a/j9Xooy966SSX0Cit8OL9YiD1Y.svg)](https://asciinema.org/a/j9Xooy966SSX0Cit8OL9YiD1Y)
</details>

<details>
<summary>gendiff --format plain demo</summary>

[![asciicast](https://asciinema.org/a/5W6udTbud3x69g2A2bSf5bTgh.svg)](https://asciinema.org/a/5W6udTbud3x69g2A2bSf5bTgh)
</details>

<details>
<summary>gendiff --format json demo</summary>

[![asciicast](https://asciinema.org/a/DYZaFCQrGQfOXMR8hM9J6cZM5.svg)](https://asciinema.org/a/DYZaFCQrGQfOXMR8hM9J6cZM5)
</details>
