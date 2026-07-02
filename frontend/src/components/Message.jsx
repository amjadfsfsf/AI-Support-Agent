export default function Message({ sender, text, sources }) {

    const isUser = sender === "user";

    return (
        <div
            style={{
                display: "flex",
                justifyContent: isUser ? "flex-end" : "flex-start",
                marginBottom: "24px",
            }}
        >
            <div
                style={{
                    display: "flex",
                    flexDirection: isUser ? "row-reverse" : "row",
                    alignItems: "flex-start",
                    gap: "12px",
                    maxWidth: "80%",
                }}
            >
                {/* Avatar */}

                <div
                    style={{
                        width: "42px",
                        height: "42px",
                        borderRadius: "50%",
                        background: isUser ? "#2563eb" : "#1e293b",
                        display: "flex",
                        justifyContent: "center",
                        alignItems: "center",
                        fontSize: "20px",
                        flexShrink: 0,
                    }}
                >
                    {isUser ? "👤" : "🤖"}
                </div>

                {/* Bubble */}

                <div
                    style={{
                        background: isUser ? "#2563eb" : "#1e293b",
                        color: "#f8fafc",
                        padding: "18px",
                        borderRadius: "18px",
                        lineHeight: "1.7",
                        boxShadow: "0 6px 18px rgba(0,0,0,0.20)",
                        border: isUser
                            ? "1px solid #3b82f6"
                            : "1px solid #334155",
                        wordBreak: "break-word",
                    }}
                >
                    {/* Sender */}

                    <div
                        style={{
                            fontSize: "13px",
                            fontWeight: "700",
                            color: isUser ? "#dbeafe" : "#93c5fd",
                            marginBottom: "10px",
                        }}
                    >
                        {isUser ? "You" : "AI Assistant"}
                    </div>

                    {/* Message */}

                    <div
                        style={{
                            whiteSpace: "pre-wrap",
                            fontSize: "15px",
                        }}
                    >
                        {text}
                    </div>

                    {/* Sources */}

                    {sources && sources.length > 0 && (

                        <div
                            style={{
                                marginTop: "18px",
                                paddingTop: "15px",
                                borderTop: "1px solid rgba(255,255,255,0.08)",
                            }}
                        >
                            <div
                                style={{
                                    fontWeight: "600",
                                    marginBottom: "10px",
                                    color: "#cbd5e1",
                                    fontSize: "14px",
                                }}
                            >
                                📚 Sources
                            </div>

                            {sources.map((source, index) => (

                                <div
                                    key={index}
                                    style={{
                                        background: "#0f172a",
                                        border: "1px solid #334155",
                                        borderRadius: "10px",
                                        padding: "10px 12px",
                                        marginBottom: "8px",
                                        fontSize: "13px",
                                        color: "#cbd5e1",
                                    }}
                                >
                                    📄 <strong>{source.file}</strong>

                                    <div
                                        style={{
                                            marginTop: "4px",
                                            color: "#94a3b8",
                                        }}
                                    >
                                        Page {source.page}
                                    </div>
                                </div>

                            ))}

                        </div>

                    )}

                </div>

            </div>

        </div>
    );

}