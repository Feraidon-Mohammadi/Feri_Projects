import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEnvelope } from "@fortawesome/free-solid-svg-icons";

export default function Test() {
  const firstName = "John";
  const lastName = "Doe";
  const now = new Date();
  const hours = now.getHours();
  const greeting =
    hours < 12
      ? "Guten Morgen"
      : hours < 18
      ? "Guten Tag"
      : hours < 22
      ? "Guten Abend"
      : "Gute Nacht";

  // return <h1>Hello {firstName + " " + lastName + "!"}</h1>;
  // return <h1>Hello {`${firstName} ${lastName}!`}</h1>;
  return (
    <h1>
      <FontAwesomeIcon icon={faEnvelope} />
      {greeting} {firstName} {lastName}! Es ist {now.toLocaleTimeString()}.
    </h1>
  );
}

export function ReactRendersArrays() {
  const colors = [<h3>Red</h3>, <h3>Green</h3>, <h3>Blue</h3>];
  const names = ["alice", "bob", "charlie"];
  const numbers = [1, 2, 3, 4];
  const booleans = [true, false];
  const objects = [
    { a: 1, b: 2 },
    { a: 4, b: 5 },
  ];
  return (
    <div>
      {colors}
      {names}
      {numbers}
      {booleans.map((b) => b.toString())}
      {/* {booleans} Boolesche Werte werden nicht dargestellt */}
      {/* {objects} Reine Objekte lassen sich nicht rendern. */}
    </div>
  );
}
