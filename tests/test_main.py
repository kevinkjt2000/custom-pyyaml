import yaml

import custom_pyyaml


def test_can_load_special_classes():
    secret = yaml.safe_load("""
!KubeSecret secret-name:something
    """)
    assert secret.value == "tops3cret"
