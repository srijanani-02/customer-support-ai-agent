import "./../../styles/header.css";

import { Bot, Volume2 } from "lucide-react";

import ThemeSelector from "../common/ThemeSelector";

const Header = ({
    theme,
    setTheme
}) => {

    return (

        <header className="header">

            <div className="logo-section">

                <Bot size={34} />

                <div>

                    <h1>SmartAssist</h1>

                    <p>AI Powered Customer Support</p>

                </div>

            </div>

            <div className="header-right">

                <div className="status">

                    <span className="dot"></span>

                    Active AI

                </div>

                <ThemeSelector
                    theme={theme}
                    setTheme={setTheme}
                />

                <button
                    className="icon-btn"
                    title="Toggle Voice Output"
                >
                    <Volume2 size={20}/>
                </button>

            </div>

        </header>

    );

};

export default Header;