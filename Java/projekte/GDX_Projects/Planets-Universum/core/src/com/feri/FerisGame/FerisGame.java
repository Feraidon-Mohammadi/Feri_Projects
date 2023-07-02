package com.feri.FerisGame;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.utils.ScreenUtils;

import java.util.ArrayList;

import static com.badlogic.gdx.math.MathUtils.random;

public class FerisGame extends ApplicationAdapter {
    ShapeRenderer shape;


    Circle sun;  ///
    Circle mercury;
    Circle venus; ///
    Circle earth; ///
    Circle mars;
    Circle jupiter;
    Circle saturn; ///
    Circle uranus;
    Circle neptune;

    Circle ring;
    //int angleRing = 0;
    int angleVelocityRing = 5;


    double angleVelocityMercury= 1.4;
    double angleVelocityVenus = 1.2;
    double angleVelocityEarth = 0.9;
    double angleVelocityMars = 0.70;
    double angleVelocityJupiter = 0.50;
    double angleVelocitySaturn = 0.4;
    double angleVelocityUranus = 0.20;
    double angleVelocityNeptune = 0.10;



    double angleMercury = 0;
    double angleVenus = 0;
    double angleEarth = 0;
    double angleMars = 0;
    double angleJupiter = 0;
    double angleSaturn = 0;
    double angleUranus = 0;
    double angleNeptune = 0;


    double distanceMercurySun = 50;
    //int distanceRingSaturn = 60;
    double distanceVenusSun = 75;
    double distanceEarthSun = 100;
    double distanceMarsSun = 125;
    double distanceJupiterSun = 150;
    double distanceSaturnSun = 175;
    double distanceUranusSun = 200;
    double distanceNeptuneSun = 225;

    int rectSaturnA;


    Stern sternA;
    //Stern sternB;


    private ArrayList<Stern> stars = new ArrayList<>();

    @Override
    public void create() {


        sun = new Circle(300, 250, 20);
        sun.color = Color.GOLDENROD;


        mercury = new Circle((int) (300 + distanceMercurySun), 300, 7);
        mercury.color = Color.RED;


        venus = new Circle((int) (300 + distanceVenusSun), 300, 8);
        venus.color = Color.BLUE;


        earth = new Circle((int) (300 + distanceEarthSun), 300, 9);
        earth.color = Color.WHITE;


        mars = new Circle((int) (300 + distanceMarsSun), 300, 8);
        mars.color = Color.MAGENTA;


        jupiter = new Circle((int) (300 + distanceJupiterSun), 300, 15);
        jupiter.color = Color.BROWN;


        saturn = new Circle((int)(400 + distanceEarthSun), 400, 9);
        saturn.color = Color.GREEN;
        shape = new ShapeRenderer();


        uranus = new Circle((int) (300 + distanceUranusSun), 300, 10);
        uranus.color = Color.YELLOW;


        neptune = new Circle((int) (300 + distanceNeptuneSun), 300, 6);
        neptune.color = Color.PINK;








        sternA = new Stern(new Vector2(500, 300), Color.GOLD, 3f);
        sternA.sizeRate = 0.25f;

        ring  = new Circle(100, 100, 10);
        //sternB = new Stern(new Vector2(550, 320), Color.WHITE, 30f);
//        sternC = new Stern(230,20,50,40,150,75);
//        sternD = new Stern(230,20,50,40,150,75);
//        sternA.color=Color.LIGHT_GRAY;

        // Erzeuge 100 Sterne mit zufälligen Positionen. Füge jedes neue Stern-Objekt zur Liste stars hinzu.



            for (int i = 0; i < 200; i++){

                int  x = random(800 );
                int  y = random(800);
                Stern newStar = new Stern(new Vector2(x,y));
                stars.add(newStar);
            }


        //ArrayList(int stern)



    }

    @Override
    public void render() {




        for (Stern s : stars) {
            s.update();
        }


        //sternB.update();


        //shapeRenderer.triangle(float x, float x, float x1, float x1, float x2, float x2);
        ScreenUtils.clear(Color.BLACK);
        shape.begin(ShapeRenderer.ShapeType.Filled);


        for (Stern s : stars) {



            double red = random.nextDouble();
            double green = random.nextDouble();
            double blue = random.nextDouble();
            double white = random.nextDouble();

            // Create a new Color object with the random RGB values
            Color randomColor = new Color((float) red, (float) green, (float) blue,10);

            // Set the random color for the current star
            s.color.set(randomColor.r, randomColor.g,randomColor.b,randomColor.a); //.setColor(randomColor);
            s.draw(shape);
        }




//       Circle.color = Color.WHITE;
        sun.draw(shape);
//        Circle.color = Color.MAGENTA;
        mercury.draw(shape);
        venus.draw(shape);
        earth.draw(shape);
        mars.draw(shape);
        jupiter.draw(shape);
        saturn.draw(shape);
        uranus.draw(shape);
        neptune.draw(shape);
        //ring.draw(shape);

        //sternB.draw(shape);


        shape.end();

        angleMercury += angleVelocityMercury;
        angleMercury %= 360;
        mercury.x = sun.x + distanceMercurySun * Math.cos(toRadians(angleMercury));
        mercury.y = sun.y + distanceMercurySun * Math.sin(toRadians(angleMercury));


        angleVenus += angleVelocityVenus;
        angleVenus %= 360;
        venus.x = sun.x + distanceVenusSun * Math.cos(toRadians(angleVenus));
        venus.y = sun.y + distanceVenusSun * Math.sin(toRadians(angleVenus));



        angleEarth += angleVelocityEarth;
        angleEarth %= 360;
        earth.x = sun.x + distanceEarthSun * Math.cos(toRadians(angleEarth));
        earth.y = sun.y + distanceEarthSun * Math.sin(toRadians(angleEarth));


        angleMars += angleVelocityMars;
        angleMars %= 360;
        mars.x = sun.x + distanceMarsSun * Math.cos(toRadians(angleMars));
        mars.y = sun.y + distanceMarsSun * Math.sin(toRadians(angleMars));


        angleJupiter += angleVelocityJupiter;
        angleJupiter %= 360;
        jupiter.x = sun.x + distanceJupiterSun * Math.cos(toRadians(angleJupiter));
        jupiter.y = sun.y + distanceJupiterSun * Math.sin(toRadians(angleJupiter));


        angleSaturn += angleVelocitySaturn;
        angleSaturn %= 360;
        saturn.x = sun.x + distanceSaturnSun * Math.cos(toRadians(angleSaturn));
        saturn.y = sun.y + distanceSaturnSun * Math.sin(toRadians(angleSaturn));
        //angleSaturn += angleSaturn;


        angleUranus += angleVelocityUranus;//
        angleEarth %= 360;
        uranus.x = sun.x + distanceUranusSun * Math.cos(toRadians(angleUranus));
        uranus.y = sun.y + distanceUranusSun * Math.sin(toRadians(angleUranus));


        angleNeptune += angleVelocityNeptune;//
        angleNeptune %= 360;
        neptune.x = sun.x + distanceNeptuneSun * Math.cos(toRadians(angleNeptune));
        neptune.y = sun.y + distanceNeptuneSun * Math.sin(toRadians(angleNeptune));



/*
        angleRing += angleVelocityRing;
        angleRing %= 360;
        ring.x = saturn.x + distanceRingSaturn * Math.cos(toRadians(angleRing));
        ring.y = saturn.y + distanceRingSaturn * Math.sin(toRadians(angleRing));
        //angleRing += angleVelocityRing;
*/




    }

    private static double toRadians(double angle) {
        return angle / 180 * Math.PI;
    }


}
