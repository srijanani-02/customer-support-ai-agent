import { useState, useRef } from "react";
import { Mic, Square, SendHorizontal } from "lucide-react";

const ChatInput = ({
    input,
    setInput,
    sendMessage
}) => {

    const [isRecording, setIsRecording] = useState(false);

    const recognitionRef = useRef(null);

    const finalTranscriptRef = useRef("");

    const startRecording = () => {

        const SpeechRecognition =
            window.SpeechRecognition ||
            window.webkitSpeechRecognition;

        if (!SpeechRecognition) {

            alert("Speech Recognition is not supported in this browser.");

            return;

        }

        finalTranscriptRef.current = "";

        const recognition = new SpeechRecognition();

        recognitionRef.current = recognition;

        recognition.lang = "en-US";

        recognition.continuous = true;

        recognition.interimResults = true;

        recognition.maxAlternatives = 1;

        recognition.onstart = () => {

            setIsRecording(true);

        };

        recognition.onresult = (event) => {

            let finalText = finalTranscriptRef.current;

            let interimText = "";

            for (let i = event.resultIndex; i < event.results.length; i++) {

                if (event.results[i].isFinal) {

                    finalText += event.results[i][0].transcript + " ";

                } else {

                    interimText += event.results[i][0].transcript;

                }

            }

            finalTranscriptRef.current = finalText;

            setInput((finalText + interimText).trim());

        };

        recognition.onerror = (event) => {

            console.error(event.error);

        };

        recognition.onend = () => {

            if (isRecording) {

                recognition.start();

            }

        };

        recognition.start();

    };

    const stopRecording = () => {

        setIsRecording(false);

        if (recognitionRef.current) {

            recognitionRef.current.onend = null;

            recognitionRef.current.stop();

        }

        const finalText = finalTranscriptRef.current.trim();

        if (finalText.length > 0) {

            setInput(finalText);

            setTimeout(() => {

                sendMessage(finalText);

                setInput("");

                finalTranscriptRef.current = "";

            }, 300);

        }

    };

    return (

        <div className="chat-input-container">

            <input

                type="text"

                placeholder={
                    isRecording
                        ? "🎤 Listening..."
                        : "Ask SmartAssist anything..."
                }

                value={input}

                onChange={(e) => setInput(e.target.value)}

                onKeyDown={(e) => {

                    if (e.key === "Enter") {

                        sendMessage();

                    }

                }}

            />

            {

                isRecording ? (

                    <button

                        className="icon-btn listening"

                        onClick={stopRecording}

                        title="Stop Recording"

                    >

                        <Square size={18}/>

                    </button>

                ) : (

                    <button

                        className="icon-btn"

                        onClick={startRecording}

                        title="Start Recording"

                    >

                        <Mic size={20}/>

                    </button>

                )

            }

            <button

                className="send-btn"

                onClick={() => sendMessage()}

            >

                <SendHorizontal size={20}/>

            </button>

        </div>

    );

};

export default ChatInput;