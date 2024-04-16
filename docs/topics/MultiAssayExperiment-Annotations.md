# Molecular Profile Annotations

TODO::Convert this to an `.Rmd` file and add examples

Standard `@metadata` slot annotations each `Experiment` in a `MultiAssayExperiment` object.

```yaml
"MolecularProfiles": [
    {
        "annotation": string, # one of "rnaseq", "rna", "cnv", "mut"
        "datatype" : string, #  Any subtype of annotation, e.g. "fpkm", "tpm"
        "class" : string, # one off "SummarizedExperiment", "RangedSummarizedExperiment", "Matrix", "BumpyMatrix", "ExpressionSet", etc.],
        "filename" : string, # The exact file name used to load this data, i.e "rnaseq_fpkm_20220624.csv"
        "data_source": {
            "description" : string, # A sentence or two describing the data & its source
            "tool" : string, # Tool used to generate the data, i.e "STAR", "PureCN", "Kallisto"
            "url" : string, # Exact URL used to access & possibly download the data, i.e "https://cog.sanger.ac.uk/cmp/download/rnaseq_all_20220624.zip"
        },
        "date" : string, # Date the data was generated, i.e "2024-02-26"
        "numSamples" : integer, # Number of samples in the data, i.e 949
        "numGenes" : integer, # Number of genes in the data, i.e 20000
    },
    ...
]
```

#### Example adding metadata to a Summarized Experiment

If you already have a `SummarizedExperiment` object, you can add metadata to it like this:

```R
# assume you have a Summarized Experiment:

show(genes_tpm_SE)
# class: RangedSummarizedExperiment
# dim: 3 2
# metadata(0):
# assays(1): exprs
# rownames(3): gene1 gene2 gene3
# rowData names(1): gene_id
# colnames(2): sample1 sample2
# colData names(2): sampleid batchid

genes_tpm_SE@metadata <- list(
    annotation = "rnaseq",
    datatype = "genes_tpm",
    class = "RangedSummarizedExperiment",
    filename = "rnaseq_fpkm_20220624.csv",
    data_source = list(
        # In this example, the source file url is a zip of multiple files, including the one above
        description = "Read counts, TPM & FPKM-values for all sequenced models including cell lines and organoids.",
        tool = "STAR v2.7.9a",
        url = "https://cog.sanger.ac.uk/cmp/download/rnaseq_all_20220624.zip"
    ),
    date = Sys.Date(),
    numSamples = ncol(genes_tpm_SE),
    numGenes = nrow(genes_tpm_SE)
)

show(genes_tpm_SE@metadata)
$annotation
[1] "rnaseq"

$datatype
[1] "genes_tpm"

$class
[1] "RangedSummarizedExperiment"

$filename
[1] "rnaseq_fpkm_20220624.csv"

$data_source
$data_source$description
[1] "Read counts, TPM & FPKM-values for all sequenced models including cell lines and organoids."

$data_source$tool
[1] "STAR v2.7.9a"

$data_source$url
[1] "https://cog.sanger.ac.uk/cmp/download/rnaseq_all_20220624.zip"


$date
[1] "2024-04-12"

$numSamples
[1] 2

```
