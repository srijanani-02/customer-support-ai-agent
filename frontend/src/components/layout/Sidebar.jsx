import "./../../styles/sidebar.css";

import {
  SquarePen,
  History,
  Settings,
  Bot,
  Clock3,
  KeyRound,
  BadgeDollarSign,
  Package,
  Wrench,
  MessageCircle,
} from "lucide-react";

const Sidebar = ({
  newChat,
  history,
  loadConversation,
}) => {

  const getChatInfo = (messages = []) => {

    if (!messages.length) {

      return {
        title: "General Inquiry",
        icon: <MessageCircle size={18} />,
      };

    }

    const text = messages[0].text.toLowerCase();

    if (text.includes("password")) {

      return {
        title: "Password Reset",
        icon: <KeyRound size={18} />,
      };

    }

    if (text.includes("refund")) {

      return {
        title: "Refund Request",
        icon: <BadgeDollarSign size={18} />,
      };

    }

    if (text.includes("order")) {

      return {
        title: "Order Tracking",
        icon: <Package size={18} />,
      };

    }

    if (
      text.includes("technical") ||
      text.includes("error")
    ) {

      return {
        title: "Technical Issue",
        icon: <Wrench size={18} />,
      };

    }

    return {
      title: "General Inquiry",
      icon: <MessageCircle size={18} />,
    };

  };

  return (

    <aside className="sidebar">

      <div className="sidebar-logo">

        <Bot size={34} />

        <div>

          <h2>SmartAssist</h2>

          <p>Support AI</p>

        </div>

      </div>

      <button

        className="new-chat"

        onClick={newChat}

      >

        <SquarePen size={20} />

        <span>New Chat</span>

      </button>

      <div className="history-section">

        <div className="history-heading">

          <History size={17} />

          <span>Recent Conversations</span>

        </div>

        {

          history.length === 0 ? (

            <div className="empty-history">

              No conversations yet

            </div>

          ) : (

            history.map((chat) => {

              const info = getChatInfo(chat.messages);

              return (

                <div

                  key={chat.id}

                  className="history-card"

                  onClick={() => loadConversation(chat)}

                >

                  <div className="history-card-top">

                    {info.icon}

                    <span>{info.title}</span>

                  </div>

                  <div className="history-time">

                    <Clock3 size={13} />

                    <span>{chat.createdAt}</span>

                  </div>

                </div>

              );

            })

          )

        }

      </div>

      <nav>

        <button>

          <Settings size={20} />

          <span>Settings</span>

        </button>

      </nav>

    </aside>

  );

};

export default Sidebar;