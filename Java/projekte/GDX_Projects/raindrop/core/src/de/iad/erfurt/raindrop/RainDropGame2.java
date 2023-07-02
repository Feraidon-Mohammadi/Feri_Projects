package de.iad.erfurt.raindrop;


import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.utils.ScreenUtils;
import java.awt.event.WindowAdapter;




public class RainDropGame2 extends ApplicationAdapter {

    private Texture bucket;

    public Texture droplet;
    private SpriteBatch spriteBatch;

    private float bucketX;
    private float bucketY;

    public float dropletX;
    public float dropletY;

    private float bucketvelocity = 100;// 100 pixel pro Sekunde
    private float bucketOffsetAngle= 0; // winkel in grad
    private float bucketOffsetVelocity = 360; // 360 grad pro sekunde




    @Override
    public void create() {
        spriteBatch = new SpriteBatch();
        // dade die bucket.png Datei und die droplet.png aus dem Assets-Verzeichnis.
        bucket = new Texture(Gdx.files.internal("bucket.png"));
        droplet = new Texture(Gdx.files.internal("droplet.png"));
        bucketY = 100; // Y bucket upper



    }

    @Override
    public void render() {
        // background  color
        ScreenUtils.clear(Color.BLUE);




        // umwandlung von Grad in Radianten
        double angleInTadians = bucketOffsetAngle / 180.0f * Math.PI;
        double offset = Math.sin(2* angleInTadians) * 100;



        spriteBatch.begin();
        spriteBatch.draw(bucket, bucketX , (float) (bucketY +offset));
        spriteBatch.end();


        bucketOffsetAngle += bucketOffsetVelocity * Gdx.graphics.getDeltaTime();
        bucketOffsetAngle %= 360.0;


        bucketX += bucketvelocity * Gdx.graphics.getDeltaTime();

        float windowWidth = Gdx.graphics.getWidth();
        if(bucketX <=0){
            bucketX = 0;
            bucketvelocity = -bucketvelocity;
        } else if (bucketX >= windowWidth - bucket.getWidth()){
            bucketX = windowWidth -bucket.getWidth();
            bucketvelocity = -bucketvelocity;
        }







        float mouseX = Gdx.input.getX();
        //float mouseX = Gdx.input.getY();
        //bucketX = mouseX;
        // bucketX = mouseX;


// regnet
        spriteBatch.begin();
        spriteBatch.draw(droplet, dropletX+0, dropletY +500);
        dropletY--;
        spriteBatch.end();

        spriteBatch.begin();
        spriteBatch.draw(droplet, dropletX+100, dropletY +400);
        dropletY--;
        spriteBatch.end();







        float time = Gdx.graphics.getDeltaTime();








        for(float i = 0; i < windowWidth; i++){
        }










    }



    /*   for ( droplet) {
            if(droplet < windowWidth){
                spriteBatch.begin();
                spriteBatch.draw(droplet, dropletX+100, dropletY-200);
                dropletY--;
                spriteBatch.end();
            }
            dropletX++;
        }
*/





       /* for(int i = 0; i < windowWidth; i++ ){
            float droplet = 0;
            if(droplet <= windowWidth ){
            }
        }
        */



}
