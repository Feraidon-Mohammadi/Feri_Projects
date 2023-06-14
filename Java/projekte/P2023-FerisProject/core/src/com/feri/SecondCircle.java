package com.feri;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;

public class SecondCircle {
        int x1,y1,radius1;



    public SecondCircle(int x1, int y1, int radius1){

            this.x1=x1;
            this.y1=y1;
            this.radius1=radius1;

        }

        public void draw(ShapeRenderer shapeRenderer){
            shapeRenderer.setColor(Color.YELLOW);
            shapeRenderer.circle(x1,y1,radius1);

        }
}
