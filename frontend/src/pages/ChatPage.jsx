// import { useState } from "react";
import api from "../api/client";
import MediaPlayer from "../components/MediaPlayer";
import { useState, useEffect } from "react";


export default function ChatPage() {

  const [summary, setSummary] = useState("");
  const [loadingSummary, setLoadingSummary] = useState(false);

  const transcriptId = localStorage.getItem("transcript_id");
  const fileUrl = localStorage.getItem("file_url");

  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [answer, setAnswer] = useState(null);
  const [error, setError] = useState("");

  if (!transcriptId) {
    return (
      <div className="p-10 text-center text-red-600 font-bold">
        Please upload a file first.
      </div>
    );
  }

  const fetchSummary = async () => {
  try {
    setLoadingSummary(true);

    const fd = new FormData();
    fd.append("transcript_id", transcriptId);

    const res = await api.post("summary/", fd);

    setSummary(res.data.summary);
  } catch (err) {
    console.log(err);
    setSummary("Failed to load summary.");
  } finally {
    setLoadingSummary(false);
  }
};


  const ask = async () => {
    setError("");

    if (!question.trim()) {
      setError("Please type a question");
      return;
    }

    try {
      const fd = new FormData();
      fd.append("transcript_id", transcriptId);
      fd.append("question", question);

      const res = await api.post("ask/", fd);

      setMessages((prev) => [
        ...prev,
        { role: "user", text: question },
        { role: "bot", text: res.data.answer },
      ]);

      setAnswer(res.data);
      setQuestion("");
    } catch (err) {
      console.log('erro s is '+ err);
      setError("Failed to get answer");
    }
  };

  useEffect(() => {
  if (transcriptId) {
    fetchSummary();
  }
}, [transcriptId]);


  return (
  <div className="h-screen grid grid-cols-3">

 
    <div className="col-span-1 border-r p-6 bg-gray-50 overflow-y-auto">

      <h2 className="text-xl font-bold mb-4">
        📄 Content Summary
      </h2>

      {loadingSummary ? (
        <p className="text-gray-500">Generating summary...</p>
      ) : (
        <p className="text-gray-700 whitespace-pre-line">
          {summary || "No summary available."}
        </p>
      )}

      <button
        onClick={fetchSummary}
        className="mt-4 bg-blue-500 text-white px-3 py-1 rounded"
      >
        Regenerate Summary
      </button>
    </div>


 
    <div className="col-span-2 p-6 max-w-3xl mx-auto w-full flex flex-col">

      <h2 className="text-xl font-bold mb-4">🤖 AI Chat</h2>

   
      <div className="border p-4 h-80 overflow-y-auto mb-4 bg-white rounded">
        {messages.map((m, i) => (
          <p
            key={i}
            className={`mb-2 ${
              m.role === "user" ? "text-right" : "text-left"
            }`}
          >
            <b>{m.role === "user" ? "You" : "AI"}:</b> {m.text}
          </p>
        ))}
      </div>

    
      <div className="flex gap-2">
        <input
          className="border w-full p-2 rounded"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask something..."
        />

        <button
          onClick={ask}
          className="bg-green-600 text-white px-4 rounded"
        >
          Send
        </button>
      </div>

      {error && (
        <p className="text-red-600 mt-2">{error}</p>
      )}


      {answer && (
        <MediaPlayer
          fileUrl={fileUrl}
          start={answer.start_time}
        />
      )}

    </div>
  </div>
);
}
