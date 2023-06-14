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
    private Texture droplet;

    private SpriteBatch spriteBatch;
    private BitmapFont baseFont;

    private float bucketX;
    private float bucketY;
    private float bucketVelocity = 200;

    private ArrayList<Point> dropletPositions;
    private float dropIntervalInSeconds = 0.5f; // Alle 500ms wird ein neuer Regentropfen erzeugt.
    private int dropletVelocityInPixels = 200; // 200 Pixel pro Sekunde
    private float elapsedSecondsSinceLastDrop = dropIntervalInSeconds; // Verstrichene Zeit seit Erzeugung des letzten Regentropfens.

    private int score = 0;

    @Override
    public void create() {
        spriteBatch = new SpriteBatch();
        baseFont = new BitmapFont();
        // Lade die bucket.png Datei und die droplet.png aus dem Assets-Verzeichnis.
        bucket = new Texture(Gdx.files.internal("bucket.png"));
        droplet = new Texture(Gdx.files.internal("droplet.png"));
        bucketY = 0;
        dropletPositions = new ArrayList<Point>();
    }

    @Override
    public void render() {
        ScreenUtils.clear(Color.BLUE);

        spriteBatch.begin();
        spriteBatch.draw(bucket, bucketX, bucketY);
        for (Point dropletPosition : dropletPositions) {
            spriteBatch.draw(droplet, dropletPosition.x, dropletPosition.y);
        }
        baseFont.setColor(Color.WHITE);
        baseFont.draw(spriteBatch, "Score: %02d".formatted(score), 0, Gdx.graphics.getHeight());
        spriteBatch.end();

        if (Gdx.input.isKeyPressed(Input.Keys.RIGHT)) {
            bucketX += bucketVelocity * Gdx.graphics.getDeltaTime();
        } else if (Gdx.input.isKeyPressed(Input.Keys.LEFT)) {
            bucketX -= bucketVelocity * Gdx.graphics.getDeltaTime();
        }

        // Sicherstellen, dass sich das Bucket nicht außerhalb des Fensters befindet.
        // Die clamp Funktion sorgt dafür, dass sich bucketX im Intervall 0 bis Fensterbreite-Bucketbreite befindet.
        bucketX = MathUtils.clamp(bucketX, 0, Gdx.graphics.getWidth() - bucket.getWidth());

        // Vorhandene Regentropfen nach unten bewegen.
        for (Point dropletPosition : dropletPositions) {
            dropletPosition.y -= dropletVelocityInPixels * Gdx.graphics.getDeltaTime();
        }

        // Prüfe, ob ein neuer Regentropfen zu erzeugen ist.
        elapsedSecondsSinceLastDrop += Gdx.graphics.getDeltaTime();
        if (elapsedSecondsSinceLastDrop >= dropIntervalInSeconds) {
            elapsedSecondsSinceLastDrop = 0;
            int dropletX = MathUtils.random(0, Gdx.graphics.getWidth() - droplet.getWidth());
            dropletPositions.add(new Point(dropletX, Gdx.graphics.getHeight()));
        }

        // Entferne Regentropfen, die sich aus dem Fenster herausbewegt haben.
        Iterator<Point> iterator = dropletPositions.iterator();
        while (iterator.hasNext()) {
            Point dropletPosition = iterator.next();
            if (dropletPosition.y < -droplet.getHeight()) {
                iterator.remove();
                continue;
            }
            // Kollidiert ein Regentropfen mit dem Bucket, wird der Regentropfen ebenfalls entfernt.
            if (doIntersect(new Point(bucketX, bucketY), dropletPosition, bucket.getWidth(), droplet.getWidth(),
                    bucket.getHeight(), droplet.getHeight())) {
                score++;
                iterator.remove();
            }
        }

    }

    // Prüfe, ob sich die Rechtecke A und B überschneiden.
    // Annahme: A und B sind nicht rotiert, d.h. die Kanten laufen parallel zu den Koordinatenachsen.
    private boolean doIntersect(Point positionOfA, Point positionOfB, int widthOfA, int widthOfB, int heightOfA, int heightOfB) {
        float topOfA = positionOfA.y + heightOfA; // top = Oberkante
        float rightOfA = positionOfA.x + widthOfA; // right = Rechte Kante
        float topOfB = positionOfB.y + heightOfB;
        float rightOfB = positionOfB.x + widthOfB;
        return topOfB >= positionOfA.y
                && positionOfB.y <= topOfA
                && rightOfB >= positionOfA.x
                && positionOfB.x <= rightOfA;
    }
}
