import yaml

import custom_pyyaml


def test_can_load_special_classes():
    secret = yaml.safe_load("""
!KubeSecret
name: nubium-secrets
key: something
    """)
    assert secret.value == "tops3cret"
