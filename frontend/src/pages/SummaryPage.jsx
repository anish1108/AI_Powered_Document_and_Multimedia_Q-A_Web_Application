import { useState } from "react";
import api from "../api/client";

export default function SummaryPage() {
  const transcriptId = localStorage.getItem("transcript_id");
  const [summary, setSummary] = useState("");

  const getSummary = async () => {
    const fd = new FormData();
    fd.append("transcript_id", transcriptId);

    const res = await api.post("summary/", fd);
    setSummary(res.data.summary);
  };

  return (
    <div className="p-6">
      <button
        onClick={getSummary}
        className="bg-purple-600 text-white px-6 py-2"
      >
        Generate Summary
      </button>

      {summary && (
        <p className="mt-4 border p-4 bg-gray-100">{summary}</p>
      )}
    </div>
  );
}
