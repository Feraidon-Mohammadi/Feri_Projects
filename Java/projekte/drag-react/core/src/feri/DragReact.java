package feri;


import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;

import java.awt.*;
import java.util.ArrayList;
import java.util.Random;

public class DragReact extends ApplicationAdapter {


	ShapeRenderer shape;
	private Ball ball;
	//private ArrayList<Ball>balls;
	//private Random randomNumberGenerator;
	private Paddle paddle;
	private SpielField spiefield;

	@Override
	public void create() {
		shape = new ShapeRenderer();
		ball = new Ball ( 400, 300,20, 10,10);
		paddle = new Paddle(200, 15, 150, 10);

/*
		randomNumberGenerator = new Random();
		for (int i = 1; i <= 10; i++) {
			Ball aBall = new Ball(
					randomNumberGenerator.nextInt(Gdx.graphics.getWidth()),
					randomNumberGenerator.nextInt(Gdx.graphics.getWidth()),
					randomNumberGenerator.nextInt(100),
					randomNumberGenerator.nextInt(15),
					randomNumberGenerator.nextInt(15));
				balls.add(aBall);

		}*/
//ball = new Ball(150, 200, 70, 12, 5);
	}


	@Override
	public void render() {
		Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);
		shape.begin(ShapeRenderer.ShapeType.Filled);
		shape.setColor(Color.GOLD);


		ball.draw(shape);
		ball.update();

		//spiefield.update();



		shape.setColor(Color.BLUE);
		paddle.update();
		paddle.draw(shape);

		shape.end();

	}








}
