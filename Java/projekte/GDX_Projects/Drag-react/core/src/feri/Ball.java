package feri;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;




public class Ball {

    public int x;
    public int y;
    private int xSpeed;
    private int ySpeed =30;
    private int size = 20;
    Color color = Color.WHITE;




    public Ball(int x, int y, int radius, int ySpeed, int xSpeed) {

        this.x = x;
        this.y = y;
        this.size = size;
    

    }
    public void update(){
        x += xSpeed;
        y += ySpeed;
        if (x < 0 || x > Gdx.graphics.getWidth()) {
            xSpeed = -xSpeed;
        }
        if (y < 0 || y > Gdx.graphics.getHeight()) {
            ySpeed = -ySpeed;
        }
    }


    public void draw(ShapeRenderer shape) {
        shape.setColor(Color.GOLD);
        shape.circle(x, y, size);
    }

    


    private boolean collidesWith(Paddle paddle) {
        int paddleLeft = paddle.x;
        int paddleRight = paddle.x + paddle.width;
        int paddleTop = paddle.y ;
        int paddleDown = paddle.y + paddle.height;

        if( x >= paddleLeft && x <= paddleRight && y <= paddleDown && y >= paddleTop){
            return true;
        }
        return false;
    }

    private boolean collidesWith(Block block) {
      /*  int paddleLeft = block.x;
        int paddleRight = block.x + block.width;
        int paddleTop = block.y ;
        int paddleDown = block.y + block.height;

        if( x >= paddleLeft && x <= paddleRight && y <= paddleDown && y >= paddleTop){
            return true;
        }*/
        return false;
    }


    public void checkCollision(Paddle paddle) {
        if(collidesWith(paddle)){
             ySpeed = -ySpeed;

        }
    }

    public void checkCollision(Block block) {
        if (collidesWith(block)) {
            ySpeed -= ySpeed;
            block.destroyed = true;
        }
    }



}

