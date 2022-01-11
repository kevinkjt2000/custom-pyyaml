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
    need_to_split = loader.construct_scalar(node)
    name, key = need_to_split.split(":")
    return KubeSecret(name=name, key=key)


yaml.SafeLoader.add_constructor("!KubeSecret", kube_secret_constructor)
