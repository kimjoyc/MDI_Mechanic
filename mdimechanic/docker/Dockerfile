#------------------------------------------------------------#
# Docker file for MDI Mechanic
#------------------------------------------------------------#

FROM mdi/base

RUN apt-get update -y && \
    apt-get install -y \
        git \
        cmake \
        graphviz \
	expect \
        && \
    apt-get clean && \
    apt-get purge && \
    rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* && \
    pip install mpi4py && \
    pip install pandas && \
    pip install PyYAML && \
    pip install graphviz && \
    pip install pymdi
