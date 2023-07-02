package com.mygdx.game;

import com.badlogic.gdx.backends.lwjgl3.Lwjgl3Application;
import com.badlogic.gdx.backends.lwjgl3.Lwjgl3ApplicationConfiguration;
import com.mygdx.game.Funwithgraphics;

// Please note that on macOS your application needs to be started with the -XstartOnFirstThread JVM argument
public class DesktopLauncher {
	public static void main (String[] arg) {
		Lwjgl3ApplicationConfiguration config = new Lwjgl3ApplicationConfiguration();
		config.setForegroundFPS(60);
		config.setTitle("Funwithgraphics");
		config.setWindowedMode(1024, 768);
		new Lwjgl3Application(new Funwithgraphics(), config);


		//System.out.println(Funwithgraphics.drawCircles(3,3,100,25,100,100));

	}
}
