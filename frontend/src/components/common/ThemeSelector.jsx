import { Moon, Sun } from "lucide-react";

const ThemeSelector = ({
    theme,
    setTheme
}) => {

    const toggleTheme = () => {

        const nextTheme =
            theme === "dark"
                ? "light"
                : "dark";

        setTheme(nextTheme);

    };

    return (

        <button

            className="icon-btn"

            onClick={toggleTheme}

            title="Change Theme"

        >

            {

                theme === "dark"

                    ? <Sun size={20}/>

                    : <Moon size={20}/>

            }

        </button>

    );

};

export default ThemeSelector;