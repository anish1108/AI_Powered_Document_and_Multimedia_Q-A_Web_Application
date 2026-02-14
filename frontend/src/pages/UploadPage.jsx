import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/client";

export default function UploadPage() {
    const [file, setFile] = useState(null);
    const [error, setError] = useState("");
    const navigate = useNavigate();

    const upload = async () => {
        setError("");

        if (!file) {
            setError("Please select a file");
            return;
        }

        try {
            const fd = new FormData();
            fd.append("file", file);

            const res = await api.post("upload/", fd);

            if (!res.data.transcript_id) {
                setError("Transcript not generated");
                return;
            }

            localStorage.setItem(
                "transcript_id",
                String(res.data.transcript_id)
            );

            localStorage.setItem(
                "file_url",
                res.data.file_url
            );

            navigate("/chat");
        } catch (err) {
            setError("Upload failed");
        }
    };


    return (
        <div className="h-screen flex flex-col items-center justify-center">
            <h1 className="text-2xl font-bold mb-4">Upload File</h1>

            <input
                type="file"
                onChange={(e) => setFile(e.target.files[0])}
                className="mb-3"
            />

            <button
                onClick={upload}
                className="bg-blue-600 text-white px-6 py-2 rounded"
            >
                Upload
            </button>

            {error && <p className="text-red-500 mt-3">{error}</p>}
        </div>
    );
}
