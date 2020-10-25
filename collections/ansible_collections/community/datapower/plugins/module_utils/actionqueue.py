#PUT actionqueue help code here

def quiesce(timeout):
    return { "QuiesceDP" :{ "timeout" : timeout }}

def unquiesce():
    return { "UnquiesceDP" : { }}

def save_config():
    return { "SaveConfig" : {}}

def tcp_connection_test(remote_host, remote_port):
    return { "TCPConnectionTest" :{"RemoteHost" : remote_host,"RemotePort" : remote_port}}