package de.iad.erfurt.raindrop;


import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.utils.ScreenUtils;


import java.util.ArrayList;
import java.util.Iterator;


public class RainDropGame extends ApplicationAdapter {

    private Texture bucket;

    public Texture droplet;
    private SpriteBatch spriteBatch;

    private float bucketX;
    private float bucketY;

    private float bucketVelocity = 700;

    private ArrayList<Point> dropletPositions; // ganz wichtig  . diese liste muss auch mit eine methode geloscht werden  unnotige regentropfen wegen speicher platz .

    private float dropIntervalInSeconds = 0.5f; // Alle 500ms wird ein neuer Regentropfen erzeugt.

    private int dropletVelocityInPixels = 200;

    private float elapsedTimeSinceLastDrop = dropIntervalInSeconds; // Verstreichen zeit seit Erzeugung des letzten Regentropfen

    private int score = 0;

    private BitmapFont baseFont;



    @Override
    public void create() {
        baseFont = new BitmapFont();


        spriteBatch = new SpriteBatch();
        // dade die bucket.png Datei und die droplet.png aus dem Assets-Verzeichnis.
        bucket = new Texture(Gdx.files.internal("bucket.png"));
        droplet = new Texture(Gdx.files.internal("droplet.png"));
        bucketY = 0; // Y bucket upper

        dropletPositions = new ArrayList<Point>();

    }


    @Override
    public void render() {
        // background  color
        ScreenUtils.clear(Color.BLUE);


        spriteBatch.begin();
        spriteBatch.draw(bucket, bucketX, bucketY);

        for(Point dropletPosition : dropletPositions){
            spriteBatch.draw(droplet, dropletPosition.x , dropletPosition.y);
        }

        baseFont.draw(spriteBatch, "Score: %02d".formatted(score), 0, Gdx.graphics.getHeight());

        spriteBatch.end();


        if (Gdx.input.isKeyPressed(Input.Keys.RIGHT)){
            bucketX += bucketVelocity * Gdx.graphics.getDeltaTime();
        } else if(Gdx.input.isKeyPressed(Input.Keys.LEFT)){
            bucketX -= bucketVelocity * Gdx.graphics.getDeltaTime();
        }

        // sicherstellen , dass sich das bucket nicht außerhalb des fenster befindet
        //
        bucketX = MathUtils.clamp(bucketX, 0, Gdx.graphics.getWidth() - bucket.getWidth());


        //
        for(Point dropletPosition : dropletPositions){
            dropletPosition.y -= dropletVelocityInPixels * Gdx.graphics.getDeltaTime();
        }

        // prüfe ,ob ein neuer Regentropgen zu erzeugen ist.
       elapsedTimeSinceLastDrop += Gdx.graphics.getDeltaTime();
       if(elapsedTimeSinceLastDrop >= dropIntervalInSeconds){
           elapsedTimeSinceLastDrop = 0;
           int dropletX = MathUtils.random(0 , Gdx.graphics.getWidth() - droplet.getWidth());
           dropletPositions.add(new Point(dropletX, Gdx.graphics.getHeight()));
       }


       //entferne Regentropfen,
        Iterator<Point> interator = dropletPositions.iterator();
       while(interator.hasNext()){
           Point dropletPosition = interator.next();
           if(dropletPosition.y < -droplet.getHeight()){
               interator.remove();
           }
           // Kollidiert eine Regentropfen mit dem Bucket, wird
           if(doIntersect(new Point(bucketX, bucketY), dropletPosition, bucket.getWidth(), droplet.getWidth(),
                   bucket.getHeight(), droplet.getHeight())){
               score++;
               interator.remove();
           }
       }





        System.out.println(dropletPositions.size());



        //
       /* for (Point dropletPosition : dropletPositions){
            if (dropletPosition.y <= -droplet.getHeight()){
                dropletPosition.remove(dropletPosition);
            }
        }
*/


    }


    // prüfe ob sich techteecke A und B pberschneiden
    // Annahme: A und B sind nicht rotiert , d.h  die kanten laufen parallel zu dne koordinatenachsen.
    private  boolean doIntersect(Point positionOfA, Point positionOfB , int widthOfA, int widthOfB, int heightOfA, int heightOfB){
        float topOfA = positionOfA.y + heightOfA; // top = Oberkante
        float rightOfA = positionOfA.x + widthOfA; // right = rechte kante
        float topOFB = positionOfB.y+ heightOfB;
        float rightOfB = positionOfB.x + widthOfB;
        return topOFB >= positionOfA.y
                && positionOfB.y <= topOfA
                && rightOfB >= positionOfA.x
                && positionOfB.x <= rightOfA;
    }

}
