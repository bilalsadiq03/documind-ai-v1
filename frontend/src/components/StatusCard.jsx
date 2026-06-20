function StatusCard({ status }) {

    const isCompleted = status === "completed";

  const getMessage = () => {

    switch (status) {

      case "queued":
        return "Preparing your repository...";

      case "processing":
        return "Generating documentation...";

      case "completed":
        return "README generated successfully";

      case "failed":
        return "Generation failed";

      default:
        return "Starting...";
    }
  };

  return (
    <div className="max-w-2xl mx-auto mt-12">

      <div className="border rounded-2xl p-8 bg-white shadow-sm">

        <div className="flex items-center gap-4">

          <div className="w-4 h-4 rounded-full bg-black animate-pulse" />

          <div>

            <h3 className="font-semibold text-lg">
              {getMessage()}
            </h3>

            <p className="text-gray-500 capitalize">
              Status: {status}
            </p>

            <div className={`w-4 h-4 rounded-full ${isCompleted ? "bg-green-500" : "bg-black animate-pulse"}`} />

          </div>

        </div>

      </div>

    </div>
  );
}

export default StatusCard;