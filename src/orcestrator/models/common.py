from typing import Annotated

from pydantic.functional_validators import BeforeValidator

# Note:
# MongoDB stores data as BSON. FastAPI encodes and decodes data as JSON strings.
# BSON has support for additional non-JSON-native data types, including ObjectId
# which can't be directly encoded as JSON. Because of this, we convert ObjectIds
# to strings before storing them as the id field.


# Create a new type called PyObjectId
# - type is a string
# - before pydantic validates if the string is a valid ObjectId,
#   the BeforeValidator `func` is called on it
#   which in this case will convert the string to a string
#     - It will be represented as a `str` on the model so that it can be serialized to JSON.

PyObjectId = Annotated[str, BeforeValidator(str)]
