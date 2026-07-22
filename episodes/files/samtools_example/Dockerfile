
FROM ubuntu:25.10

# Build-time arguments
ARG VERSION=1.19.2
ARG URL=https://github.com/samtools/samtools/releases/download/

# Upgrade existing packages
# set -e: exit on error
# set -u: treat unset variables as errors
# set -x: print commands before running - helps debugging
RUN set -eux; \
    apt-get update; \
    apt-get upgrade -y

# Install only required dependencies, clean up after
RUN set -eux; \
    apt-get install -y --no-install-recommends ca-certificates wget bzip2 \
    autoconf automake make gcc perl zlib1g-dev libbz2-dev liblzma-dev \
    libcurl4-gnutls-dev libssl-dev libncurses5-dev libdeflate-dev; \
    rm -rf /var/lib/apt/lists/* 

# Download and unzip samtools code
RUN set -eux; \
    TAR="samtools-${VERSION}.tar.bz2"; \
    wget --https-only --timeout=30 -O "/tmp/${TAR}" "${URL}/${VERSION}/${TAR}"; \
    tar -xf "/tmp/${TAR}" -C "/opt"; \
    rm -rf "/tmp/${TAR}"

# Configure and install samtools
RUN set -eux; \
    cd /opt/samtools-${VERSION}; \
    ./configure; \
    make; \
    make install