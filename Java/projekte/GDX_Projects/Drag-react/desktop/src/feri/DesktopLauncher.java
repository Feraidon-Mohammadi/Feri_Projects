package feri;



import com.badlogic.gdx.backends.lwjgl3.Lwjgl3Application;
import com.badlogic.gdx.backends.lwjgl3.Lwjgl3ApplicationConfiguration;
import org.lwjgl.glfw.GLFW;

import java.awt.*;







// Please note that on macOS your application needs to be started with the -XstartOnFirstThread JVM argument
public class DesktopLauncher {
	public static void main (String[] arg) {
		Lwjgl3ApplicationConfiguration config = new Lwjgl3ApplicationConfiguration();
		config.setForegroundFPS(60);
		config.setWindowedMode(1024, 768);
		config.setTitle("drag-react");
		new Lwjgl3Application(new DragReact(), config);



	/*

		// Create the application
		DragReact application = new DragReact();
		Lwjgl3Application applicationWindow = new Lwjgl3Application(application, config);

		// Get the reference to the application's window
		long windowHandle = applicationWindow.getWindow().getHandle();

		// Get the screen width and height
		int screenWidth = GLFW.glfwGetVideoMode(GLFW.glfwGetPrimaryMonitor()).width();
		int screenHeight = GLFW.glfwGetVideoMode(GLFW.glfwGetPrimaryMonitor()).height();

		// Set the desired position of the application's window (top-right corner)
		int desiredX = screenWidth - config.getBackBufferWidth();  // X-coordinate in pixels
		int desiredY = screenHeight - config.getBackBufferHeight();  // Y-coordinate in pixels

		// Set the position of the application's window
		GLFW.glfwSetWindowPos(windowHandle, 300, 500);

config.setWindowPosition(100, 400);
		config.setWindowedMode(800, 600);
		config.setResizable(false);
	*/

	}
}





















