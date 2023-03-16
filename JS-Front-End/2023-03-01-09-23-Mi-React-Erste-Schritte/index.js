const root = document.querySelector("#root");

// JSX = JavaScript with XML
// Damit JSX Code vom Browser ausgeführt werden kann, muss der Code
// zunächst mit einem Präprozessor (hier Babel) in herkömmlichen
// JavaScript Code übersetzt werden.
ReactDOM.render(<h1>Hello everyone</h1>, root);
// Die obige Zeile lässt sich auch in herkömmlichem JavaScript wie folgt
// schreiben:
// const content = React.createElement("h1", {}, "Hello everyone");
// ReactDOM.render(content, document.querySelector("#root"));

ReactDOM.render(
  <ul>
    <li>Item 1</li>
    <li>Item 2</li>
  </ul>,
  root
);

function MainContent() {
  return <h1>I'm learning React!</h1>;
}

// Deklarativer Programmierstil
ReactDOM.render(
  <div>
    <MainContent />
    <MainContent />
    <MainContent />
  </div>,
  root
);

// Imperativer Programmierstil
// const myHeading = document.createElement("h1");
// myHeading.classList.add("header");
// myHeading.innerText = "Das ist ein Heading";
// root.append(myHeading);

const page = (
  <div>
    <h1 className="header">This is JSX.</h1>
    <p>This is a paragraph.</p>
  </div>
);

const navigationBar = (
  <nav>
    <h1>Schenker Technologies</h1>
    <ul>
      <li>Pricing</li>
      <li>About</li>
      <li>Contact</li>
    </ul>
  </nav>
);

ReactDOM.render(navigationBar, root);
