import { useState } from "react";

import Sidebar from "../components/Sidebar";
import Header from "../components/Header";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";

const sessionId = "user-1";

export default function Chat() {

    const [messages, setMessages] = useState([
        {
            sender: "assistant",
            text: "👋 Hello! I'm your AI Customer Support Assistant.\n\nHow can I help you today?"
        }
    ]);

    const handleSend = async (message) => {

        setMessages(prev => [
            ...prev,
            {
                sender: "user",
                text: message
            }
        ]);

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/chat",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        session_id: sessionId,
                        message: message
                    })
                }
            );

            const data = await response.json();

            setMessages(prev => [
                ...prev,
                {
                    sender: "assistant",
                    text: data.answer,
                    sources: data.sources
                }
            ]);

        } catch (error) {

            setMessages(prev => [
                ...prev,
                {
                    sender: "assistant",
                    text: "❌ Failed to connect to the backend."
                }
            ]);

        }

    };

    return (

        <div
            style={{
                display: "flex",
                height: "100vh",
                background: "#020617",
                color: "#f8fafc",
                fontFamily:
                    "Inter, Segoe UI, Arial, sans-serif",
            }}
        >

            <Sidebar />

            <div
                style={{
                    flex: 1,
                    display: "flex",
                    flexDirection: "column",
                    overflow: "hidden",
                }}
            >

                <Header />

                <ChatWindow
                    messages={messages}
                />

                <ChatInput
                    onSend={handleSend}
                />

            </div>

        </div>

    );

}