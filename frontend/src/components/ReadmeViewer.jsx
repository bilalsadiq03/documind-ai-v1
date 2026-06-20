import ReactMarkdown from "react-markdown";

function ReadmeViewer({ content }) {

  const copyMarkdown = async () => {
    await navigator.clipboard.writeText(content);
    alert("README copied successfully");
  };

  const downloadReadme = () => {

    const blob = new Blob(
      [content],
      { type: "text/markdown" }
    );

    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;
    a.download = "README.md";

    a.click();

    URL.revokeObjectURL(url);
  };

  return (
    <div
      className="
        mt-12
        border
        rounded-2xl
        bg-white
        shadow-sm
        overflow-hidden
      "
    >

      <div
        className="
          border-b
          px-8
          py-6
          flex
          items-center
          justify-between
        "
      >

        <div>
          <h2 className="text-2xl font-bold">
            README Generated
          </h2>

          <p className="text-gray-500">
            Your documentation is ready.
          </p>
        </div>

        <div className="flex gap-3">

          <button
            onClick={copyMarkdown}
            className="
              border
              px-4
              py-2
              rounded-lg
            "
          >
            Copy Markdown
          </button>

          <button
            onClick={downloadReadme}
            className="
              bg-black
              text-white
              px-4
              py-2
              rounded-lg
            "
          >
            Download
          </button>

        </div>

      </div>

      <div className="p-8">

        <div className="prose lg:prose-lg max-w-none">
          <ReactMarkdown>
            {content}
          </ReactMarkdown>
        </div>

      </div>

    </div>
  );
}

export default ReadmeViewer;