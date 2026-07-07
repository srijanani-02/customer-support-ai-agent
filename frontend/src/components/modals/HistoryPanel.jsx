import "./../../styles/history.css";

import { X, MessageSquare } from "lucide-react";

const HistoryPanel = ({
    isOpen,
    onClose,
    history,
    loadConversation
}) => {

    if (!isOpen) return null;

    return (

        <div className="history-overlay">

            <div className="history-panel">

                <div className="history-header">

                    <h2>Chat History</h2>

                    <button
                        className="icon-btn"
                        onClick={onClose}
                    >
                        <X size={20}/>
                    </button>

                </div>

                {

                    history.length === 0 ? (

                        <div className="empty-history">

                            <MessageSquare size={42}/>

                            <p>No previous conversations.</p>

                        </div>

                    ) : (

                        <div className="history-list">

                            {

                                history.map((chat) => (

                                    <div

                                        key={chat.id}

                                        className="history-item"

                                        onClick={() => loadConversation(chat)}

                                    >

                                        <MessageSquare size={18}/>

                                        <div>

                                            <h4>

                                                {chat.createdAt}

                                            </h4>

                                            <p>

                                                {

                                                    chat.messages[0]?.text ||

                                                    "Conversation"

                                                }

                                            </p>

                                        </div>

                                    </div>

                                ))

                            }

                        </div>

                    )

                }

            </div>

        </div>

    );

};

export default HistoryPanel;