# Singularity container with GPU-configured Pytorch for climate and weather applications

## Description
An example showing how to use a Singularity container with GPU-configured Pytorch and a bunch of additional python packages that are useful for climate and weather applications.

## Installation

Follow the instructions [here](https://singularity-tutorial.github.io/) to install Singlarity and to find further tutorials.


## How to use

Build a container from the ``stack.def`` definition file:

```
sudo singularity build --force stack.sif stack.def
```

Or download the ``stack.sif`` image file from Cloud Library with:
```
singularity pull --arch amd64 library://phess/pytorch-stack/stack:latest
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

## Notes

### CUDA version
Check that the CUDA verion in the Docker image is compatible with the hardware. If not, change the CUDA version in the stack.def file.

### File systems
Some file system paths might not be visible for the container on the host system, e.g. such as ``/p/tmp/``.
These can be added with the ``--bind`` flag:

```
singularity exec --nv --bind /p/tmp/ ./stack.sif python test.py
```

### Push and pull 

Follow the instructions [here](https://sylabs.io/guides/3.5/user-guide/cloud_library.html) to register and to create an access token. Then push the image with
```
singularity push stack.sif library://<your name>/<container name>:version
```
Typically ``version`` is named ``latest``. To pull a container from the cloud use:

```
singularity pull stack.sif library://<your name>/<container name>:version
```

