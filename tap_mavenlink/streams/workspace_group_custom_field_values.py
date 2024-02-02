from tap_mavenlink.streams.base import BaseStream
from tap_mavenlink.cache import resources as ResourceCache

import singer

LOGGER = singer.get_logger()  # noqa


class WorkspaceGroupCustomFieldValuesStream(BaseStream):
    NAME = 'WorkspaceGroupCustomFieldValuesStream'
    API_METHOD = 'GET'
    TABLE = 'workspace_group_custom_field_values'
    KEY_PROPERTIES = ['id']

    def extra_params(self):
        return {
            "subject_type": "WorkspaceGroup",
            "include": "subject",
        }

    @property
    def path(self):
        return '/custom_field_values.json'

    @property
    def response_key(self):
        return 'custom_field_values'
    
    def get_stream_data(self, result, extra):
        payload_dict = result[self.response_key]
        payload_values = payload_dict.values()

        workspace_group_ids = list(result['workspace_groups'].keys())

        transformed = []
        for i, record in enumerate(payload_values):
            record.update(extra)
            record = self.transform_record(record)
            record['workspace_group_id'] = workspace_group_ids[i]
            if self.CACHE:
                pk = record['id']
                ResourceCache[self.TABLE].add(pk)
            transformed.append(record)

        return transformed
