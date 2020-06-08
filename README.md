# cysteine
Python3 script to calculate the cysteine content of all human proteins and to sort them according to cysteine content and length. As raw material, it uses a uniprot (https://www.uniprot.org) search with the parameters organism = Homo sapiens and reviewed = yes. The thus specified sequences (from a search on January 9, 2020) are provided locally in a fasta file.

## Requirements
This script has been developed to run under Linux and was specifically tested ONLY under Ubuntu 18.04. It has the following requirements:

### PYTHON MODULES

The following Python modules need to be installed:

* biopython

>sudo pip3 install biopython
