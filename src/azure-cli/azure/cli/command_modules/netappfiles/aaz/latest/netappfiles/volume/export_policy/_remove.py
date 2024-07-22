# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "netappfiles volume export-policy remove",
    confirmation="Are you sure you want to perform this operation?",
)
class Remove(AAZCommand):
    """Remove a rule from the export policy for a volume by rule index. The current rules can be obtained by performing the subgroup list command.

    :example: Remove an export policy rule from an ANF volume
        az netappfiles volume export-policy remove -g mygroup --account-name myaccname --pool-name mypoolname --name myvolname --rule-index 4
    """

    _aaz_info = {
        "version": "2024-03-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.netapp/netappaccounts/{}/capacitypools/{}/volumes/{}", "2024-03-01", "properties.exportPolicy.rules[]"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self.SubresourceSelector(ctx=self.ctx, name="subresource")
        return self.build_lro_poller(self._execute_operations, None)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.account_name = AAZStrArg(
            options=["-a", "--account-name"],
            help="The name of the NetApp account",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9\\-_]{0,127}$",
            ),
        )
        _args_schema.pool_name = AAZStrArg(
            options=["-p", "--pool-name"],
            help="The name of the capacity pool",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9\\-_]{0,63}$",
                max_length=64,
                min_length=1,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.volume_name = AAZStrArg(
            options=["-n", "-v", "--name", "--volume-name"],
            help="The name of the volume",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z][a-zA-Z0-9\\-_]{0,63}$",
                max_length=64,
                min_length=1,
            ),
        )
        _args_schema.rule_index = AAZIntArg(
            options=["--rule-index"],
            help="Order index",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.VolumesGet(ctx=self.ctx)()
        self.pre_instance_delete()
        self.InstanceDeleteByJson(ctx=self.ctx)()
        self.post_instance_delete()
        yield self.VolumesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_delete(self):
        pass

    @register_callback
    def post_instance_delete(self):
        pass

    class SubresourceSelector(AAZJsonSelector):

        def _get(self):
            result = self.ctx.vars.instance
            result = result.properties.exportPolicy.rules
            filters = enumerate(result)
            filters = filter(
                lambda e: e[1].ruleIndex == self.ctx.args.rule_index,
                filters
            )
            idx = next(filters)[0]
            return result[idx]

        def _set(self, value):
            result = self.ctx.vars.instance
            result = result.properties.exportPolicy.rules
            filters = enumerate(result)
            filters = filter(
                lambda e: e[1].ruleIndex == self.ctx.args.rule_index,
                filters
            )
            idx = next(filters, [len(result)])[0]
            result[idx] = value
            return

    class VolumesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "accountName", self.ctx.args.account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "poolName", self.ctx.args.pool_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "volumeName", self.ctx.args.volume_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-03-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _RemoveHelper._build_schema_volume_read(cls._schema_on_200)

            return cls._schema_on_200

    class VolumesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "accountName", self.ctx.args.account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "poolName", self.ctx.args.pool_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "volumeName", self.ctx.args.volume_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-03-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _RemoveHelper._build_schema_volume_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceDeleteByJson(AAZJsonInstanceDeleteOperation):

        def __call__(self, *args, **kwargs):
            self.ctx.selectors.subresource.set(self._delete_instance())


class _RemoveHelper:
    """Helper class for Remove"""

    _schema_volume_read = None

    @classmethod
    def _build_schema_volume_read(cls, _schema):
        if cls._schema_volume_read is not None:
            _schema.etag = cls._schema_volume_read.etag
            _schema.id = cls._schema_volume_read.id
            _schema.location = cls._schema_volume_read.location
            _schema.name = cls._schema_volume_read.name
            _schema.properties = cls._schema_volume_read.properties
            _schema.system_data = cls._schema_volume_read.system_data
            _schema.tags = cls._schema_volume_read.tags
            _schema.type = cls._schema_volume_read.type
            _schema.zones = cls._schema_volume_read.zones
            return

        cls._schema_volume_read = _schema_volume_read = AAZObjectType()

        volume_read = _schema_volume_read
        volume_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        volume_read.id = AAZStrType(
            flags={"read_only": True},
        )
        volume_read.location = AAZStrType(
            flags={"required": True},
        )
        volume_read.name = AAZStrType(
            flags={"read_only": True},
        )
        volume_read.properties = AAZObjectType(
            flags={"required": True, "client_flatten": True},
        )
        volume_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        volume_read.tags = AAZDictType()
        volume_read.type = AAZStrType(
            flags={"read_only": True},
        )
        volume_read.zones = AAZListType()

        properties = _schema_volume_read.properties
        properties.actual_throughput_mibps = AAZFloatType(
            serialized_name="actualThroughputMibps",
            flags={"read_only": True},
        )
        properties.avs_data_store = AAZStrType(
            serialized_name="avsDataStore",
        )
        properties.backup_id = AAZStrType(
            serialized_name="backupId",
            nullable=True,
        )
        properties.baremetal_tenant_id = AAZStrType(
            serialized_name="baremetalTenantId",
            flags={"read_only": True},
        )
        properties.capacity_pool_resource_id = AAZStrType(
            serialized_name="capacityPoolResourceId",
        )
        properties.clone_progress = AAZIntType(
            serialized_name="cloneProgress",
            nullable=True,
            flags={"read_only": True},
        )
        properties.cool_access = AAZBoolType(
            serialized_name="coolAccess",
        )
        properties.cool_access_retrieval_policy = AAZStrType(
            serialized_name="coolAccessRetrievalPolicy",
        )
        properties.coolness_period = AAZIntType(
            serialized_name="coolnessPeriod",
        )
        properties.creation_token = AAZStrType(
            serialized_name="creationToken",
            flags={"required": True},
        )
        properties.data_protection = AAZObjectType(
            serialized_name="dataProtection",
        )
        properties.data_store_resource_id = AAZListType(
            serialized_name="dataStoreResourceId",
            flags={"read_only": True},
        )
        properties.default_group_quota_in_ki_bs = AAZIntType(
            serialized_name="defaultGroupQuotaInKiBs",
        )
        properties.default_user_quota_in_ki_bs = AAZIntType(
            serialized_name="defaultUserQuotaInKiBs",
        )
        properties.delete_base_snapshot = AAZBoolType(
            serialized_name="deleteBaseSnapshot",
        )
        properties.enable_subvolumes = AAZStrType(
            serialized_name="enableSubvolumes",
        )
        properties.encrypted = AAZBoolType(
            flags={"read_only": True},
        )
        properties.encryption_key_source = AAZStrType(
            serialized_name="encryptionKeySource",
        )
        properties.export_policy = AAZObjectType(
            serialized_name="exportPolicy",
        )
        properties.file_access_logs = AAZStrType(
            serialized_name="fileAccessLogs",
            flags={"read_only": True},
        )
        properties.file_system_id = AAZStrType(
            serialized_name="fileSystemId",
            flags={"read_only": True},
        )
        properties.is_default_quota_enabled = AAZBoolType(
            serialized_name="isDefaultQuotaEnabled",
        )
        properties.is_large_volume = AAZBoolType(
            serialized_name="isLargeVolume",
        )
        properties.is_restoring = AAZBoolType(
            serialized_name="isRestoring",
        )
        properties.kerberos_enabled = AAZBoolType(
            serialized_name="kerberosEnabled",
        )
        properties.key_vault_private_endpoint_resource_id = AAZStrType(
            serialized_name="keyVaultPrivateEndpointResourceId",
        )
        properties.ldap_enabled = AAZBoolType(
            serialized_name="ldapEnabled",
        )
        properties.maximum_number_of_files = AAZIntType(
            serialized_name="maximumNumberOfFiles",
            flags={"read_only": True},
        )
        properties.mount_targets = AAZListType(
            serialized_name="mountTargets",
            flags={"read_only": True},
        )
        properties.network_features = AAZStrType(
            serialized_name="networkFeatures",
        )
        properties.network_sibling_set_id = AAZStrType(
            serialized_name="networkSiblingSetId",
            flags={"read_only": True},
        )
        properties.originating_resource_id = AAZStrType(
            serialized_name="originatingResourceId",
            nullable=True,
            flags={"read_only": True},
        )
        properties.placement_rules = AAZListType(
            serialized_name="placementRules",
        )
        properties.protocol_types = AAZListType(
            serialized_name="protocolTypes",
        )
        properties.provisioned_availability_zone = AAZStrType(
            serialized_name="provisionedAvailabilityZone",
            nullable=True,
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.proximity_placement_group = AAZStrType(
            serialized_name="proximityPlacementGroup",
        )
        properties.security_style = AAZStrType(
            serialized_name="securityStyle",
        )
        properties.service_level = AAZStrType(
            serialized_name="serviceLevel",
        )
        properties.smb_access_based_enumeration = AAZStrType(
            serialized_name="smbAccessBasedEnumeration",
            nullable=True,
        )
        properties.smb_continuously_available = AAZBoolType(
            serialized_name="smbContinuouslyAvailable",
        )
        properties.smb_encryption = AAZBoolType(
            serialized_name="smbEncryption",
        )
        properties.smb_non_browsable = AAZStrType(
            serialized_name="smbNonBrowsable",
        )
        properties.snapshot_directory_visible = AAZBoolType(
            serialized_name="snapshotDirectoryVisible",
        )
        properties.snapshot_id = AAZStrType(
            serialized_name="snapshotId",
            nullable=True,
        )
        properties.storage_to_network_proximity = AAZStrType(
            serialized_name="storageToNetworkProximity",
            flags={"read_only": True},
        )
        properties.subnet_id = AAZStrType(
            serialized_name="subnetId",
            flags={"required": True},
        )
        properties.t2_network = AAZStrType(
            serialized_name="t2Network",
            flags={"read_only": True},
        )
        properties.throughput_mibps = AAZFloatType(
            serialized_name="throughputMibps",
            nullable=True,
        )
        properties.unix_permissions = AAZStrType(
            serialized_name="unixPermissions",
            nullable=True,
        )
        properties.usage_threshold = AAZIntType(
            serialized_name="usageThreshold",
            flags={"required": True},
        )
        properties.volume_group_name = AAZStrType(
            serialized_name="volumeGroupName",
            flags={"read_only": True},
        )
        properties.volume_spec_name = AAZStrType(
            serialized_name="volumeSpecName",
        )
        properties.volume_type = AAZStrType(
            serialized_name="volumeType",
        )

        data_protection = _schema_volume_read.properties.data_protection
        data_protection.backup = AAZObjectType()
        data_protection.replication = AAZObjectType()
        data_protection.snapshot = AAZObjectType()
        data_protection.volume_relocation = AAZObjectType(
            serialized_name="volumeRelocation",
        )

        backup = _schema_volume_read.properties.data_protection.backup
        backup.backup_policy_id = AAZStrType(
            serialized_name="backupPolicyId",
        )
        backup.backup_vault_id = AAZStrType(
            serialized_name="backupVaultId",
        )
        backup.policy_enforced = AAZBoolType(
            serialized_name="policyEnforced",
        )

        replication = _schema_volume_read.properties.data_protection.replication
        replication.endpoint_type = AAZStrType(
            serialized_name="endpointType",
        )
        replication.remote_volume_region = AAZStrType(
            serialized_name="remoteVolumeRegion",
        )
        replication.remote_volume_resource_id = AAZStrType(
            serialized_name="remoteVolumeResourceId",
            flags={"required": True},
        )
        replication.replication_id = AAZStrType(
            serialized_name="replicationId",
            flags={"read_only": True},
        )
        replication.replication_schedule = AAZStrType(
            serialized_name="replicationSchedule",
        )

        snapshot = _schema_volume_read.properties.data_protection.snapshot
        snapshot.snapshot_policy_id = AAZStrType(
            serialized_name="snapshotPolicyId",
        )

        volume_relocation = _schema_volume_read.properties.data_protection.volume_relocation
        volume_relocation.ready_to_be_finalized = AAZBoolType(
            serialized_name="readyToBeFinalized",
            flags={"read_only": True},
        )
        volume_relocation.relocation_requested = AAZBoolType(
            serialized_name="relocationRequested",
        )

        data_store_resource_id = _schema_volume_read.properties.data_store_resource_id
        data_store_resource_id.Element = AAZStrType()

        export_policy = _schema_volume_read.properties.export_policy
        export_policy.rules = AAZListType()

        rules = _schema_volume_read.properties.export_policy.rules
        rules.Element = AAZObjectType()

        _element = _schema_volume_read.properties.export_policy.rules.Element
        _element.allowed_clients = AAZStrType(
            serialized_name="allowedClients",
        )
        _element.chown_mode = AAZStrType(
            serialized_name="chownMode",
        )
        _element.cifs = AAZBoolType()
        _element.has_root_access = AAZBoolType(
            serialized_name="hasRootAccess",
        )
        _element.kerberos5_read_only = AAZBoolType(
            serialized_name="kerberos5ReadOnly",
        )
        _element.kerberos5_read_write = AAZBoolType(
            serialized_name="kerberos5ReadWrite",
        )
        _element.kerberos5i_read_only = AAZBoolType(
            serialized_name="kerberos5iReadOnly",
        )
        _element.kerberos5i_read_write = AAZBoolType(
            serialized_name="kerberos5iReadWrite",
        )
        _element.kerberos5p_read_only = AAZBoolType(
            serialized_name="kerberos5pReadOnly",
        )
        _element.kerberos5p_read_write = AAZBoolType(
            serialized_name="kerberos5pReadWrite",
        )
        _element.nfsv3 = AAZBoolType()
        _element.nfsv41 = AAZBoolType()
        _element.rule_index = AAZIntType(
            serialized_name="ruleIndex",
        )
        _element.unix_read_only = AAZBoolType(
            serialized_name="unixReadOnly",
        )
        _element.unix_read_write = AAZBoolType(
            serialized_name="unixReadWrite",
        )

        mount_targets = _schema_volume_read.properties.mount_targets
        mount_targets.Element = AAZObjectType()

        _element = _schema_volume_read.properties.mount_targets.Element
        _element.file_system_id = AAZStrType(
            serialized_name="fileSystemId",
            flags={"required": True},
        )
        _element.ip_address = AAZStrType(
            serialized_name="ipAddress",
            flags={"read_only": True},
        )
        _element.mount_target_id = AAZStrType(
            serialized_name="mountTargetId",
            flags={"read_only": True},
        )
        _element.smb_server_fqdn = AAZStrType(
            serialized_name="smbServerFqdn",
        )

        placement_rules = _schema_volume_read.properties.placement_rules
        placement_rules.Element = AAZObjectType()

        _element = _schema_volume_read.properties.placement_rules.Element
        _element.key = AAZStrType(
            flags={"required": True},
        )
        _element.value = AAZStrType(
            flags={"required": True},
        )

        protocol_types = _schema_volume_read.properties.protocol_types
        protocol_types.Element = AAZStrType()

        system_data = _schema_volume_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        tags = _schema_volume_read.tags
        tags.Element = AAZStrType()

        zones = _schema_volume_read.zones
        zones.Element = AAZStrType()

        _schema.etag = cls._schema_volume_read.etag
        _schema.id = cls._schema_volume_read.id
        _schema.location = cls._schema_volume_read.location
        _schema.name = cls._schema_volume_read.name
        _schema.properties = cls._schema_volume_read.properties
        _schema.system_data = cls._schema_volume_read.system_data
        _schema.tags = cls._schema_volume_read.tags
        _schema.type = cls._schema_volume_read.type
        _schema.zones = cls._schema_volume_read.zones


__all__ = ["Remove"]
