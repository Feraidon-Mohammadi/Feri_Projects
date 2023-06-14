package com.feri;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.badlogic.gdx.utils.ScreenUtils;

public class FerisGame extends ApplicationAdapter {
    ShapeRenderer shapeRenderer;
    Circle sun;
    Circle earth;
    Circle venus;
    Circle saturn;
    int angleEarth =0;
    int angleVelocityEarth = 2;
    int angleVenus = 0;
    int angleVelocityVenus = 3;
    int angleVelocitySaturn = 1;
    int angleSaturn = 0;
    int distanceEarthSun = 200;
    int distanceVenusSun = 150;
    int distanceSaturnSun = 300;

    int rectSaturnA ;


    @Override
    public void create() {
        sun = new Circle(300, 300, 100);
        sun.color = Color.ORANGE;

        earth = new Circle(300 + distanceEarthSun, 300, 12);
        earth.color = Color.BLUE;

        venus = new Circle(300 + distanceVenusSun,300,10);
        venus.color = Color.LIGHT_GRAY;

        saturn = new Circle(400 + distanceEarthSun, 400, 12);
        saturn.color = Color.BLUE;
        shapeRenderer = new ShapeRenderer();
    }

    @Override
    public void render() {
        ScreenUtils.clear(Color.BLACK);
        shapeRenderer.begin(ShapeRenderer.ShapeType.Filled);
//        Circle.color = Color.WHITE;
        sun.draw(shapeRenderer);
//        Circle.color = Color.MAGENTA;
        earth.draw(shapeRenderer);
        venus.draw(shapeRenderer);
        saturn.draw(shapeRenderer);

        shapeRenderer.end();

        angleEarth += angleVelocityEarth;
        angleEarth %= 360;

        angleVenus += angleVelocityVenus;
        angleVenus %= 360;

        angleSaturn += angleVelocitySaturn;
        angleSaturn %= 360;

        earth.x = sun.x + distanceEarthSun * Math.cos(toRadians(angleEarth));
        earth.y = sun.y + distanceEarthSun * Math.sin(toRadians(angleEarth));

        venus.x=sun.x + distanceVenusSun * Math.cos(toRadians(angleVenus));
        venus.y=sun.y + distanceVenusSun *Math.sin(toRadians(angleVenus));

        saturn.x = sun.x + distanceSaturnSun * Math.cos(toRadians(angleSaturn));
        saturn.y = sun.y + distanceSaturnSun * Math.sin(toRadians(angleSaturn));
    }

    private static double toRadians(double angle) {
        return angle / 180 * Math.PI;
    }


}
