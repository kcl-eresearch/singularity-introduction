---
title: Introducing Containers
teaching: 20
exercises: 5
---

::::::::::::::::::::::::::::::::::::::: objectives

- Show how software depending on other software leads to configuration management problems.
- Identify the problems that software installation can pose for research.
- Explain the advantages of containerization.
- Explain how using containers can solve software configuration problems

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- What are containers, and why might they be useful to me?

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## Work in progress...

This lesson is new material that is under ongoing development.
As the tools and best practices continue to develop, elements of this material are likely to evolve.
We welcome any comments or suggestions on how the material can be improved or extended.


::::::::::::::::::::::::::::::::::::::::::::::::::


:::::::::::::::::::::::::::::::::::::::::  callout

## Learning about Docker Containers

The Australian Research Data Commons has produced a short introductory video
about Docker containers that covers many of the points below. Watch it before
or after you go through this section to reinforce your understanding!

[How can software containers help your research?](https://www.youtube.com/watch?v=HelrQnm3v4g)

Australian Research Data Commons, 2021. *How can software containers help your research?*. [video] Available at: [https://www.youtube.com/watch?v=HelrQnm3v4g](https://www.youtube.com/watch?v=HelrQnm3v4g) DOI: [http://doi.org/10.5281/zenodo.5091260](https://doi.org/10.5281/zenodo.5091260)


::::::::::::::::::::::::::::::::::::::::::::::::::

## Scientific Software Challenges

:::::::::::::::::::::::::::::::::::::::  challenge

## What's Your Experience?

Take a minute to think about challenges that you have experienced in using
scientific software (or software in general!) for your research. Then,
share with your neighbors and try to come up with a list of common gripes or
challenges.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## What is a software *dependency*?

We will mention software *dependencies* a lot in this section of the workshop
so it is good to clarify this term up front. A software dependency is a
relationship between software components where one component relies on the
other to work properly. For example, if a software application uses a library
to query a database, the application depends on that library.

::::::::::::::::::::::::::::::::::::::::::::::::::

You may have come up with some of the following:

- you want to use software that doesn't exist for the operating system (Mac, Windows, Linux) you'd prefer.
- you struggle with installing a software tool because you have to install a number of other dependencies first. Those dependencies, in turn, require *other* things, and so on (i.e. combinatoric explosion).
- the software you're setting up involves many dependencies and only a subset of all possible versions of those dependencies actually works as desired.
- you're not actually sure what version of the software you're using because the install process was so circuitous.
- you and a colleague are using the same software but get different results because you have installed different versions and/or are using different operating systems.
- you installed everything correctly on your computer but now need to install it on a colleague's computer/campus computing cluster/etc.
- you've written a package for other people to use but a lot of your users frequently have trouble with installation.
- you need to reproduce a research project from a former colleague and the software used was on a system you no longer have access to.

A lot of these characteristics boil down to one fact: the main program you want
to use likely depends on many, many, different other programs (including the
operating system!), creating a very complex, and often fragile system. One change
or missing piece may stop the whole thing from working or break something that was
already running. It's no surprise that this situation is sometimes
informally termed **dependency hell**.



:::::::::::::::::::::::::::::::::::::::  challenge

## Software and Science

Again, take a minute to think about how the software challenges we've discussed
could impact (or have impacted!) the quality of your work.
Share your thoughts with your neighbors. What can go wrong if our software
doesn't work?


::::::::::::::::::::::::::::::::::::::::::::::::::

Unsurprisingly, software installation and configuration challenges can have
negative consequences for research:

- you can't use a specific tool at all, because it's not available or installable.
- you can't reproduce your results because you're not sure what tools you're actually using.
- you can't access extra/newer resources because you're not able to replicate your software set up.
- others cannot validate and/or build upon your work because they cannot recreate your system's unique configuration.

Thankfully there are ways to get underneath (a lot of) this mess: containers
to the rescue! Containers provide a way to package up software dependencies
and access to resources such as files and communications networks in a uniform manner.

## What is a Container?

Imagine you want to install some research software but don't want to take the chance of making a mess of your existing system by installing a bunch of additional stuff (libraries/dependencies/etc.).
You don't want to buy a whole new computer because it's too expensive.
What if, instead, you could have another independent filesystem and running operating system that you could access from your main computer, and that is actually stored within this existing computer?

More concretely, Docker Inc use the following definition of a container:

> A container is a standard unit of software that packages up code and all its dependencies so the application runs reliably from one computing environment to another.

<https://www.docker.com/resources/what-container/>

The term container can be usefully considered with reference to shipping containers.
Before shipping containers were developed, packing and unpacking cargo ships was time consuming and error prone, with high potential for different clients' goods to become mixed up. 
Just like shipping containers keep things together that should stay together, software containers standardize the description and creation of a complete software system: you can drop a container into any computer with the container software installed (the 'container host'), and it should *just work*.

:::::::::::::::::::::::::::::::::::::::::  callout

## Virtualization

Containers are an example of what's called **virtualization** -- having a
second virtual computer running and accessible from a main or **host**
computer. Another example of virtualization are **virtual machines** or
VMs. A virtual machine typically contains a whole copy of an operating system in
addition to its own filesystem and has to get booted up in the same way
a computer would.
A container is considered a lightweight version of a virtual machine;
underneath, the container is (usually) using the Linux kernel and simply has some
flavour of Linux + the filesystem inside.


::::::::::::::::::::::::::::::::::::::::::::::::::


## What are Docker and Singularity?

[Docker](https://www.docker.com/) and [Singularity](https://sylabs.io/singularity/) are tools that allow you to build and run containers.
They are similar in many ways.
However, differences in the design of Singularity and Docker mean that Singularity is particularly well-suited to running on distributed, High Performance Computing (HPC) infrastructure.
System administrators will not, generally, install Docker on shared computing platforms such as lab desktops, research clusters or HPC platforms because the design of Docker presents potential security issues for shared platforms with multiple users.
Singularity, on the other hand, can be run by end-users entirely within "user space", that is, no special administrative privileges need to be assigned to a user in order for them to run and interact with containers on a platform where Singularity has been installed.

However, Singularity is more complicated to install on Windows and Mac laptops/desktops.
Therefore, in this workshop, we will introduce both Docker and Singularity.
We will use Docker to work locally on our own machines, and Singularity to work on the HPC.

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

## Container Images

One final term: while the **container** is an alternative filesystem layer that you
can access and run from your computer, the **container image** is the 'recipe' or template
for a container. The container image has all the required information to start
up a running copy of the container. A running container tends to be transient
and can be started and shut down. The container image is more long-lived, as a definition for the container.
You could think of the container image like a cookie cutter -- it
can be used to create multiple copies of the same shape (or container)
and is relatively unchanging, where cookies come and go. If you want a
different type of container (cookie) you need a different container image (cookie cutter).

![](fig/containers-cookie-cutter.png){alt='An image comparing using a cookie cutter to the container workflow'}

## Putting the Pieces Together

Think back to some of the challenges we described at the beginning. The many layers
of scientific software installations make it hard to install and re-install
scientific software -- which ultimately, hinders reliability and reproducibility.

But now, think about what a container is -- a self-contained, complete, separate
computer filesystem. What advantages are there if you put your scientific software
tools into containers?

This solves several of our problems:

- documentation -- there is a clear record of what software and software dependencies were used, from bottom to top.
- portability -- the container can be used on any computer that has Docker installed -- it doesn't matter whether the computer is Mac, Windows or Linux-based.
- reproducibility -- you can use the exact same software and environment on your computer and on other resources (like a large-scale computing cluster).
- configurability -- containers can be sized to take advantage of more resources (memory, CPU, etc.) on large systems (clusters) or less, depending on the circumstances.

The rest of this workshop will show you how to download and run containers from pre-existing
container images on your own computer, and how to create and share your own container images.

## Use cases for containers

Now that we have discussed a little bit about containers -- what they do and the
issues they attempt to address -- you may be able to think of a few potential use
cases in your area of work. Some examples of common use cases for containers in
a research context include:

- Using containers solely on your own computer to use a specific software tool
  or to test out a tool (possibly to avoid a difficult and complex installation
  process, to save your time or to avoid dependency hell).
- Creating a `Dockerfile` that generates a container image with software that you
  specify installed, then sharing a container image generated using this Dockerfile with
  your collaborators for use on their computers or a remote computing resource
  (e.g. cloud-based or HPC system).
- Archiving the container images so you can repeat analysis/modelling using the
  same software and configuration in the future -- capturing your workflow.



<!--  LocalWords:  keypoints links.md endcomment
 -->

:::::::::::::::::::::::::::::::::::::::: keypoints

- Almost all software depends on other software components to function, but these components have independent evolutionary paths.
- Small environments that contain only the software that is needed for a given task are easier to replicate and maintain.
- Critical systems that cannot be upgraded, due to cost, difficulty, etc. need to be reproduced on newer systems in a maintainable and self-documented way.
- Virtualization allows multiple environments to run on a single computer.
- Containerization improves upon the virtualization of whole computers by allowing efficient management of the host computer's memory and storage resources.
- Containers are built from 'recipes' that define the required set of software components and the instructions necessary to build/install them within a container image.
- Docker and Singularity/Apptainer are software platforms that can create containers and the resources they use.

::::::::::::::::::::::::::::::::::::::::::::::::::
