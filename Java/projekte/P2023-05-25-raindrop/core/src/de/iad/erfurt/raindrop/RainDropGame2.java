package de.iad.erfurt.raindrop;


import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.utils.ScreenUtils;

public class RainDropGame2 extends ApplicationAdapter {

    private Texture bucket;
    private Texture droplet;

    private SpriteBatch spriteBatch;

    private float bucketX;
    private float bucketY;
    private float bucketOffsetAngle = 0; // Winkel in Grad
    private float bucketVelocity = 200; // 200 Pixel pro Sekunde
    private float bucketOffsetVelocity = 360; // 360 Grad pro Sekunde

    @Override
    public void create() {
        spriteBatch = new SpriteBatch();
        // Lade die bucket.png Datei und die droplet.png aus dem Assets-Verzeichnis.
        bucket = new Texture(Gdx.files.internal("bucket.png"));
        droplet = new Texture(Gdx.files.internal("droplet.png"));
        bucketY = 150;
    }

    @Override
    public void render() {
        ScreenUtils.clear(Color.BLUE);

        // Umwandlung von Grad in Radianten
        double angleInRadians = bucketOffsetAngle / 180.0f * Math.PI;
        // Berechnung des Offsets in y-Richtung
        double offset = Math.sin(0.5f * angleInRadians) * 100;



        spriteBatch.begin();
        spriteBatch.draw(bucket, bucketX, (float)(bucketY + offset));
        spriteBatch.end();

        // Winkel erhöhen, um den Versatz in y-Richtung zu verändern.
        bucketOffsetAngle += bucketOffsetVelocity * Gdx.graphics.getDeltaTime();
        bucketOffsetAngle %= 360.0;
        // Verschiebe das Bucket in x-Richtung
        bucketX += bucketVelocity * Gdx.graphics.getDeltaTime();
        // Verschiebe das Bucket in y-Richtung


        // Prüfe ob das Bucket einen Schwellwert erreicht hat und drehe entsprechend die
        // Bewegungsrichtung um.
        float windowWidth = Gdx.graphics.getWidth();
        if (bucketX <= 0) {
            bucketX = 0;
            bucketVelocity = -bucketVelocity;
        } else if (bucketX >= windowWidth - bucket.getWidth()) {
            bucketX = windowWidth - bucket.getWidth();
            bucketVelocity = -bucketVelocity;
        }


    }
}
