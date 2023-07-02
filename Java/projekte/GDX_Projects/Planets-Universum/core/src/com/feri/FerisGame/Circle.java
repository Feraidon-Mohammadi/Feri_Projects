package com.feri.FerisGame;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;

public class Circle {
    double x,y,radius;
// static Color color = Color.YELLOW;
    Color color;

    public Circle(int x,int y, int radius){
        this.x=x;
        this.y=y;
        this.radius=radius;
    }


    public void draw(ShapeRenderer shapeRenderer){
        shapeRenderer.setColor(color);
        shapeRenderer.circle((float)x,(float)y,(float)radius);

    }
}
