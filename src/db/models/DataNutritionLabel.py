from pydantic import (
    Field,
    ConfigDict,
    BaseModel,
    ValidationError,
    ValidationInfo,
    field_validator,
)
from pydantic.functional_validators import BeforeValidator

from typing import Annotated, List, Optional


from datetime import datetime

# {
#   "data_source": {
#     "rawdata": {
#       "description": [
#         "Data available from EGA under accession EGAD00001001357. 466 samples. Access to raw cram files requires DAC approval. NOTE: This data is not yet used in the pipeline"
#       ],
#       "url": [
#         "https://ega-archive.org/datasets/EGAD00001001357"
#       ]
#     },
#     "processed": {
#       "description": [
#         "Read counts, TPM & FPKM-values for all sequenced models including cell lines and organoids."
#       ],
#       "tool": [
#         "TODO::(add tool)"
#       ],
#       "tool_version": [
#         "TODO::(add tool version)"
#       ],
#       "url": [
#         "https://cog.sanger.ac.uk/cmp/download/rnaseq_all_20220624.zip"
#       ]
#     }
#   },
#   "filename": [
#     "rnaseq_fpkm_20220624.csv"
#   ],
#   "annotation": [
#     "rnaseq"
#   ],
#   "datatype": [
#     "fpkm"
#   ],
#   "date": [
#     "2024-02-26"
#   ],
#   "numSamples": [
#     949
#   ]
# },


class DataSource(BaseModel):
    description: str
    url: str
    tool: Optional[str] = None
    tool_version: Optional[str] = None

    class Config:
        orm_mode = True


class DataComponent(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    Name: str
    Data_Sources: List[DataSource]
    Filename: List[str]
    Annotation: str
    DataType: str
    Date: datetime


class DataNutritionLabel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    Pipeline_Name: str
    Description: str
    Pipeline_Version: str
