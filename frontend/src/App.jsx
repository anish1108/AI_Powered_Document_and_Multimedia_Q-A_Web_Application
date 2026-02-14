import { BrowserRouter, Routes, Route } from "react-router-dom";
import UploadPage from "./pages/UploadPage";
import ChatPage from "./pages/ChatPage";
import SummaryPage from "./pages/SummaryPage";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<UploadPage />} />
        <Route path="/chat" element={<ChatPage />} />
        <Route path="/summary" element={<SummaryPage />} />
      </Routes>
    </BrowserRouter>
  );
}
