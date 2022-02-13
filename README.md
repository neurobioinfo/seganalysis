# genombox: : A package for  segregation analysis
***

## Contents
- [Segregation Analysis]
- [Apache Spark]

## Segregation Analysis
Segregation is a process to explore the genetic variant. 
## Apache Spark
The pipline is tested on [Spark-3.1.2, Pre-build for Apache Hadoop3.2](https://spark.apache.org/downloads.html).  

## Hail
The following show step running the step of running segregation on HTC system.  

#### Step 1: Make sure you are run sparking   
```
export SPARK_HOME=$HOME/spark-3.1.2-bin-hadoop3.2
export SPARK_LOG_DIR=$HOME/temp
module load java/11.0.2
cd ${SPARK_HOME}; ./sbin/start-master.sh

```

#### Step 2: Generate annotated file 
Run VEP to generate the annotated file.   
```
```

#### Step 3:  Create table matrix
the following code, import VCF as a MatrixTable, 
```
import sys
import pandas as pd 
import hail as hl
hl.import_vcf('~/annotated_file.vcf.gz',force=True,reference_genome='GRCh38',array_elements_required=False).write('~/out.mt', overwrite=True)
```

#### Step 4: Run the module

```
from seganalysis import seg
mt = hl.read_matrix_table('~/out.mt')
dest='~/result'
ped=pd.read_csv('~/pedfile.ped'.ped',sep='\t')
vcffile='~/???.vcf'
seg.segrun(mt, ped,dest,hl,vcffile)    
```


## output
The output of segregation can be categorized to  1) locus and alleles,  2) Global- Non-Affected 3) Global-Affected 4) Family, 5) Family-Affected 6) Family - Non-affected.  
#### locus and alleles
locus: chromosome
alleles:  a variant form of a gene
#### Global - Non-Affected
glb_naf_wild: Global - Non-Affecteds, wildtype
glb_naf_ncl:     Global - Non-Affecteds, no call     
glb_naf_vrt:     Global - Non-Affecteds, with variant    
glb_naf_homv:    Global - Non-Affecteds, homozygous for ALT allele
glb_naf_altaf:   Global - Non-Affecteds, ALT allele frequency   

#### Global - Affected
glb_aff_wild: Global - Affecteds, wildtype 
glb_aff_ncl:     Global - Affecteds, no call     
glb_aff_vrt:     Global - Affecteds, with variant  
glb_aff_homv:    Global - Affecteds, homozygous for ALT allele
glb_aff_altaf:   Global - Affecteds, ALT allele frequency   

#### Family
{famid}_wild: Family - Affecteds: wildtype 
{famid}_ncl: Family - Affecteds: no call
{famid}_vrt: Family - Affecteds: with variant
{famid}_homv: Family - Affecteds: homozygous for ALT allele

#### Family - Affected
{famid}_wild_aff: Family - Affecteds: wildtype 
{famid}_ncl_aff: Family - Affecteds: no call
{famid}_vrt_aff: Family - Affecteds: with variant
{famid}_homv_aff: Family - Affecteds: homozygous for ALT allele

#### Family - Nonaffected   
{famid}_wild_naf: Family - Nonaffecteds: wildtype 
{famid}_ncl_naf: Family - Nonaffecteds: no call
{famid}_vrt_naf: Family - Nonaffecteds: with variant
{famid}_homv_naf: Family - Nonaffecteds: homozygous for ALT allele



## Contributing
This is an early version, any contribute or suggestion is appreciated.

## Changelog
Every release is documented on the [GitHub Releases page](https://github.com/The-Neuro-Bioinformatics-Core/seganalysis/releases).

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/The-Neuro-Bioinformatics-Core/seganalysis/blob/main/LICENSE) file for details

## Todo
???

**[⬆ back to top](#contents)**