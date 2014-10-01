import os
import datetime
import logging
from threading import Thread, current_thread

from ..databridge.agent import *
from ..config.cartridgeagentconfiguration import CartridgeAgentConfiguration
from ..util import cartridgeagentutils
from exception.datapublisherexception import DataPublisherException


class LogPublisher(Thread):

    def __init__(self, file_path, stream_definition, tenant_id, alias, date_time, member_id):
        Thread.__init__(self)

        logging.basicConfig(level=logging.DEBUG)
        self.log = logging.getLogger(__name__)

        self.file_path = file_path
        self.thrift_publisher = ThriftPublisher(
            DataPublisherConfiguration.get_instance().monitoring_server_ip,
            DataPublisherConfiguration.get_instance().monitoring_server_port,
            DataPublisherConfiguration.get_instance().admin_username,
            DataPublisherConfiguration.get_instance().admin_password,
            stream_definition)
        self.tenant_id = tenant_id
        self.alias = alias
        self.datetime = date_time
        self.member_id = member_id

        self.terminated = False

    def run(self):
        if os.path.isfile(self.file_path) and os.access(self.file_path, os.R_OK):
            self.log.info("Starting log publisher for file: " + self.file_path + ", thread: " + current_thread())
            # open file and keep reading for new entries
            read_file = open(self.file_path, "r")
            read_file.seek(os.stat(self.file_path)[6])  # go to the end of the file

            while not self.terminated:
                where = read_file.tell()  # where the seeker is in the file
                line = read_file.readline()   # read the current line
                if not line:
                    # no new line entered
                    time.sleep(1)
                    read_file.seek(where)  # set seeker
                else:
                    # new line detected, create event object
                    event = ThriftEvent()
                    event.metaData.append(self.member_id)
                    event.payloadData.append(self.tenant_id)
                    event.payloadData.append(self.alias)
                    event.payloadData.append("")
                    event.payloadData.append(self.datetime)
                    event.payloadData.append("")
                    event.payloadData.append(line)
                    event.payloadData.append("")
                    event.payloadData.append("")
                    event.payloadData.append(self.member_id)
                    event.payloadData.append("")

                    self.thrift_publisher.publish(event)

            self.thrift_publisher.disconnect()  # dicsonnect the publisher upon being terminated
        else:
            raise DataPublisherException("Unable to read the file at path %r" % self.file_path)

    def terminate(self):
        """
        Allows the LogPublisher thread to be terminated to stop publishing to BAM/CEP. Allow a minimum of 1 second delay
        to take effect.
        """
        self.terminated = True


class LogPublisherManager(Thread):
    """
    A log publishing thread management thread which maintains a log publisher for each log file. Also defines a stream
    definition and the BAM/CEP server information for a single publishing context.
    """

    @staticmethod
    def define_stream():
        """
        Creates a stream definition for Log Publishing
        :return: A StreamDefinition object with the required attributes added
        :rtype : StreamDefinition
        """
        # stream definition
        stream_definition = StreamDefinition()
        valid_tenant_id = LogPublisherManager.get_valid_tenant_id(CartridgeAgentConfiguration.tenant_id)
        alias = LogPublisherManager.get_alias(CartridgeAgentConfiguration.cluster_id)
        stream_name = "logs." + valid_tenant_id + "." \
                      + alias + "." + LogPublisherManager.get_current_date()
        stream_version = "1.0.0"
        stream_definition.name = stream_name
        stream_definition.version = stream_version
        stream_definition.description = "Apache Stratos Instance Log Publisher"
        stream_definition.add_metadata_attribute("memberId", 'STRING')
        stream_definition.add_payloaddata_attribute("tenantID", "STRING")
        stream_definition.add_payloaddata_attribute("serverName", "STRING")
        stream_definition.add_payloaddata_attribute("appName", "STRING")
        stream_definition.add_payloaddata_attribute("logTime", "STRING")
        stream_definition.add_payloaddata_attribute("priority", "STRING")
        stream_definition.add_payloaddata_attribute("message", "STRING")
        stream_definition.add_payloaddata_attribute("logger", "STRING")
        stream_definition.add_payloaddata_attribute("ip", "STRING")
        stream_definition.add_payloaddata_attribute("instance", "STRING")
        stream_definition.add_payloaddata_attribute("stacktrace", "STRING")

        return stream_definition

    def __init__(self, logfile_paths):
        Thread.__init__(self)
        self.logfile_paths = logfile_paths
        self.publishers = {}
        self.ports = []
        self.ports.append(DataPublisherConfiguration.get_instance().monitoring_server_port)
        self.ports.append(DataPublisherConfiguration.get_instance().monitoring_server_secure_port)

        cartridgeagentutils.wait_until_ports_active(DataPublisherConfiguration.get_instance().monitoring_server_ip, self.ports)
        ports_active = cartridgeagentutils.check_ports_active(DataPublisherConfiguration.get_instance().monitoring_server_ip, self.ports)
        if not ports_active:
            raise DataPublisherException("Monitoring server not active, data publishing is aborted")

        self.stream_definition = self.define_stream()

    def run(self):
        if self.logfile_paths is not None and len(self.logfile_paths):
            for log_path in self.logfile_paths:
                # thread for each log file
                publisher = self.get_publisher(log_path)
                publisher.start()

    def get_publisher(self, log_path):
        """
        Retrieve the publisher for the specified log file path. Creates a new LogPublisher if one is not available
        :return: The LogPublisher object
        :rtype : LogPublisher
        """
        if log_path not in self.publishers:
            self.publishers[log_path] = LogPublisher(log_path, self.stream_definition)

        return self.publishers[log_path]

    def terminate_publisher(self, log_path):
        """
        Terminates the LogPublisher thread associated with the specified log file
        """
        if log_path in self.publishers:
            self.publishers[log_path].terminate()

    def terminate_all_publishers(self):
        """
        Terminates all LogPublisher threads
        """
        for publisher in self.publishers:
            publisher.terminate()

    @staticmethod
    def get_valid_tenant_id(tenant_id):
        if tenant_id == "-1" or tenant_id == "-1234":
            return "0"

        return tenant_id

    @staticmethod
    def get_alias(cluster_id):
        alias = ""
        try:
            alias = cluster_id.split("\\.")[0]
        except:
            alias = cluster_id

        return alias

    @staticmethod
    def get_current_date():
        """
        Returns the current date formatted as yyyy-MM-dd
        :return: Formatted date string
        :rtype : str
        """
        return datetime.date.today().strftime("%Y.%m.%d")


class DataPublisherConfiguration:
    """
    A singleton implementation to access configuration information for data publishing to BAM/CEP
    TODO: perfect singleton impl ex: Borg
    """

    __instance = None
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    @staticmethod
    def get_instance():
        """
        Singleton instance retriever
        :return: Instance
        :rtype : DataPublisherConfiguration
        """
        if DataPublisherConfiguration.__instance is None:
            DataPublisherConfiguration.__instance = DataPublisherConfiguration()

        return DataPublisherConfiguration.__instance

    def __init__(self):
        self.enabled = False
        self.monitoring_server_ip = None
        self.monitoring_server_port = None
        self.monitoring_server_secure_port = None
        self.admin_username = None
        self.admin_password = None
        self.read_config()

    def read_config(self):
        self.enabled = True if CartridgeAgentConfiguration.read_property("enable.data.publisher", False).strip().lower() == "true" else False
        if not self.enabled:
            DataPublisherConfiguration.log.info("Data Publisher disabled")
            return

        DataPublisherConfiguration.log.info("Data Publisher enabled")

        self.monitoring_server_ip = CartridgeAgentConfiguration.read_property("monitoring.server.ip", False)
        if self.monitoring_server_ip.strip() == "":
            raise RuntimeError("System property not found: monitoring.server.ip")

        self.monitoring_server_port = CartridgeAgentConfiguration.read_property("monitoring.server.port", False)
        if self.monitoring_server_port.strip() == "":
            raise RuntimeError("System property not found: monitoring.server.port")

        self.monitoring_server_secure_port = CartridgeAgentConfiguration.read_property("monitoring.server.secure.port", False)
        if self.monitoring_server_secure_port.strip() == "":
            raise RuntimeError("System property not found: monitoring.server.secure.port")

        self.admin_username = CartridgeAgentConfiguration.read_property("monitoring.server.admin.username", False)
        if self.admin_username.strip() == "":
            raise RuntimeError("System property not found: monitoring.server.admin.username")

        self.admin_password = CartridgeAgentConfiguration.read_property("monitoring.server.admin.password", False)
        if self.admin_password.strip() == "":
            raise RuntimeError("System property not found: monitoring.server.admin.password")

        DataPublisherConfiguration.log.info("Data Publisher configuration initialized")