package tb.py4rpy;

import com.telelogic.rhapsody.core.IRPApplication;
import com.telelogic.rhapsody.core.RhapsodyAppServer;

import py4j.GatewayServer;

public class Py4Rpy {
    public static void main(String[] args) {
        IRPApplication app = null;

        System.out.println("Waiting for Rhapsody...");

        // Wait for app
        while(app == null) {
            try {
                app = RhapsodyAppServer.getActiveRhapsodyApplication();
            } catch(Exception e) {
                app = null;
            }
        }

        GatewayServer gatewayServer = new GatewayServer(app);
        gatewayServer.start();

        System.out.println("py4rpy gateway started!");
    }
}