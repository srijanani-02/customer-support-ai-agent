import { useEffect, useRef, useState } from "react";

import {
  KeyRound,
  BadgeDollarSign,
  Package,
  Wrench,
} from "lucide-react";

import api from "../../services/api";

import Message from "./Message";
import ChatInput from "./ChatInput";
import TypingIndicator from "./TypingIndicator";

const quickActions = [
  {
    icon: <KeyRound size={22} />,
    title: "Password Reset",
    query: "How do I reset my password?",
  },
  {
    icon: <BadgeDollarSign size={22} />,
    title: "Refund Policy",
    query: "What is your refund policy?",
  },
  {
    icon: <Package size={22} />,
    title: "Order Status",
    query: "Where is my order?",
  },
  {
    icon: <Wrench size={22} />,
    title: "Technical Support",
    query: "I need technical support.",
  },
];

const ChatBox = ({ messages, setMessages }) => {

    const [input, setInput] = useState("");

    const [loading, setLoading] = useState(false);

    const [waitingForAdditionalHelp, setWaitingForAdditionalHelp] = useState(false);

    const [showFollowUpCards, setShowFollowUpCards] = useState(false);

    const messageEndRef = useRef(null);

    useEffect(() => {

        messageEndRef.current?.scrollIntoView({

            behavior: "smooth",

        });

    }, [messages, loading]);

    const sendMessage = async (customQuery = "") => {

        const query = customQuery || input;

        if (!query.trim()) return;

        // -------------------------------
        // Handle YES / NO locally
        // -------------------------------

        if (waitingForAdditionalHelp) {

            const answer = query.trim().toLowerCase();

            const yesWords = [
                "yes",
                "yeah",
                "yep",
                "sure",
                "ok",
                "okay"
            ];

            const noWords = [
                "no",
                "nope",
                "nah"
            ];

            if (yesWords.includes(answer)) {

                setMessages((prev) => [

                    ...prev,

                    {
                        sender: "user",
                        text: query,
                    },

                    {
                        sender: "ai",
                        text:
                            "Sure! 😊\n\nWhat else can I help you with today?",
                        showQuickActions: true,
                    },

                ]);

                setWaitingForAdditionalHelp(false);

                setShowFollowUpCards(true);

                setInput("");

                return;

            }

            if (noWords.includes(answer)) {

                setMessages((prev) => [

                    ...prev,

                    {
                        sender: "user",
                        text: query,
                    },

                    {
                        sender: "ai",
                        text:
                            "You're welcome! 😊\n\nThank you for contacting SmartAssist.\n\nHave a wonderful day! 👋",
                    },

                ]);

                setWaitingForAdditionalHelp(false);

                setShowFollowUpCards(false);

                setInput("");

                return;

            }

        }

        const userMessage = {

            sender: "user",

            text: query,

        };

        setMessages((prev) => [

            ...prev,

            userMessage,

        ]);

        setInput("");

        setLoading(true);

        setShowFollowUpCards(false);

        try {

            const response = await api.post("/chat", {

                user_query: query,

            });

            const aiMessage = {

                sender: "ai",

                text: response.data.response,

                showQuickActions: false,

            };

            setMessages((prev) => [

                ...prev,

                aiMessage,

            ]);

            const responseText = response.data.response.toLowerCase();

            if (
                responseText.includes("is there anything else i can help you with") ||
                responseText.includes("do you need help with anything else")
            ) {
                setWaitingForAdditionalHelp(true);
            } else {
                setWaitingForAdditionalHelp(false);
            }

        }

        catch (error) {

            setMessages((prev) => [

                ...prev,

                {

                    sender: "ai",

                    text: "Something went wrong. Please try again.",

                },

            ]);

        }

        finally {

            setLoading(false);

        }

    };
    return (

    <div className="chat-box">

        {

            messages.length === 0 && (

                <div className="welcome">

                    <h1>

                        Welcome to SmartAssist 👋

                    </h1>

                    <p>

                        AI Powered Customer Support Assistant

                    </p>

                    <div className="quick-grid">

                        {

                            quickActions.map((item) => (

                                <div

                                    key={item.title}

                                    className="quick-card"

                                    onClick={() => sendMessage(item.query)}

                                >

                                    {item.icon}

                                    <h3>

                                        {item.title}

                                    </h3>

                                </div>

                            ))

                        }

                    </div>

                </div>

            )

        }

        <div className="messages">

            {

                messages.map((message, index) => (

                    <div key={index}>

                        <Message

                            sender={message.sender}

                            text={message.text}

                        />

                        {

                            message.sender === "ai" &&
                            message.showQuickActions &&
                            showFollowUpCards && (

                                <div
                                    className="quick-grid"
                                    style={{
                                        marginTop: "15px",
                                        marginBottom: "15px"
                                    }}
                                >

                                    {

                                        quickActions.map((item) => (

                                            <div

                                                key={item.title}

                                                className="quick-card"

                                                onClick={() => {

                                                    setShowFollowUpCards(false);

                                                    sendMessage(item.query);

                                                }}

                                            >

                                                {item.icon}

                                                <h3>

                                                    {item.title}

                                                </h3>

                                            </div>

                                        ))

                                    }

                                </div>

                            )

                        }

                    </div>

                ))

            }

            {

                loading && (

                    <TypingIndicator />

                )

            }

            <div

                ref={messageEndRef}

            />

        </div>

        <ChatInput

            input={input}

            setInput={setInput}

            sendMessage={sendMessage}

        />

    </div>

);

};

export default ChatBox;