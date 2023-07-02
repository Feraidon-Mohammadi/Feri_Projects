package de.iad.erfurt.raindrop;

import com.badlogic.gdx.backends.lwjgl3.Lwjgl3Application;
import com.badlogic.gdx.backends.lwjgl3.Lwjgl3ApplicationConfiguration;
import de.iad.erfurt.raindrop.RainDropGame;

// Please note that on macOS your application needs to be started with the -XstartOnFirstThread JVM argument
public class DesktopLauncher {
	public static void main (String[] arg) {
		Lwjgl3ApplicationConfiguration config = new Lwjgl3ApplicationConfiguration();
		config.setForegroundFPS(60);
		config.setWindowedMode(1024, 768);
		config.setResizable(false);
		config.setTitle("Java Grundlagen - RainDrop");
		new Lwjgl3Application(new RainDropGame(), config);
	}
}
