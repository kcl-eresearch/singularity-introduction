---
title: Files in Singularity containers
teaching: 10
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- Understand that some data from the host system is usually made available by default within a container
- Learn more about how Singularity handles users and binds directories from the host filesystem.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How do I make data available in a Singularity container?
- What data is made available by default in a Singularity container?

::::::::::::::::::::::::::::::::::::::::::::::::::

The way in which user accounts and access permissions are handled in Singularity containers is very different from that in Docker (where you effectively always have superuser/root access). When running a Singularity container, you only have the same permissions to access files as the user you are running as on the host system.

In this episode we'll look at working with files in the context of Singularity containers and how this links with Singularity's approach to users and permissions within containers.

## Users within a Singularity container

The first thing to note is that when you ran `whoami` within the container shell you started at the end of the previous episode, you should have seen the username that you were signed in as on the host system when you ran the container.

For example, if my username were `jc1000`, I'd expect to see the following:

```bash
$ singularity shell hello-world.sif
Singularity> whoami
jc1000
```

But hang on! I downloaded the standard, public version of the `hello-world.sif` image from Singularity Hub. I haven't customised it in any way. How is it configured with my own user details?!

If you have any familiarity with Linux system administration, you may be aware that in Linux, users and their Unix groups are configured in the `/etc/passwd` and `/etc/group` files respectively. In order for the shell within the container to know of my user, the relevant user information needs to be available within these files within the container.

Assuming this feature is enabled within the installation of Singularity on your system, when the container is started, Singularity appends the relevant user and group lines from the host system to the `/etc/passwd` and `/etc/group` files within the container [[1](#ref-1)].

This means that the host system can effectively ensure that you cannot access/modify/delete any data you should not be able to on the host system and you cannot run anything that you would not have permission to run on the host system since you are restricted to the same user permissions within the container as you are on the host system.

## Files and directories within a Singularity container

Singularity also *binds* some *directories* from the host system where you are running the `singularity` command into the container that you're starting. Note that this bind process is not copying files into the running container, it is making an existing directory on the host system visible and accessible within the container environment. If you write files to this directory within the running container, when the container shuts down, those changes will persist in the relevant location on the host system.

There is a default configuration of which files and directories are bound into the container but ultimate control of how things are set up on the system where you are running Singularity is determined by the system administrator. As a result, this section provides an overview but you may find that things are a little different on the system that you're running on.

One directory that is likely to be accessible within a container that you start is your *home directory*.  You may also find that the directory from which you issued the `singularity` command (the *current working directory*) is also mapped.

The mapping of file content and directories from a host system into a Singularity container is illustrated in the example below showing a subset of the directories on the host Linux system and in a Singularity container:

```output
Host system:                                                      Singularity container:
-------------                                                     ----------------------
/                                                                 /
├── bin                                                           ├── bin
├── etc                                                           ├── etc
│   ├── ...                                                       │   ├── ...
│   ├── group  ─> user's group added to group file in container ─>│   ├── group
│   └── passwd ──> user info added to passwd file in container ──>│   └── passwd
├── home                                                          ├── usr
│   └── jc1000 ───> user home directory made available ──> ─┐     ├── sbin
├── usr                 in container via bind mount         │     ├── home
├── sbin                                                    └────────>└── jc1000
└── ...                                                           └── ...

```

:::::::::::::::::::::::::::::::::::::::  challenge

## Questions and exercises: Files in Singularity containers

**Q1:** What do you notice about the ownership of files in a container started from the hello-world image? (e.g. take a look at the ownership of files in the root directory (`/`))

**Exercise 1:** In this container, try editing (for example using the editor `vi` which should be available in the container) the `/rawr.sh` file. What do you notice?

*If you're not familiar with `vi` there are many quick reference pages online showing the main commands for using the editor, for example [this one](https://web.mit.edu/merolish/Public/vi-ref.pdf).*

**Exercise 2:** In your home directory within the container shell, try and create a simple text file. Is it possible to do this? If so, why? If not, why not?! If you can successfully create a file, what happens to it when you exit the shell and the container shuts down?

:::::::::::::::  solution

## Answers

**A1:** Use the `ls -l` command to see a detailed file listing including file ownership and permission details. You should see that most of the files in the `/` directory are owned by `root`, as you'd probably expect on any Linux system. If you look at the files in your home directory, they should be owned by you.

**A Ex1:** We've already seen from the previous answer that the files in `/` are owned by `root` so we wouldn't expect to be able to edit them if we're not the root user. However, if you tried to edit `/rawr.sh` you probably saw that the file was read only and, if you tried for example to delete the file you would have seen an error similar to the following: `cannot remove '/rawr.sh': Read-only file system`. This tells us something else about the filesystem. It's not just that we don't have permission to delete the file, the filesystem itself is read-only so even the `root` user wouldn't be able to edit/delete this file. We'll look at this in more detail shortly.

**A Ex2:** Within your home directory, you *should* be able to successfully create a file. Since you're seeing your home directory on the host system which has been bound into the container, when you exit and the container shuts down, the file that you created within the container should still be present when you look at your home directory on the host system.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::


## Binding additional host system directories to the container

We may sometimes want to work with datasets or scripts stored in shared locations, using the container.
For example, in the `/datasets/hpc_training/sample-files/arrayjob/` folder contains some toy data files. 

Let's say we wanted to analyse these files using a container based on the `hello-world.sif` container image.


:::::::::::::::::::::::::::::::::::::::  challenge

## Running containers

Question: What command would we use to run `ls` from the `hello-world.sif` container?


:::::::::::::::  solution

## Solution

We can run `ls` inside a container from the image using:

```bash
$ singularity exec hello-world.sif ls
```
:::::::::::::::::::

::::::::::::::::::::::::::::::::::::::: 

If we try using the container to run `ls` on the shared dataset directory, what happens?

```bash
$ singularity exec hello-world.sif ls 
```

```output
/bin/ls: cannot access /datasets/hpc_training/sample-files/arrayjob/: No such file or directory
```

:::::::::::::::::::::::::::::::::::::::  challenge

## No such file or directory

Question: What does the error message mean? Why might `ls` inside the container
not be able to find or open our directory?

This question is here for you to think about - we explore the answer to this
question in the content below.

::::::::::::::::::::::::::::::::::::::::::::::::::

The problem here is that the container and its filesystem is separate from our
host computer's filesystem. When the container runs, it can't see anything outside
itself, apart from the files and directories we discussed above, which are bound to the container by default.

In order to access data files (outside the container, on our host computer),
we need to *bind* that directory to the container, and create a link between the container and our host computer.

We can create a mount between our computer and the running container by using an additional
option to `singularity run` or `singularity exec`. The option will look like this

`--bind /datasets/hpc_training/sample-files/arrayjob/:/data`

What this means is: make the directory `/datasets/hpc_training/sample-files/arrayjob/` (on the host computer) -- the source --
*visible* within the container that is about to be started, and inside this container, name the
directory `/temp` -- the target.

Let's try running the command now:

```bash
$ singularity exec --bind /datasets/hpc_training/sample-files/arrayjob/:/data hello-world.sif ls /datasets/hpc_training/sample-files/arrayjob/
```

But we get the same error!

```output
/bin/ls: cannot access /datasets/hpc_training/sample-files/arrayjob/: No such file or directory
```

This final piece is a bit tricky -- we really have to remember to put ourselves
inside the container. Where is the data? It's in the directory that's been
mapped to `/data` -- so we need to include that in the path to `ls`. This
command should give us what we need:

```bash
$ singularity exec --bind /datasets/hpc_training/sample-files/arrayjob/:/data hello-world.sif ls /data
```

Note that if we create any files in the `/data` directory while the container is
running, these files will appear on our host filesystem in the original directory
and will stay there even when the container stops.


Note that you don't *need* to specify a target mount location in the container.
By default, a bind is mounted at the same path in the container as on the host system.
So we could also use this command:

```bash
$ singularity exec --bind /datasets/hpc_training/sample-files/arrayjob/ hello-world.sif ls /datasets/hpc_training/sample-files/arrayjob/
```

You can also specify multiple binds to `--bind` by separating them by commas (`,`).

You can also copy data into a container image at build time if there is some static data required in the image. We cover this later in the section on building containers.

:::::::::::::::::::::::::::::::::::::::: challenge

## Exercise - binding directories

Bind the `/datasets/hpc_training/` directory into the `hello-world.sif` container.
Can you run the "`helloworld.py`"  script found in `/datasets/hpc_training/utils/`?

:::::::::::::::  solution

## Solution

```bash
$ singularity exec --bind /datasets/hpc_training/ hello-world.sif python3 /datasets/hpc_training/utils/helloworld.py 
```

```output
Hello World!
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## References

[1] Gregory M. Kurzer, Containers for Science, Reproducibility and Mobility: Singularity P2. Intel HPC Developer Conference, 2017. Available at: [https://www.intel.com/content/dam/www/public/us/en/documents/presentation/hpc-containers-singularity-advanced.pdf](https://www.intel.com/content/dam/www/public/us/en/documents/presentation/hpc-containers-singularity-advanced.pdf){#ref-1}

:::::::::::::::::::::::::::::::::::::::: keypoints

- Your current directory and home directory are usually available by default in a container.
- You have the same username and permissions in a container as on the host system.
- You can specify additional host system directories to be available in the container.

::::::::::::::::::::::::::::::::::::::::::::::::::


