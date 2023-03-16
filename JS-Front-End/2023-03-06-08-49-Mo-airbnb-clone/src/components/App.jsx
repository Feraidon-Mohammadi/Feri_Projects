import NavBar from "./NavBar.jsx";
import Hero from "./Hero.jsx";
import Card from "./Card.jsx";
import Test from "./Test.jsx";
import { ReactRendersArrays } from "./Test.jsx";
import Contact from "./Contact.jsx";
import Joke from "./Joke.jsx";
import jokesData from "../assets/jokesData.js";

import zaferesUrl from "../assets/katie-zaferes.png";

export default function App() {
  return (
    <>
      {/*
      <Contact
        img="/src/assets/mr-whiskerson.png"
        name="Mr. Whiskerson"
        phone="(212) 555-1234"
        email="mr.whiskaz@catnap.meow"
      />
      <Contact
        img="/src/assets/fluffykins.png"
        name="Fluffykins"
        phone="(212) 555-2345"
        email="fluff@me.com"
      />
      <Contact
        img="/src/assets/felix.png"
        name="Felix"
        phone="(212) 555-4567"
        email="thecat@hotmail.com"
      />
      <Contact
        img="/src/assets/pumpkin.png"
        name="Pumpkin"
        phone="(0800) CAT KING"
        email="pumpkin@scrimba.com"
      /> */}
      {/* <NavBar />
      <Hero />
      <Card
        img={zaferesUrl}
        badge="sold out"
        rating="5.0"
        reviewCount={6}
        country="USA"
        price={136}
        title="Life lessions with Katie Zaferes"
      /> */}
      {/* <ReactRendersArrays /> */}
      {jokesData.map((joke) => (
        <Joke setup={joke.setup} punchline={joke.punchline} comments={["nice"]} />
      ))}
    </>
  );
}
