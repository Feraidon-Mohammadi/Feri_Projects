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


    Circle sun;
    Circle earth;
    Circle venus;
    Circle saturn;

    Circle ring;
    int angleRing = 0;
    int angleVelocityRing = 10;
    int distanceRingSaturn = 5;


    int angleEarth = 0;
    int angleVelocityEarth = 2;
    int angleVenus = 0;
    int angleVelocityVenus = 3;
    int angleVelocitySaturn = 1;
    int angleSaturn = 0;
    int distanceEarthSun = 100;
    int distanceVenusSun = 75;
    int distanceSaturnSun = 150;

    int rectSaturnA;


    Stern sternA;
    //Stern sternB;


    private ArrayList<Stern> stars = new ArrayList<>();

    @Override
    public void create() {


        sun = new Circle(300, 300, 20);
        sun.color = Color.ORANGE;

        earth = new Circle(300 + distanceEarthSun, 300, 12);
        earth.color = Color.GRAY;

        venus = new Circle(300 + distanceVenusSun, 300, 10);
        venus.color = Color.LIGHT_GRAY;

        saturn = new Circle(400 + distanceEarthSun, 400, 12);
        saturn.color = Color.OLIVE;
        shape = new ShapeRenderer();


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
        earth.draw(shape);
        venus.draw(shape);

        saturn.draw(shape);
        //ring.draw(shape);

        //sternB.draw(shape);


        shape.end();

        angleEarth += angleVelocityEarth;
        angleEarth %= 360;

        angleVenus += angleVelocityVenus;
        angleVenus %= 360;



        earth.x = sun.x + distanceEarthSun * Math.cos(toRadians(angleEarth));
        earth.y = sun.y + distanceEarthSun * Math.sin(toRadians(angleEarth));



        venus.x = sun.x + distanceVenusSun * Math.cos(toRadians(angleVenus));
        venus.y = sun.y + distanceVenusSun * Math.sin(toRadians(angleVenus));









        angleSaturn += angleVelocitySaturn;
        angleSaturn %= 360;

        saturn.x = sun.x + distanceSaturnSun * Math.cos(toRadians(angleSaturn));
        saturn.y = sun.y + distanceSaturnSun * Math.sin(toRadians(angleSaturn));
        //angleSaturn += angleSaturn;

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
