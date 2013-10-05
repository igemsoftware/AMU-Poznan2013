shmir
=====

sh-miR Designer is a software aimed for fast and efficient design of effective RNA interference (RNAi) reagents - sh-miRs, also known as artificial miRNAs. sh-miRs are RNA particles whose structure is based on miRNA precursor pri-miRNA, but sequence interacting with transcript is changed depending on research purpose. Maintenance of structure of pri-miRNA is very important to enable cellular processing and therefore ensure functionality of artificial particles. sh-miRs delivered to cells on genetic vectors - plasmids or viral vectors - enter natural RNAi pathway and silence target mRNA. They can be used in genetic therapies and basic biomedical research.

##Documentation:
* [sh-miR Designer](http://shmir-designer.readthedocs.org/)
* [sh-miR Api](http://shmir-api.rtfd.org)

##What you need to use it?
* python in version 2.7

##How to use it?
Change directory to shmir_designer, run terminal and write:
```
./main seq1 seq2
```
or
```
./main seq
```
Where seq1 and seq2 are strands in 5'-3' orientation
If you use only one strand program will generate another complementary to the first.

You can also use it on our [website](http://shmir.pl) what is much easier.
[Instruction video](http://youtu.be/bZrlwx_D_8s)

##What if you would like to make own mfold/database server?
You need to do it:
* python in version 3.3
* [mfold](http://mfold.rna.albany.edu/?q=mfold/mfold-references)
* postgresql
* flask
* psycopg2

[How?](shmir_api/README.md)
