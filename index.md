---
permalink: index.html
site: sandpaper::sandpaper_site
---

This lesson provides an introduction to using the [Singularity container platform](https://github.com/hpcng/singularity). Singularity is particularly suited to running containers on infrastructure where users don't have administrative privileges, for example shared infrastructure such as High Performance Computing (HPC) clusters.

This lesson will introduce Singularity from scratch showing you how to run a simple container and building up to creating your own containers and running parallel scientific workloads on HPC infrastructure.

::::::::::::::::::::::::::::::::::::::::::  prereq

## Prerequisites

There are two core elements to this lesson - *running containers* and *building containers*. The prerequisites are slightly different for each and are explained below.

**Running containers:** (episodes 1-5 and 8)

- Access to a local or remote platform with Singularity pre-installed and accessible to you as a user (i.e. no administrator/root access required).
  - If you are attending a taught version of this material, it is expected that the course organisers will provide access to a platform (e.g. an institutional HPC cluster) that you can use for these sections of the material.
- The platform you will be using should also have MPI installed (required for episode 8).

**Building containers:** (episodes 6 and 7)
Building containers requires access to a platform with an installation of Singularity on which you also have administrative access. If you run Linux and are comfortable with following the [Singularity installation instructions](https://sylabs.io/guides/3.5/admin-guide/installation.html), then installing Singularity directly on your system is an option. However, we strongly recommend using the [Docker Singularity container](https://quay.io/repository/singularity/singularity?tab=tags) for this section of the material. Details are provided on how to use the container in the relevant section of the lesson material. To support building containers, the prerequisite is therefore:

- Access to a system with Docker installed on which you can run the Docker Singularity  container.
  
  OR

- Access to a local or remote Linux-based system on which you have administrator (root) access and can install the Singularity software.

**Please note that the version of Singularity used in this part of the course is *version 3.5.3* which was the latest stable release at the time of writing.** If you are installing Singularity on your own system for use in the course, you are recommneded to install version 3.5.3.


::::::::::::::::::::::::::::::::::::::::::::::::::
