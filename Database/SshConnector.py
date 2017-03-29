import logging
from sshtunnel import SSHTunnelForwarder


class SshConnector:
    """
    Klasa obsługująca połączenie po ssh -> może być np potrzebne jeśli musimy najpierw się połączyć po ssh z serwerem,
    na którym stoi nasza baza danych.
    Jak w przypadku połączenia do bazy danych -> połączenie trzymamy jak najkrócej.
    Przykładowe użycie:
    sshConnection = SshConnector("192.10.10.10", "user", "password")
    sshConnection.startTunneling()
    sshConnection.stopTunneling()
    """

    def __init__(self, ipAddress, username, password):
        self.sshTunnel = SSHTunnelForwarder(ssh_address_or_host=ipAddress,
                                            ssh_username=username, ssh_password=password,
                                            remote_bind_address=('127.0.0.1', 3306),
                                            local_bind_address=('127.0.0.1', 3306))

    def startTunneling(self):
        logging.info('Establishing tunnel')
        self.sshTunnel.start()
        logging.info('Tunnel established')

    def stopTunneling(self):
        logging.info('Stopping tunnel')
        self.sshTunnel.stop()
        logging.info('Tunnel stopped')



