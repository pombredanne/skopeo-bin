# Python wrapper for Skopeo binary

This is a Python wrapper for [Skopeo](https://github.com/containers/skopeo). Using `skopeo-bin` you can install Skopeo using Pipenv or Pip, instead of manually downloading, unzipping and building it.

## Usage

```sh
pipenv install skopeo-bin

skopeo --version
```

## Build wheel

Works only on Mac/Linux for distributing since we need to set the execution rights of the binaries properly. Windows doesnt allow this.

```sh
build-wheel.sh
```

## Updating Skopeo binaries

For building the MacOS binary follow the instructions [here](https://github.com/containers/skopeo#building-without-a-container) and for Linux follow the pure-GO static binary instructions [here](https://github.com/containers/skopeo#building-in-a-container).

## License

This project is [Apache License Version 2.0](LICENSE).
