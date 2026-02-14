export default function MediaPlayer({ fileUrl, start }) {
  return (
    <div className="mt-6">
      <audio
        controls
        src={`http://127.0.0.1:8000${fileUrl}`}
        onLoadedMetadata={(e) => {
          e.target.currentTime = start;
        }}
      />
    </div>
  );
}
