# Build a Singularity container with GPU-configured Pytorch

## Description
An example showing how to build a Singularity container with GPU-configured Pytorch and a bunch of additional python packages.

## Installation

Follow the instructions [here](https://singularity-tutorial.github.io/) to install Singlarity and further tutorials.

## How to use

Build a container:

```
sudo singularity build --force stack.sif stack.def
```

Execute test.py script with using the container with Nvidia drivers enabled:

```
singularity exec --nv ./stack.sif python test.py
```

Start jupyterlab:

```
singularity exec --nv ./stack.sif jupyter lab
```

## Customize

Just add/remove packages in the stack.def file.

