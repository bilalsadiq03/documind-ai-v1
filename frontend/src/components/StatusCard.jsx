function StatusCard({ status }) {

  const getStatusData = () => {

    switch (status) {

      case "queued":
        return {
          title: "Analyzing Repository",
          description:
            "Scanning files and understanding project structure.",
        };

      case "processing":
        return {
          title: "Generating Documentation",
          description:
            "AI is creating your README and architecture overview.",
        };

      case "completed":
        return {
          title: "README Ready",
          description:
            "Documentation generated successfully.",
        };

      case "failed":
        return {
          title: "Generation Failed",
          description:
            "Something went wrong while generating documentation.",
        };

      default:
        return {
          title: "Starting",
          description:
            "Preparing generation process.",
        };
    }
  };

  const data = getStatusData();

  const completed = status === "completed";

  return (
    <div className="max-w-3xl mx-auto mt-10">

      <div className="border rounded-2xl bg-white shadow-sm p-8">

        <div className="flex items-start gap-4">

          <div
            className={`
              mt-2 h-4 w-4 rounded-full
              ${
                completed
                  ? "bg-green-500"
                  : "bg-blue-500 animate-pulse"
              }
            `}
          />

          <div className="flex-1">

            <h3 className="text-xl font-semibold">
              {data.title}
            </h3>

            <p className="text-gray-500 mt-2">
              {data.description}
            </p>

            <div className="mt-6">
                <div className="h-2 bg-gray-200 rounded-full overflow-hidden">
                    <div className={`h-full ${ status === "queued" ? "w-1/3" : status === "processing" ? "w-2/3" : status === "completed" ? "w-full": "w-0"} transition-all duration-700 bg-black`}/>
                </div>
            </div>

          </div>

        </div>

      </div>

    </div>
  );
}

export default StatusCard;