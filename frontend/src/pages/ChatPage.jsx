import { useState, useEffect } from "react";

import Header from "../components/layout/Header";
import Sidebar from "../components/layout/Sidebar";
import ChatBox from "../components/chat/ChatBox";

const ChatPage = () => {

    const [theme, setTheme] = useState(
        localStorage.getItem("theme") || "dark"
    );

    const [messages, setMessages] = useState([]);

    const [history, setHistory] = useState([]);

    const [currentChatId, setCurrentChatId] = useState(null);

    useEffect(() => {

        document.body.className = theme;

        localStorage.setItem("theme", theme);

    }, [theme]);

    useEffect(() => {

        const storedHistory = JSON.parse(

            localStorage.getItem("smartassist-history") || "[]"

        );

        setHistory(storedHistory);

    }, []);

    const saveConversation = (chatMessages) => {

        if (chatMessages.length === 0) return;

        let updatedHistory = [...history];

        if (currentChatId) {

            updatedHistory = updatedHistory.map((chat) =>

                chat.id === currentChatId

                    ? {
                          ...chat,
                          messages: chatMessages,
                          createdAt: new Date().toLocaleString(),
                      }

                    : chat

            );

        }

        else {

            const newId = Date.now();

            setCurrentChatId(newId);

            updatedHistory.unshift({

                id: newId,

                createdAt: new Date().toLocaleString(),

                messages: chatMessages,

            });

        }

        setHistory(updatedHistory);

        localStorage.setItem(

            "smartassist-history",

            JSON.stringify(updatedHistory)

        );

    };

    useEffect(() => {

        if (messages.length > 0) {

            saveConversation(messages);

        }

    }, [messages]);

    const newChat = () => {

        setMessages([]);

        setCurrentChatId(null);

    };

    const loadConversation = (chat) => {

        setMessages(chat.messages);

        setCurrentChatId(chat.id);

    };

    return (

        <div className={`app-layout ${theme}`}>

            <Sidebar

                newChat={newChat}

                history={history}

                loadConversation={loadConversation}

            />

            <div className="main-content">

                <Header

                    theme={theme}

                    setTheme={setTheme}

                />

                <ChatBox

                    messages={messages}

                    setMessages={setMessages}

                />

            </div>

        </div>

    );

};

export default ChatPage;