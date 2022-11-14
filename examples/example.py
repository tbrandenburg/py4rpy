# py4j is mainly used to improve performance by loading java class and Eclipse
# CDT only once
from py4j.java_gateway import JavaGateway

try:
    gateway = JavaGateway()
    rpyAppServer = gateway.entry_point
    if rpyAppServer:
        print("Found Rhapsody Application!")
        prj = rpyAppServer.activeProject()
        if prj:
            print("Found Rhapsody Project \"" + prj.getName() + "\"")
        else:
            print("Rhapsody Project not found!")
    else:
        print("Rhapsody Application not found!")
except Exception as e:
    print(e)