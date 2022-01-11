import yaml


class KubeSecret:
    def __setstate__(self, d):
        name = d["name"]
        key = d["key"]

        print(f"Fetching super-secret {name}.{key}")
        self._value = "tops3cret" # TODO: talk to kube API instead

    @property
    def value(self):
        return self._value
