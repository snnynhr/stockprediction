About ark-sage
==============

Ark-SAGE is a Java library that implements the L1-regularized version of **S**parse **A**dditive **G**enerativ**E** models of Text (SAGE).
SAGE is an algorithm for learning sparse representations of text. Details of the algorithm is described in

> Eisenstein, Jacob, Amr Ahmed, and Eric P. Xing. "Sparse additive generative models of text." In _Proceedings of ICML_. pp. 1041-1048. 2011. [PDF](http://www.cc.gatech.edu/~jeisenst/papers/icml2011.pdf)

The idea behind the L1-regularized implementation of SAGE is briefly described in

> Yanchuan Sim, Noah A. Smith, David A. Smith. "Discovering Factions in the Computational Linguistics Community." In _Proceedings of the Association for Computational Linguistics (ACL 2012) Special Workshop on Rediscovering 50 Years of Discoveries_. pp. 22-32. 2012. [PDF](http://dl.acm.org/citation.cfm?id=2390511)

There are several ways you can use this library.
The most straightforward way is to use SAGE for learning sparse effects without latent variables using the tool included in the library.
You can run the tool using the shell script

    ./supervised-SAGE.sh --help

See the relevant [Javadoc for ark-sage](http://skylander.bitbucket.org/ark-sage/) on

    edu.cmu.cs.ark.sage.apps.SupervisedSAGE

for more details.

Fixes to Version 0.1 (4/7/2013)
--------------------------------
- Fixed usage information appearing > 1 time.

Fixes to Version 0.1 (3/9/2013)
--------------------------------
- Added regularization penalty to log likelihood calculation.
- Fixed wrong commons-math library version in `supervised-SAGE.sh` script
- Added `-XX:ParallelGCThreads` as a default option in `supervised-SAGE.sh` script

Version 0.1 (3/3/2013)
----------------------
- Initial release of SAGE along with SupervisedSAGE implementation.