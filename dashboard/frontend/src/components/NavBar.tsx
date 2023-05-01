import React from 'react';
import './NavBar.css';

interface NavBarProps {
  toggleDashboard: () => void;
  toggleTapForm: () => void;
}

const NavBar: React.FC<NavBarProps> = ({ toggleDashboard, toggleTapForm }: NavBarProps) => {
  return (
    <nav className="navBar">
      <div className="navWrapper">
        <a id="navPhlask" href="#">Phlask Admin</a>
      </div>
      <ul className="navList">
        <li className="navItem">
          <a href="/">How to use</a>
        </li>
        <li className="navItem">
          <a href="/about">Change Resource</a>
        </li>
        <li className="navItem">
          <a href="/contact">Contact</a>
        </li>
      </ul>
      <button className="toggleButton" onClick={toggleDashboard}>
        Toggle Dashboard
      </button>
      <button className="toggleButton" onClick={toggleTapForm}>
        Toggle Tap Form
      </button>
      
    </nav>
  );
};

export default NavBar;
