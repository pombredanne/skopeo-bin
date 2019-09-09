# Python wrapper for Skopeo binary

This is a Python wrapper for [Skopeo](https://github.com/containers/skopeo). Using `skopeo-bin` you can install Skopeo using Pipenv or Pip, instead of manually downloading, unzipping and building it.

## Usage

```sh
pipenv install --dev skopeo-bin

skopeo --version
```

## Build wheel

Windows:

```sh
build-wheel.bat
```

Linux/Mac:

```sh
build-wheel.sh
```

## License

This project is [Apache License Version 2.0](LICENSE).
