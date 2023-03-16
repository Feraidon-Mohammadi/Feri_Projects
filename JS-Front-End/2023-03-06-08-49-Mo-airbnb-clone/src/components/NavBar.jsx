import logoUrl from "../assets/airbnb-logo.png";

export default function NavBar() {
  return (
    <header>
      <nav className="nav-bar">
        <img src={logoUrl} className="nav-bar__logo" />
      </nav>
    </header>
  );
}
