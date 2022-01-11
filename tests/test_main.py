from yaml import load, dump, CLoader as Loader, CDumper as Dumper


def test_can_load_special_classes():
    secret = load("""
!!python/object:custom_pyyaml.KubeSecret
name: Welthyr Syxgon
key: something
    """, Loader=Loader)
    assert secret.value == "tops3cret"
