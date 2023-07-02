package feri;


import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;

import java.util.ArrayList;



public class DragReact extends ApplicationAdapter {


	ShapeRenderer shape;
	private Ball ball;
	//private ArrayList<Ball>balls;
	//private Random randomNumberGenerator;
	private Paddle paddle;
	private SpielField spielfield;
	private Block block;

	ArrayList<Block> blocks = new ArrayList<>();

	@Override
	public void create() {
		shape = new ShapeRenderer();
		ball = new Ball ( 400, 300,20, 10,10);
		paddle = new Paddle(200, 15, 150, 10);
		spielfield = new SpielField();


		int blockwidth = 63;
		int blockheight = 20;


		for (int x = 20; x < Gdx.graphics.getWidth() - blockwidth; x += blockwidth +14 ) {
			for(int y = Gdx.graphics.getHeight() / 2; y < Gdx.graphics.getHeight() - blockheight; y += blockheight +14){
				blocks.add(new Block(x, y, blockwidth, blockheight));
			}

		}

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

		//block.destroyed();
		//block.draw(shape);
		//block.gameLevel();

		spielfield.rectField(shape);

		//shape.setColor(Color.BLUE);
		paddle.update();
		paddle.draw(shape);



		//ball.checkCollision(paddle);
		ball.checkCollision(block);

		for (Block b : blocks) {
			b.draw(shape);
			ball.checkCollision(b);
		}
		for (int i = 0; i < blocks.size(); i++) {
			Block b = blocks.get(i);
			if (b.destroyed) {
				blocks.remove(b);
				i--;
			}
		}
		shape.end();


	}


}
