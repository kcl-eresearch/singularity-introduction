---
title: 'Reference'
---

# Reference

## Common Docker commands

**To download a container image:**

```bash
docker image pull hello-world
```

**To run a container:**

If you have not yet downloaded the `hello-world` container image, this command will also download it.

```bash
docker container run hello-world
```

**To run a shell inside a container:**

This depends on how the container is set up.
For some containers, you can access a shell directly:

```bash
$ docker container run -it alpine sh
```

For other containers you will need to override the default entrypoint:
```bash
$ docker container run -it --entrypoint sh my-container
```

**To run a specific command using a container:**

As above, this depends on how the container is set up.
For some containers, you can run a command directly:
```bash
docker container run alpine cat /etc/os-release
```

For others, you will need to override the default entrypoint:
```bash
$ docker container run -it --entrypoint /bin/date hello-world
```

## Common Singularity commands

**To download a container image:**

```bash
$ singularity pull hello-world.sif shub://vsoch/hello-world
```

**To run a container:**

```bash
$ singularity run hello-world.sif
```

**To run a shell inside a container:**

```bash
$ singularity shell hello-world.sif
```

**To run a specific command using a container:**

```bash
$ singularity exec hello-world.sif /bin/echo Hello World!
```
