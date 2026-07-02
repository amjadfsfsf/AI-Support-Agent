export default function Header() {
    return (
        <div
            style={{
                height: "80px",
                padding: "0 30px",
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                background: "#0f172a",
                borderBottom: "1px solid #1f2937",
            }}
        >
            {/* Left */}
            <div>
                <h2
                    style={{
                        margin: 0,
                        color: "#f8fafc",
                        fontSize: "24px",
                        fontWeight: "700",
                    }}
                >
                    🤖 AI Customer Support Agent
                </h2>

                <p
                    style={{
                        margin: "6px 0 0",
                        color: "#94a3b8",
                        fontSize: "14px",
                    }}
                >
                    Powered by Ollama • MCP • RAG
                </p>
            </div>

            {/* Right */}
            <div
                style={{
                    display: "flex",
                    alignItems: "center",
                    gap: "10px",
                    background: "#1e293b",
                    padding: "10px 16px",
                    borderRadius: "999px",
                    border: "1px solid #334155",
                }}
            >
                <div
                    style={{
                        width: "10px",
                        height: "10px",
                        borderRadius: "50%",
                        background: "#22c55e",
                    }}
                />

                <span
                    style={{
                        color: "#e2e8f0",
                        fontSize: "14px",
                        fontWeight: "600",
                    }}
                >
                    AI Online
                </span>
            </div>
        </div>
    );
}