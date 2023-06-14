package feri;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;

public class Ball {

    public int x;
    public int y;
    private int horizontalSpeed ;
    private int verticalSpeed ;
    private int size = 20;




    public Ball(int x, int y, int radius, int horizontalSpeed, int verticalSpeed) {
        this.x = x;
        this.y = y;
        this.size = size;
        this.horizontalSpeed = horizontalSpeed;
        this.verticalSpeed = verticalSpeed;

    }
    public void update(){
        x += horizontalSpeed;
        y += verticalSpeed;
        if (x < 0 || x > Gdx.graphics.getWidth()) {
            horizontalSpeed = -horizontalSpeed;
        }
        if (y < 0 || y > Gdx.graphics.getHeight()) {
            verticalSpeed = -verticalSpeed;
        }

    }


    public void draw(ShapeRenderer shape) {
        shape.setColor(Color.GOLD);

        shape.circle(x, y, size);

        // shape.rect(reactPositionx,reactPositiony, size);


    }



}

