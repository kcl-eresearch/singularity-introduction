---
permalink: index.html
site: sandpaper::sandpaper_site
---

This lesson provides an introduction to using software containers with the goal of using them to effect reproducible computational environments. Such environments are useful for ensuring reproducible research outputs, for example.

This lesson will introduce both [Docker](https://www.docker.com/) and [Singularity](https://sylabs.io/singularity/) as tools for running containers. Singularity is particularly suited to running containers on infrastructure where users don't have administrative privileges, for example shared infrastructure such as High Performance Computing (HPC) clusters.

::::::::::::::::::::::::::::::::::::::  objectives

## After completing this session you should:

- Have an understanding of what software containers are, why they are useful
  and the common terminology used
- Understand how to use existing containers for common tasks, both by using 
  Docker on your local system and Singularity on an HPC system
- Be able to build your own Docker containers by understanding both the role
  of a `Dockerfile` in building containers, and the syntax used in `Dockerfile`s
- Understand how to manage Docker containers on your local system and how to 
  manage the Singularity cache
- Appreciate issues around reproducibility in software, understand how
  containers can address some of these issues and what the limits to
  reproducibility using containers are

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::  prereq

## Prerequisites

- You should have basic familiarity with using a command shell, and the lesson text will at times request that you "open a shell window", with an assumption that you know what this means.
  - Under Linux or macOS it is assumed that you will access a `bash` shell (usually the default), using your Terminal application.
  - Under Windows, Powershell and Git Bash should allow you to use the Unix instructions. We will also try to give command variants for Windows `cmd.exe`.
- The lessons will sometimes request that you use a text editor to create or edit files in particular directories. It is assumed that you either have an editor that you know how to use that runs within the working directory of your shell window (e.g. `nano`), or that if you use a graphical editor, that you can use it to read and write files into the working directory of your shell.
- You will need access to a local or remote platform with Singularity pre-installed and accessible to you as a user (i.e. no administrator/root access required).
  - If you are attending a taught version of this material, it is expected that the course organisers will provide access to a platform (e.g. an institutional HPC cluster) that you can use for these sections of the material.
- You should be familiar with the basic commands for running jobs on the HPC platform you will be using.
- The platform you will be using should also have MPI installed (required for episode 8).

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## Target audience

This lesson on the use of containers is intended to be relevant to a wide range of
researchers, as well as existing and prospective technical professionals. It is
intended as a beginner level course that is suitable for people who have no
experience of containers.

We are aiming to help people who want to develop their knowledge of container
tooling to help improve reproducibility and support their research work, or
that of individuals or teams they are working with.

<!-- We provide more detail on specific roles that might benefit from this course on
the [Learner Profiles](/profiles.html) page. -->

::::::::::::::::::::::::::::::::::::::::::::::::::
