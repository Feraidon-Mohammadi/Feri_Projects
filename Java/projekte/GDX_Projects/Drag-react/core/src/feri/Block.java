package feri;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;



public class Block {
    public boolean destroyed;
    int x,y ,width,height;
     ShapeRenderer shape;
    public Block(int x, int y, int width, int height) {

        this.x = x;
        this.y = y;
        this.height = height;
        this.width = width;
    }


    public void draw(ShapeRenderer shape) {

        shape.setColor(Color.PURPLE);
        shape.rect(x,y ,width, height);

/*
        int width = Gdx.graphics.getWidth();
        int heigth = Gdx.graphics.getHeight();

        List<String> blocks = new ArrayList<>();
        int[] anzahlSplaten = new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        int[] anzahlZeilen = new int[]{0,0,0,0,0,0};
        for(int i = 0 ; i < anzahlSplaten.length ; i++) {
            shape.setColor(Color.WHITE);
            shape.rect(width - heigth - 230, heigth - 50, 60, 30);
            String shapeString = shape.toString();
            blocks.add(shapeString);

            for (String block : blocks) {
            }

            }
       */
    }

    public void destroyed(){
        destroyed = true;

    }
}
