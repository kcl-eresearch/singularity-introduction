---
title: 'Singularity: Getting started'
start: yes
teaching: 30
exercises: 20
---

::::::::::::::::::::::::::::::::::::::: objectives

- Understand what Singularity is and when you might want to use it.
- Undertake your first run of a simple Singularity container.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- What is Singularity and why might I want to use it?

::::::::::::::::::::::::::::::::::::::::::::::::::


## What is Singularity?

So far in this lesson we have been using Docker to run containers.
However, the design of Docker presents potential security issues for shared computing platforms with multiple users, such as lab desktops, research clusters or HPC platforms.
Therefore, system administrators will generally not install Docker on such shared platforms. 
Singularity, on the other hand, can be run by end-users entirely within "user space", that is, no special administrative privileges need to be assigned to a user in order for them to run and interact with containers on a platform where Singularity has been installed.


:::::::::::::::::::::::::::::::::::::::::  callout

## What is the relationship between Singularity, SingularityCE and Apptainer?

Singularity is open source and was initially developed within the research community.
The company [Sylabs](https://sylabs.io/) was founded in 2018 to provide commercial support for Singularity.
In [May 2021](https://sylabs.io/2021/05/singularity-community-edition/), Sylabs "forked" the codebase to create a new project called [SingularityCE]((https://sylabs.io/singularity)) (where CE means "Community Edition").
This in effect marks a common point from which two projects---SingularityCE and Singularity---developed.
Sylabs continue to develop both the free, open source SingularityCE and a Pro/Enterprise edition of the software.
In November 2021, the original open source Singularity project [renamed itself to Apptainer](https://apptainer.org/news/community-announcement-20211130/) and [joined the Linux Foundation](https://www.linuxfoundation.org/press/press-release/new-linux-foundation-project-accelerates-collaboration-on-container-systems-between-enterprise-and-high-performance-computing-environments).

At the time of writing, in the context of the material covered in this lesson, Apptainer and Singularity are effectively interchangeable.
If you are working on a platform that now has Apptainer installed, you might find that the only change you need to make when working through this material is to use the the command `apptainer` instead of `singularity`.
This course will continue to refer to Singularity until differences between the projects warrant choosing one project or the other for the course material.
:::::::::::::::::::::::::::::::::::::::::


## Getting started with Singularity

Initially developed within the research community, Singularity is open source and the [repository](https://github.com/hpcng/singularity) is currently available in the "[The Next Generation of High Performance Computing](https://github.com/hpcng)" GitHub organisation.
This Singularity material is intended to be used on a remote platform where Singularity has been pre-installed.

*If you're attending a taught version of this course, you will be provided with access details for a remote platform made available to you. This platform will have the Singularity software pre-installed.*

Sign in to the remote platform, with Singularity installed, that you've been provided with access to. Check that the `singularity` command is available in your terminal:

:::::::::::::::::::::::::::::::::::::::::  callout

## Loading a module

HPC systems often use *modules* to provide access to software on the system so you may need to use the command:

```bash
$ module load singularity
```

before you can use the `singularity` command on the system.


::::::::::::::::::::::::::::::::::::::::::::::::::

```bash
$ singularity --version
```

```output
singularity-ce version 4.1.2-jammy
```

Depending on the version of Singularity installed on your system, you may see a different version. At the time of writing, `v4.2.2` is the latest release of Singularity CE and `v1.3.6` is the latest version of Apptainer.

## Getting an image and running a Singularity container

If you recall from learning about Docker, Docker images are formed of a set of *layers* that make up the complete image. When you pull a Docker image from Docker Hub, you see the different layers being downloaded to your system. They are stored in your local Docker repository on your system and you can see details of the available images using the `docker` command.

Singularity images are a little different. Singularity uses the [Singularity Image Format (SIF)](https://github.com/sylabs/sif) and images are provided as single `SIF` files (with a `.sif` filename extension). Singularity images can be pulled from [Singularity Hub](https://singularity-hub.org/), a registry for container images. Singularity is also capable of running containers based on images pulled from [Docker Hub](https://hub.docker.com/) and some other sources. We'll look at accessing containers from Docker Hub later in the Singularity material.

:::::::::::::::::::::::::::::::::::::::::  callout

## Singularity Hub

Note that in addition to providing a repository that you can pull images from, [Singularity Hub](https://singularity-hub.org/) can also build Singularity images for you from a ***recipe*** - a configuration file defining the steps to build an image. We'll look at recipes and building images later.


::::::::::::::::::::::::::::::::::::::::::::::::::

Let's begin by creating a `test` directory, changing into it and *pulling* a test *Hello World* image from Singularity Hub:

```bash
$ mkdir test
$ cd test
$ singularity pull hello-world.sif shub://vsoch/hello-world
```

```output
INFO:    Downloading shub image
 59.75 MiB / 59.75 MiB [===============================================================================================================] 100.00% 52.03 MiB/s 1s
```

What just happened?! We pulled a SIF image from Singularity Hub using the `singularity pull` command and directed it to store the image file using the name `hello-world.sif` in the current directory. If you run the `ls` command, you should see that the `hello-world.sif` file is now present in the current directory. This is our image and we can now run a container based on this image:

```bash
$ singularity run hello-world.sif
```

```output
RaawwWWWWWRRRR!! Avocado!
```

The above command ran the *hello-world* container from the image we downloaded from Singularity Hub and the resulting output was shown.

How did the container determine what to do when we ran it?! What did running the container actually do to result in the displayed output?

When you run a container from a Singularity image without using any additional command line arguments, the container runs the default run script that is embedded within the image. This is a shell script that can be used to run commands, tools or applications stored within the image on container startup. We can inspect the image's run script using the `singularity inspect` command:

```bash
$ singularity inspect -r hello-world.sif
```

```output
#!/bin/sh 

exec /bin/bash /rawr.sh

```

This shows us the script within the `hello-world.sif` image configured to run by default when we use the `singularity run` command.

That concludes this introductory Singularity episode. The next episode looks in more detail at running containers.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Singularity is another container platform and it is often used in cluster/HPC/research environments.
- Singularity has a different security model to other container platforms, one of the key reasons that it is well suited to HPC and cluster environments.
- Singularity has its own container image format (SIF).
- The `singularity` command can be used to pull images from Singularity Hub and run a container from an image file.

::::::::::::::::::::::::::::::::::::::::::::::::::
