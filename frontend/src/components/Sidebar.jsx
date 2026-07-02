export default function Sidebar() {
    return (
        <div
            style={{
                width: "280px",
                background: "#111827",
                borderRight: "1px solid #1f2937",
                display: "flex",
                flexDirection: "column",
                padding: "24px",
            }}
        >
            {/* Logo */}
            <div
                style={{
                    textAlign: "center",
                    marginBottom: "30px",
                }}
            >
                <h2
                    style={{
                        margin: 0,
                        color: "#ffffff",
                        fontSize: "34px",
                        fontWeight: "700",
                    }}
                >
                    🤖 AI Support
                </h2>

                <p
                    style={{
                        marginTop: "8px",
                        color: "#94a3b8",
                        fontSize: "14px",
                    }}
                >
                    Customer Support Assistant
                </p>
            </div>

            {/* New Chat Button */}
            <button
                style={{
                    width: "100%",
                    padding: "15px",
                    background: "#2563eb",
                    color: "white",
                    border: "none",
                    borderRadius: "12px",
                    cursor: "pointer",
                    fontWeight: "600",
                    fontSize: "15px",
                    transition: "0.2s",
                    boxShadow: "0 4px 15px rgba(37,99,235,0.35)",
                }}
            >
                + New Chat
            </button>

            {/* Recent Chats */}
            <div
                style={{
                    marginTop: "35px",
                }}
            >
                <p
                    style={{
                        color: "#94a3b8",
                        fontSize: "13px",
                        marginBottom: "15px",
                        letterSpacing: "1px",
                    }}
                >
                    RECENT CHATS
                </p>

                {[
                    "Support Ticket",
                    "Order Tracking",
                    "Calculator"
                ].map((chat, index) => (
                    <div
                        key={index}
                        style={{
                            padding: "14px",
                            marginBottom: "10px",
                            borderRadius: "10px",
                            background: "#1e293b",
                            color: "#e2e8f0",
                            cursor: "pointer",
                            border: "1px solid transparent",
                        }}
                    >
                        💬 {chat}
                    </div>
                ))}
            </div>

            {/* Footer */}
            <div
                style={{
                    marginTop: "auto",
                    textAlign: "center",
                    color: "#64748b",
                    fontSize: "12px",
                    paddingTop: "20px",
                    borderTop: "1px solid #1f2937",
                }}
            >
                Powered by
                <br />
                <strong style={{ color: "#cbd5e1" }}>
                    Ollama • MCP • RAG
                </strong>
            </div>
        </div>
    );
}