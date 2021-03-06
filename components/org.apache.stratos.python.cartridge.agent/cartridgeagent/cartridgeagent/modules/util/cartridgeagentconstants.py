# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

PARAM_FILE_PATH = "param.file.path"
EXTENSIONS_DIR = "extensions.dir"

MB_IP = "mb.ip"
MB_PORT = "mb.port"

CARTRIDGE_KEY = "CARTRIDGE_KEY"
APPLICATION_ID = "APPLICATION_ID"
APPLICATION_PATH = "APPLICATION_PATH"
SERVICE_GROUP = "SERIVCE_GROUP"
SERVICE_NAME = "SERVICE_NAME"
CLUSTER_ID = "CLUSTER_ID"
CLUSTER_INSTANCE_ID= "CLUSTER_INSTANCE_ID"
MEMBER_ID = "MEMBER_ID"
INSTANCE_ID= "INSTANCE_ID"
LB_CLUSTER_ID = "LB_CLUSTER_ID"
NETWORK_PARTITION_ID = "NETWORK_PARTITION_ID"
PARTITION_ID = "PARTITION_ID"
TENANT_ID = "TENANT_ID"
REPO_URL = "REPO_URL"
PORTS = "PORTS"
DEPLOYMENT = "DEPLOYMENT"
MANAGER_SERVICE_TYPE = "MANAGER_SERVICE_TYPE"
WORKER_SERVICE_TYPE = "WORKER_SERVICE_TYPE"
PERSISTENCE_MAPPING = "PERSISTENCE_MAPPING"
DEPENDENCY_CLUSTER_IDS = "DEPENDENCY_CLUSTER_IDS"
EXPORT_METADATA_KEYS="EXPORT_METADATA_KEYS"
IMPORT_METADATA_KEYS="IMPORT_METADATA_KEYS"

# stratos.sh environment variables keys
LOG_FILE_PATHS = "LOG_FILE_PATHS"
MEMORY_CONSUMPTION = "memory_consumption"
LOAD_AVERAGE = "load_average"
PORTS_NOT_OPEN = "ports_not_open"
MULTITENANT = "MULTITENANT"
CLUSTERING = "CLUSTERING"
MIN_INSTANCE_COUNT = "MIN_COUNT"
ENABLE_ARTIFACT_UPDATE = "enable.artifact.update"
ARTIFACT_UPDATE_INTERVAL = "artifact.update.interval"
COMMIT_ENABLED = "COMMIT_ENABLED"
AUTO_COMMIT = "auto.commit"
AUTO_CHECKOUT = "auto.checkout"
LISTEN_ADDRESS = "listen.address"
PROVIDER = "PROVIDER"
INTERNAL = "INTERNAL"
LB_PRIVATE_IP = "lb.private.ip"
LB_PUBLIC_IP = "lb.public.ip"

# stratos.sh extension points shell scripts names keys
INSTANCE_STARTED_SCRIPT = "extension.instance.started"
START_SERVERS_SCRIPT = "extension.start.servers"
INSTANCE_ACTIVATED_SCRIPT = "extension.instance.activated"
ARTIFACTS_UPDATED_SCRIPT = "extension.artifacts.updated"
CLEAN_UP_SCRIPT = "extension.clean"
MOUNT_VOLUMES_SCRIPT = "extension.mount.volumes"
MEMBER_ACTIVATED_SCRIPT = "extension.member.activated"
MEMBER_TERMINATED_SCRIPT = "extension.member.terminated"
MEMBER_SUSPENDED_SCRIPT = "extension.member.suspended"
MEMBER_STARTED_SCRIPT = "extension.member.started"
COMPLETE_TOPOLOGY_SCRIPT = "extension.complete.topology"
COMPLETE_TENANT_SCRIPT = "extension.complete.tenant"
SUBSCRIPTION_DOMAIN_ADDED_SCRIPT = "extension.subscription.domain.added"
SUBSCRIPTION_DOMAIN_REMOVED_SCRIPT = "extension.subscription.domain.removed"
ARTIFACTS_COPY_SCRIPT = "extension.artifacts.copy"
TENANT_SUBSCRIBED_SCRIPT = "extension.tenant.subscribed"
TENANT_UNSUBSCRIBED_SCRIPT = "extension.tenant.unsubscribed"

SERVICE_GROUP_TOPOLOGY_KEY = "payload_parameter.SERIVCE_GROUP"
CLUSTERING_TOPOLOGY_KEY = "payload_parameter.CLUSTERING"
CLUSTERING_PRIMARY_KEY = "PRIMARY"

SUPERTENANT_TEMP_PATH = "/tmp/-1234/"

DEPLOYMENT_MANAGER = "manager"
DEPLOYMENT_WORKER = "worker"
DEPLOYMENT_DEFAULT = "default"
SUPER_TENANT_REPO_PATH = "super.tenant.repository.path"
TENANT_REPO_PATH = "tenant.repository.path"

# topic names to subscribe
INSTANCE_NOTIFIER_TOPIC = "instance/#"
HEALTH_STAT_TOPIC = "health/#"
TOPOLOGY_TOPIC = "topology/#"
TENANT_TOPIC = "tenant/#"
INSTANCE_STATUS_TOPIC = "instance/status/"

#Messaging Model
TENANT_RANGE_DELIMITER = "-"

INSTANCE_STARTED_EVENT = "InstanceStartedEvent"
INSTANCE_ACTIVATED_EVENT = "InstanceActivatedEvent"
INSTANCE_MAINTENANCE_MODE_EVENT = "InstanceMaintenanceModeEvent"
INSTANCE_READY_TO_SHUTDOWN_EVENT = "InstanceReadyToShutdownEvent"

PUBLISHER_SERVICE_NAME = "publisher"
APISTORE_SERVICE_NAME = "apistore"
APIMANAGER_SERVICE_NAME = "apim"
GATEWAY_SERVICE_NAME = "gatewaymgt"
GATEWAY_MGT_SERVICE_NAME = "gateway"
KEY_MANAGER_SERVICE_NAME = "keymanager"

PRIMARY = "PRIMARY"
MIN_COUNT = "MIN_COUNT"

#multi tenant constants
INVALID_TENANT_ID = "-1"
SUPER_TENANT_ID = "-1234"

DATE_FORMAT = "%Y.%m.%d"

PORT_CHECK_TIMEOUT = "port.check.timeout"

CEP_PUBLISHER_ENABLED = "cep.stats.publisher.enabled"
CEP_RECEIVER_IP = "thrift.receiver.ip"
CEP_RECEIVER_PORT = "thrift.receiver.port"
CEP_SERVER_ADMIN_USERNAME = "thrift.server.admin.username"
CEP_SERVER_ADMIN_PASSWORD = "thrift.server.admin.password"

MONITORING_PUBLISHER_ENABLED = "enable.data.publisher"
MONITORING_RECEIVER_IP = "monitoring.server.ip"
MONITORING_RECEIVER_PORT = "monitoring.server.port"
MONITORING_RECEIVER_SECURE_PORT = "monitoring.server.secure.port"
MONITORING_SERVER_ADMIN_USERNAME = "monitoring.server.admin.username"
MONITORING_SERVER_ADMIN_PASSWORD = "monitoring.server.admin.password"