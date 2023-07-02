package com.feri.FerisGame;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.math.Vector2;

import java.util.ArrayList;
import java.util.List;

public class Stern {

    //    float x,y,x1,y1,x2,y2;
    Color color =Color.WHITE ;

    Vector2 center;
    final float baseSize; // Basisgröße
    float size; // aktuelle Größe
    float sizeRate =MathUtils.random(.10f) ; // Änderungsrate von size
    static final float MAX_SIZE_RATIO = 2f;
    static final float MIN_SIZE_RATIO = 0.20f;






    public Stern(Vector2 center) {
        this(center, Color.WHITE, 1f);
    }

    public Stern(Vector2 center, Color color, float size) {
        this.center = center;
        this.color = color;
        this.baseSize = size;
        this.size = baseSize;
    }


    public void update() {
        size += sizeRate;
        float ratio = size / baseSize;
        if (ratio < MIN_SIZE_RATIO || ratio > MAX_SIZE_RATIO) {
            sizeRate = -sizeRate;
        }
        size = MathUtils.clamp(size, MIN_SIZE_RATIO * baseSize, MAX_SIZE_RATIO * baseSize);


    }













    public void draw(ShapeRenderer shape) {
        shape.setColor(color);
        final float offset = 1.25f * size;
        float left = center.x - size;
        float right = center.x + size;
        float top = center.y + 2 * size;
        float bottom = center.y - 2 * size;


        shape.triangle(
                center.x, top,
                left, center.y,
                right, center.y

        );
        shape.triangle(
                center.x, bottom + offset,
                left, center.y + offset,
                right, center.y + offset

        );


    }






}


