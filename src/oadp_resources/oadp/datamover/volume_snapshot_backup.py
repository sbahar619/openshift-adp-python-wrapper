from ocp_resources.resource import NamespacedResource
from src.oadp_constants.resources import ApiGroups


class VolumeSnapshotBackup(NamespacedResource):
    api_group = ApiGroups.DATAMOVER_OADP_API_GROUP.value

    @classmethod
    def get_vsbs_by_restore_name(cls, restore_name):
        return list(cls.get(label_selector=f"velero.io/restore-name={restore_name}"))