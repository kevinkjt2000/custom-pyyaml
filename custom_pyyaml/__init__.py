from typing import Optional

import pydantic
import yaml


class KubeSecret(pydantic.BaseModel):
    name: str
    key: str
    value: Optional[str] = None

    @pydantic.validator('value', always=True)
    def populate_secret_value(cls, v, values) -> str:
        print(f'Fetching super-secret {values["name"]}.{values["key"]}')
        return "tops3cret" # TODO: talk to kube API instead


def kube_secret_constructor(loader, node):
    return KubeSecret(**loader.construct_mapping(node))


yaml.SafeLoader.add_constructor("!KubeSecret", kube_secret_constructor)
