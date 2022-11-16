import pprint
import json

from py4j.java_gateway import JavaGateway

def _model_to_json(parentModelElement) -> dict():
    entry = dict()
    # Get nested packages
    entry["type"] = parentModelElement.getMetaClass()
    children = parentModelElement.getNestedElements().toList()
    if children.size()>0:
        entry["children"] = dict()
        for modelElement in children:
            if modelElement.getMetaClass() == "Package":
                print(modelElement.getMetaClass() + ": " + modelElement.getName())
                entry["children"].update({modelElement.getName():_model_to_json(modelElement)})
    return entry

try:
    gateway = JavaGateway()
    rpyAppServer = gateway.entry_point
    if rpyAppServer:
        print("Found Rhapsody Application!")
        prj = rpyAppServer.activeProject()
        pp = pprint.PrettyPrinter(indent=4)
        model = _model_to_json(prj)
        with open("model.json", "w") as outfile:
            json.dump(model, outfile, sort_keys=True, indent=4)
    else:
        print("Rhapsody Application not found!")
except Exception as e:
    print(e)