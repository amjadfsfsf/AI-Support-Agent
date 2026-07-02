import Message from "./Message";

export default function ChatWindow({ messages }) {

    return (

        <div
            style={{
                flex: 1,
                overflowY: "auto",
                background: "#0f172a",
                padding: "35px 0",
            }}
        >

            <div
                style={{
                    maxWidth: "950px",
                    margin: "0 auto",
                    padding: "0 25px",
                }}
            >

                {messages.map((message, index) => (

                    <Message
                        key={index}
                        sender={message.sender}
                        text={message.text}
                        sources={message.sources}
                    />

                ))}

            </div>

        </div>

    );

}