# Pharmacoset-Specific

These are the PharmacoSet Specific DNL requirements


## PharmacoSet

```plantuml
@startjson
{
    "Data Components": {
        "MolecularProfiles": [
            {
                "annotation": "rnaseq",
                "datatype" : "fpkm",
                "class" : "SummarizedExperiment",
                "filename" : "rnaseq_fpkm_20220624.csv",
                "data_source": {
                    "description" : "Read counts, TPM & FPKM-values for all sequenced models including cell lines and organoids.",
                    "tool" : "TODO::(add tool)",
                    "url" : "https://cog.sanger.ac.uk/cmp/download/rnaseq_all_20220624.zip"
                },
                "date" : "2024-02-26",
                "numSamples" : 949
            },
            {
                "annotation": "rnaseq",
                "datatype" : "tpm",
                "class" : "SummarizedExperiment",
                "filename" : "rnaseq_tpm_20220624.csv",
                "data_source": {
                    "description" : "Read counts, TPM & FPKM-values for all sequenced models including cell lines and organoids.",
                    "tool" : "TODO::(add tool)",
                    "url" : "https://cog.sanger.ac.uk/cmp/download/rnaseq_all_20220624.zip"
                },
                "date" : "2024-02-26",
                "numSamples" : 949
            },
            {
                "annotation": "cnv",
                "datatype" : "genes",
                "class" : "SummarizedExperiment",
                "filename" : "WES_pureCN_CNV_genes_20221213.csv",
                "data_source": {
                    "description" : "Total copy number and categorical CNA calls derived from WES data processed through PureCN.",
                    "tool" : "TODO::(add tool)",
                    "url" : "https://cog.sanger.ac.uk/cmp/download/WES_pureCN_CNV_genes_20221213.zip"
                },
                "date" : "2024-02-26 19:50:17",
                "numSamples" : 934
            },
            {
                "annotation": "cnv",
                "datatype" : "genes_cn_category",
                "class" : "SummarizedExperiment",
                "filename" : "WES_pureCN_CNV_genes_cn_category_20221213.csv",
                "data_source": {
                    "description" : "Total copy number and categorical CNA calls derived from WES data processed through PureCN.",
                    "tool" : "TODO::(add tool)",
                    "url" : "https://cog.sanger.ac.uk/cmp/download/WES_pureCN_CNV_genes_20221213.zip"
                },
                "date" : "2024-02-26 19:50:17",
                "numSamples" : 934
            },
            {
                "annotation": "fusion",
                "datatype" : "",
                "class" : "SummarizedExperiment",
                "filename" : "Fusions_20230725.zip",
                "data_source": {
                    "description" : "TODO::(add description)",
                    "tool" : "TODO::(add tool)",
                    "url" : "https://cog.sanger.ac.uk/cmp/download/Fusions_20230725.zip"
                },
                "date" : "2024-02-26 19:50:17",
                "numSamples" : 934
            }
        ],
        "treatmentResponse" : [
            {
                "filename": "GDSC2_public_raw_data.csv; GDSC2_fitted_dose_response.xlsx",
                "data_source": {
                    "description" : "The raw data for the GDSC2 release 8.5 is available from the GDSC website.",
                    "tool" : "TODO::(add tool)",
                    "url" : "https://www.cancerrxgene.org/downloads/bulk_download"
                },
                "date" : "2024-02-26"
            }
        ],
        "sampleMetadata" : {
            "numSamples": 1000,
            "sampleAnnotations" : [
                "GDSC.sampleid",
                "GDSC.Sample_Name",
                "CMP.model_id",
                "cellosaurus.acc",
                "cellosaurus.id",
                "cellosaurus.samplingSite",
                "cellosaurus.diseases",
                "etc..."
            ]
        },
        "treatmentMetadata" : {
            "numTreatments": 539,
            "treatmentAnnotations" : [
                "pubchem.ChEMBL.ID",
                "GDSC.treatmentid",
                "GDSC.DRUG_ID",
                "pubchem.CID",
                "pubchem.InChIKey",
                "pubchem.NSC.Number",
                "pubchem.DILI.Status",
                "pubchem.CAS.Number",
                "pubchem.ATC.Code",
                "etc..."
            ]
        }
     }
}
@endjson
```

### Python Pydantic class definitions of the json


```Python
import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

class DataSource_DNL(BaseModel):
    description: str
    tool: Optional[str] = None
    url: str

class MolecularProfile_DNL(BaseModel):
    annotation: str
    datatype: str
    class_: str = Field(alias="class")
    filename: str
    data_source: DataSource_DNL
    date: datetime.datetime
    numSamples: int

class TreatmentResponse_DNL(BaseModel):
    filename: str
    data_source: DataSource_DNL
    date: datetime.datetime

class SampleMetadata_DNL(BaseModel):
    numSamples: int
    sampleAnnotations: List[str]

class TreatmentMetadata_DNL(BaseModel):
    numTreatments: int
    treatmentAnnotations: List[str]

class PharmacoSet_DNL(BaseModel):
    MolecularProfiles: List[MolecularProfile]
    treatmentResponse: List[TreatmentResponse]
    sampleMetadata: SampleMetadata
    treatmentMetadata: TreatmentMetadata

```
