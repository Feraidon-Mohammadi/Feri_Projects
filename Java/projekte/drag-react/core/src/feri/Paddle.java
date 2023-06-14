package feri;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.badlogic.gdx.scenes.scene2d.ui.Window;
import com.badlogic.gdx.utils.ScreenUtils;

public class Paddle {
    private int x;
    private int y;
    private int width;
    private int height;
    ShapeRenderer shape;


    public Paddle(int x, int y , int width, int height){
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;


    }
    public void update(){



        int screenWidth = Gdx.graphics.getWidth();
        int screenHeight = Gdx.graphics.getHeight();

        x += Gdx.input.getX();
        if (x > 0 ) {
            x = Gdx.input.getX() - width /2;
        }
        if(Gdx.input.getX() < 0){
            x = screenWidth /2;
            y = screenHeight /2;
        }
        if(Gdx.input.getX() < 0){

        }










    }


    public void draw(ShapeRenderer shape) {


            shape.rect(x,y,width,height);



    }



}
