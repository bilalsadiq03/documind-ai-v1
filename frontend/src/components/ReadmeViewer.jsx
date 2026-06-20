import ReactMarkdown from "react-markdown";

function ReadmeViewer({ content, jobId }) {

  const copyMarkdown = async () => {
    await navigator.clipboard.writeText(content);
    alert("README copied to clipboard");
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

    document.body.appendChild(a);

    a.click();

    document.body.removeChild(a);

    URL.revokeObjectURL(url);
  };

  return (
    <div className="mt-12">

      <div className="border rounded-2xl p-8 bg-white shadow-sm">

        <div className="flex items-center justify-between mb-6">

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

        <hr className="mb-8" />

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