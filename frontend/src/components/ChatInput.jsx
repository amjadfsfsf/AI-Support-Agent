import { useState } from "react";

export default function ChatInput({ onSend }) {

    const [message, setMessage] = useState("");

    const send = () => {

        if (!message.trim()) return;

        onSend(message);

        setMessage("");
    };

    return (

        <div
            style={{
                padding: "22px",
                borderTop: "1px solid #1f2937",
                background: "#111827",
            }}
        >

            <div
                style={{
                    display: "flex",
                    alignItems: "center",
                    gap: "15px",
                    maxWidth: "1200px",
                    margin: "0 auto",
                }}
            >

                <input

                    value={message}

                    onChange={(e) => setMessage(e.target.value)}

                    onKeyDown={(e) => {

                        if (e.key === "Enter") {

                            send();

                        }

                    }}

                    placeholder="Ask anything..."

                    style={{
                        flex: 1,
                        padding: "16px 20px",
                        borderRadius: "16px",
                        border: "1px solid #334155",
                        background: "#0f172a",
                        color: "#f8fafc",
                        outline: "none",
                        fontSize: "15px",
                        transition: "0.2s",
                    }}

                />

                <button

                    onClick={send}

                    style={{
                        padding: "16px 24px",
                        background: "#2563eb",
                        color: "white",
                        border: "none",
                        borderRadius: "16px",
                        cursor: "pointer",
                        fontWeight: "600",
                        fontSize: "15px",
                        boxShadow: "0 6px 18px rgba(37,99,235,.35)",
                        transition: "0.2s",
                    }}

                >

                    ➤ Send

                </button>

            </div>

        </div>

    );

}