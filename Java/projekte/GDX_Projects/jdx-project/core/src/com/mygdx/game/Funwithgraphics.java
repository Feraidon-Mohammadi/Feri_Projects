package com.mygdx.game;


import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.utils.ScreenUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import static com.badlogic.gdx.math.MathUtils.cos;
import static com.badlogic.gdx.math.MathUtils.random;


public class Funwithgraphics extends ApplicationAdapter {


    public static ShapeRenderer shapeRenderer;
    private static final List<Color> colorPalette = List.of(Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW, Color.ORANGE);

    @Override
    public void create() {
        shapeRenderer = new ShapeRenderer();
        Random random = new Random();
        //circle1 = new Texture(Gdx.);
        //circle2 = new Texture(Gdx.files.internal());


    }

    @Override
    public void render() {
        ScreenUtils.clear(Color.BLACK);

        circle(10, 10, 25, 25, 50, 50);

//        shapeRenderer.line(0, 0, 100, 200);


        //shapeRenderer.circle((Float) anzhalElements,100,30);
        //int AnzhalElements = 0;
        //for (int x = x; x <=AnzhalElements; x += 150) {
        //     shapeRenderer.circle(x, 100, 30);}

     /*   shapeRenderer.circle((Float) anzhalElements,100,30);
        for (int x = 100; x <= (Float) anzhalElements; x += 150) {
            shapeRenderer.circle(x, 100, 30);

            for (int t = 100; t <= (Float) anzhalElements; t += 150) {
                shapeRenderer.circle(t, 250, 30);

                for (r = 100; r <= (Float) anzhalElements; r += 150) {
                    shapeRenderer.circle(r, 400, 30);

                }
            }

        }*/


        //circle1 = MathUtils.degreesToRadians(PI / 180);


    }


    public static void circle(int anzahlSpalten, int anzahlZeilen, int gap, int radius, int positionX, int positionY) {
        int distance = radius * 2 + gap;

        for (int i = 0; i < anzahlZeilen; i++) {
            int y = positionY + i * distance;
            for (int t = 0; t < anzahlSpalten; t++) {
                int x = positionX + t * distance;

                shapeRenderer.begin(ShapeRenderer.ShapeType.Line);
                // Zeichne horizontale Linie zum Vorgängerkreis.
                if (t >= 1) {
                    int preX = positionX + (t - 1) * distance;
                    shapeRenderer.setColor(Color.RED);
                    shapeRenderer.line(preX , y, x , y);
                }

                // Zeichne vertikale Linie zum Vorgängerkreis
                if (i >= 1) {
                    int preY = positionY + (i - 1) * distance;
                    shapeRenderer.setColor(Color.RED);
                    shapeRenderer.line(x, preY, x, y );
                }
                shapeRenderer.end();


            }
        }



        for (int i = 0; i < anzahlZeilen; i++) {
            int y = positionY + i * distance;
            for (int t = 0; t < anzahlSpalten; t++) {
                int x = positionX + t * distance;

                shapeRenderer.begin(ShapeRenderer.ShapeType.Filled);
                int colorIndex = MathUtils.random(0, colorPalette.size() - 1);
                shapeRenderer.setColor(colorPalette.get(colorIndex));
                shapeRenderer.circle(x, y, radius);
                shapeRenderer.end();
            }
        }

    }

}


































             /*  if( positionx == 100 || positionx == 200 || positionx == 300 || positionx == 400 || positionx == 500 ){
                    shapeRenderer.circle(positionx, positiony, radius);
                } else if(positionx < 100 || positionx > 100 || positionx <200 || positionx >200 || positionx < 300 || positionx > 300 || positionx <400 || positionx > 400 || positionx < 500 || positionx >500 ){

   */




