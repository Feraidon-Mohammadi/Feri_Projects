package feri;


import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;

public class SpielField {
   /* int x ;
    int y;
    int size = 15;
    int left ;
    int right ;
    int top;
    int down;*/
    ShapeRenderer shape;


    public void Field ( ){
     /*   this.x = x;
        this.y = y;

        this.size = size;
        this.down = down;
        this.top = top;
        this.left = left;
        this.right = right;*/

    }


/*
    public void SpielField(int left, int right, int up, int down,int width, int height) {
          //int swedth = Gdx.graphics.getWidth();
         //shape.rect(4,1000,3,3);
        // height = Gdx.graphics.getHeight();
       // width = Gdx.graphics.getWidth();
    }
    */



    public void update() {



    }
    public void rectField(ShapeRenderer shape){

        int height = Gdx.graphics.getHeight();
        int width = Gdx.graphics.getWidth();
        int widthMinus = Gdx.graphics.getWidth()-10;
        //int heightMinus = Gdx.graphics.getHeight()-5;


        shape.setColor(Color.OLIVE);
        //down field
        shape.rect(1, 1, width, 12);
        // top field
        shape.rect(10, height -10, width, 12);
        //left field
        shape.rect(1, 1, 12, 1000);
        // right field
        shape.rect(widthMinus, 1,  10, height );



    }


}
