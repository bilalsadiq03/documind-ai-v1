import { useState, useEffect } from "react";

import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import RepoForm from "./components/RepoForm";
import Footer from "./components/Footer";
import StatusCard from "./components/StatusCard";
import ReadmeViewer from "./components/ReadmeViewer";

import api from "./services/api";

function App() {

  const [jobId, setJobId] = useState("");
  const [status, setStatus] = useState("");
  const [loading, setLoading] = useState(false);
  const [readme, setReadme] = useState("");

  const handleGenerate = async (repoUrl) => {

    try {

      setLoading(true);

      const response = await api.post("/generate", {
        repo_url: repoUrl,
      });

      setJobId(response.data.job_id);
      setStatus("queued");
      setReadme("");

    } catch (error) {

      console.error(error);
      alert("Failed to generate README");

    } finally {

      setLoading(false);

    }
  };

  useEffect(() => {

    if (!jobId) return;

    const interval = setInterval(async () => {

      try {

        const response = await api.get(
          `/jobs/${jobId}`
        );

        const currentStatus =
          response.data.status;

        setStatus(currentStatus);

        if (currentStatus === "completed") {

          clearInterval(interval);

          const readmeResponse =
            await api.get(
              `/jobs/${jobId}/readme`
            );

          setReadme(
            readmeResponse.data.content
          );
        }

        if (currentStatus === "failed") {
          clearInterval(interval);
        }

      } catch (error) {
        console.error(error);
      }

    }, 2000);

    return () => clearInterval(interval);

  }, [jobId]);

  return (
    <div className="min-h-screen bg-white">

      <Navbar />

      <main className="max-w-6xl mx-auto px-6">

        <Hero />

        <RepoForm
          onGenerate={handleGenerate}
          loading={loading}
        />

        {!status && (
          <div className="text-center py-16 text-gray-500">
            Paste a GitHub repository URL to generate
            professional documentation.
          </div>
        )}

        {status && (
          <StatusCard status={status} />
        )}

        {readme && (
          <ReadmeViewer content={readme} />
        )}

      </main>

      <Footer />

    </div>
  );
}

export default App;