import ReactMarkdown from "react-markdown";

function ReadmeViewer({ content }) {
  return (
    <div className="mt-12">

      <div className="border rounded-2xl p-8 bg-white shadow-sm">

        <h2 className="text-2xl font-bold mb-6">
          Generated README
        </h2>

        <div className="prose max-w-none">
          <ReactMarkdown>
            {content}
          </ReactMarkdown>
        </div>

      </div>

    </div>
  );
}

export default ReadmeViewer;