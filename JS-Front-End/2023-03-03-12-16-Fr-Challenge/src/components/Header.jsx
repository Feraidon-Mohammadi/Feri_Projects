import reactLogo from "../assets/react.svg";

export default function Header() {
  return (
    <header>
      <nav className="nav-bar">
        <img src={reactLogo} className="nav-bar__logo" />
        <h1 className="nav-bar__title">ReactFacts</h1>
        <h2 className="nav-bar__sub-title">React Course - Project 1</h2>
      </nav>
    </header>
  );
}
