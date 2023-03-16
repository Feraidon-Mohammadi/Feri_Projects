import React from "react";
import reactLogoUrl from "./assets/react.svg";

export default function PageHeader() {
  return (
    <header>
      <nav className="nav-bar">
        <img src={reactLogoUrl} alt="React Logo" className="nav-bar__logo" />
        <ul className="nav-bar__menu no-markers">
          <li>Pricing</li>
          <li>About</li>
          <li>Contact</li>
        </ul>
      </nav>
    </header>
  );
}
